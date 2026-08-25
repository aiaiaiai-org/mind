#!/usr/bin/env python3
# © 2026 aiaiaiai · aiaiaiai.org
# SPDX-License-Identifier: MIT
"""Generate deterministic provider-ready raster exports from canonical SVG assets."""

from __future__ import annotations

import argparse
import hashlib
import io
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
SVG_PATH = ROOT / "assets" / "visual" / "aiaiaiai" / "compact-emblem.svg"
PNG_PATH = (
    ROOT
    / "assets"
    / "visual"
    / "aiaiaiai"
    / "exports"
    / "compact-emblem-1024.png"
)
EXPECTED_VIEWBOX = (0.0, 0.0, 64.0, 64.0)
EXPECTED_FILL = "#5BC6F4"
CANVAS = "#FFFFFF"
OUTPUT_SIZE = 1024
SUPERSAMPLE = 1


@dataclass(frozen=True)
class Line:
    x1: float
    y1: float
    x2: float
    y2: float


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_number_list(value: str) -> tuple[float, ...]:
    return tuple(float(part) for part in value.replace(",", " ").split())


def parse_svg() -> tuple[list[tuple[float, float]], list[Line], float]:
    tree = ET.parse(SVG_PATH)
    root = tree.getroot()
    namespace = {"svg": "http://www.w3.org/2000/svg"}

    viewbox = parse_number_list(root.attrib.get("viewBox", ""))
    if viewbox != EXPECTED_VIEWBOX:
        raise ValueError(f"unexpected viewBox: {viewbox!r}")

    polygon = root.find(".//svg:polygon[@id='mask-body']", namespace)
    channels = root.find(".//svg:g[@id='channels']", namespace)
    mark = root.find(".//svg:rect[@id='mark-fill']", namespace)
    if polygon is None or channels is None or mark is None:
        raise ValueError("canonical SVG is missing required controlled geometry")

    fill = mark.attrib.get("fill", "").upper()
    if fill != EXPECTED_FILL:
        raise ValueError(f"unexpected canonical fill: {fill!r}")

    raw_points = polygon.attrib.get("points", "").split()
    points: list[tuple[float, float]] = []
    for raw in raw_points:
        x, y = raw.split(",", maxsplit=1)
        points.append((float(x), float(y)))
    if len(points) < 3:
        raise ValueError("canonical silhouette must have at least three vertices")

    stroke_width = float(channels.attrib.get("stroke-width", "0"))
    if stroke_width != 3.2:
        raise ValueError(f"unexpected channel width: {stroke_width!r}")

    lines: list[Line] = []
    for element in channels.findall("svg:line", namespace):
        lines.append(
            Line(
                x1=float(element.attrib["x1"]),
                y1=float(element.attrib["y1"]),
                x2=float(element.attrib["x2"]),
                y2=float(element.attrib["y2"]),
            )
        )
    if not lines:
        raise ValueError("canonical SVG has no negative-space channels")

    return points, lines, stroke_width


def render_png_bytes() -> bytes:
    points, lines, stroke_width = parse_svg()
    scale = OUTPUT_SIZE * SUPERSAMPLE / EXPECTED_VIEWBOX[2]
    render_size = OUTPUT_SIZE * SUPERSAMPLE

    image = Image.new("RGB", (render_size, render_size), CANVAS)
    draw = ImageDraw.Draw(image)

    scaled_points = [(round(x * scale), round(y * scale)) for x, y in points]
    draw.polygon(scaled_points, fill=EXPECTED_FILL)

    width = round(stroke_width * scale)
    for line in lines:
        start = (round(line.x1 * scale), round(line.y1 * scale))
        end = (round(line.x2 * scale), round(line.y2 * scale))
        draw.line((start, end), fill=CANVAS, width=width)
        radius = width / 2
        for x, y in (start, end):
            draw.ellipse(
                (
                    round(x - radius),
                    round(y - radius),
                    round(x + radius),
                    round(y + radius),
                ),
                fill=CANVAS,
            )

    image = image.resize(
        (OUTPUT_SIZE, OUTPUT_SIZE),
        resample=Image.Resampling.LANCZOS,
    )

    output = io.BytesIO()
    image.save(
        output,
        format="PNG",
        optimize=False,
        compress_level=9,
    )
    return output.getvalue()


def check() -> int:
    expected = PNG_PATH.read_bytes()
    actual = render_png_bytes()
    if actual == expected:
        print(
            "deterministic visual export is current: "
            f"{PNG_PATH.relative_to(ROOT)} sha256={sha256_bytes(actual)}"
        )
        return 0

    print("visual export drift detected:", file=sys.stderr)
    print(f"- committed sha256: {sha256_bytes(expected)}", file=sys.stderr)
    print(f"- generated sha256: {sha256_bytes(actual)}", file=sys.stderr)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="regenerate in memory and fail if committed bytes differ",
    )
    args = parser.parse_args()

    if args.check:
        return check()

    data = render_png_bytes()
    PNG_PATH.parent.mkdir(parents=True, exist_ok=True)
    PNG_PATH.write_bytes(data)
    print(
        f"wrote {PNG_PATH.relative_to(ROOT)} "
        f"({len(data)} bytes, sha256={sha256_bytes(data)})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
