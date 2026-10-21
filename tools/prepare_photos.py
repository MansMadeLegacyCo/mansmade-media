#!/usr/bin/env python3
"""Prepare product photos for publication.

For each input photo this script:
  * applies the camera's orientation so the image displays upright,
  * converts it to sRGB JPEG,
  * resizes it so the longest side is at most 2400 px,
  * writes it WITHOUT any metadata (EXIF, GPS location, camera serials).

Usage:
  python3 tools/prepare_photos.py <product-handle> <photo> [<photo> ...]

Output:
  products/<product-handle>/<product-handle>-01.jpg, -02.jpg, ...
  Numbering continues after any photos already in that folder.
"""
import re
import sys
from pathlib import Path

from PIL import Image, ImageOps

try:
    import pillow_heif  # iPhone HEIC support

    pillow_heif.register_heif_opener()
except ImportError:
    pass

MAX_EDGE = 2400
QUALITY = 85
REPO = Path(__file__).resolve().parent.parent


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    handle = sys.argv[1]
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", handle):
        print("Handle must be lowercase words joined by hyphens, e.g. walnut-valet-tray")
        return 2

    out_dir = REPO / "products" / handle
    out_dir.mkdir(parents=True, exist_ok=True)
    existing = sorted(out_dir.glob(f"{handle}-*.jpg"))
    index = len(existing)

    for src in sys.argv[2:]:
        index += 1
        with Image.open(src) as img:
            img = ImageOps.exif_transpose(img)
            if img.mode not in ("RGB", "L"):
                background = Image.new("RGB", img.size, (255, 255, 255))
                if "A" in img.getbands():
                    background.paste(img, mask=img.getchannel("A"))
                else:
                    background.paste(img.convert("RGB"))
                img = background
            img = img.convert("RGB")
            img.thumbnail((MAX_EDGE, MAX_EDGE), Image.LANCZOS)
            # Rebuild from raw pixels so no metadata can carry over.
            clean = Image.frombytes("RGB", img.size, img.tobytes())
            dest = out_dir / f"{handle}-{index:02d}.jpg"
            clean.save(dest, "JPEG", quality=QUALITY, optimize=True, progressive=True)
            print(f"{src} -> {dest.relative_to(REPO)} ({clean.size[0]}x{clean.size[1]})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
