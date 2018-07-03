#!/usr/bin/env python3
from PIL import Image
import glob, os

for f in glob.glob("*.jpg"):
    file, extension = os.path.splitext(f)
    im = Image.open(f).convert("RGB")
    im.save(file + ".webp", lossless=True, exif=False)
