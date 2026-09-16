#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تحويل صور «مكينة الفايبر ليزر» إلى JPEG مضغوطة جاهزة للويب
داخل assets/img/svc/ — بأسماء وصفية صديقة لمحركات البحث.

    python3 tools/optimize-engraving-images.py
"""
import os
from PIL import Image

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.abspath(
    os.path.join(SITE, "..", "صور اعمال رواد الليزر", "صور مكينة الفايبر ليزر ")
)
OUT = os.path.join(SITE, "assets", "img", "svc")

MAX_DIM = 1400
QUALITY = 74

MAP = {
    # لوحات وعيّنات إمكانيات (عريضة — تصلح للمقدمات)
    "ChatGPT Image 16 سبتمبر 2026، 06_54_09 م.png": "laser-engraving-metals-range.jpg",
    "ChatGPT Image 16 سبتمبر 2026، 06_48_35 م.png": "engraving-line-detail-test.jpg",
    "ChatGPT Image 16 سبتمبر 2026، 06_56_38 م.png": "fiber-laser-capability-plate.jpg",
    "ChatGPT Image 16 سبتمبر 2026، 06_46_29 م.png": "engraving-power-test-grid.jpg",
    "ChatGPT Image 16 سبتمبر 2026، 06_42_51 م.png": "engraving-contrast-range.jpg",
    "Gemini_Generated_Image_342k8n342k8n342k.jpeg": "photo-engraving-on-metal.jpg",
    "Gemini_Generated_Image_5ubs6b5ubs6b5ubs.jpeg": "engraving-four-metals-test.jpg",
    # قطع ولوحات منقوشة
    "Gemini_Generated_Image_dqdd9tdqdd9tdqdd.jpeg": "engraved-part-number-plate.jpg",
    "Gemini_Generated_Image_jdrhuhjdrhuhjdrh.jpeg": "engraved-machine-nameplate.jpg",
    "Gemini_Generated_Image_bzd64cbzd64cbzd6.jpeg": "engraved-qr-equipment-id.jpg",
    "Gemini_Generated_Image_c9rdjwc9rdjwc9rd.jpeg": "engraved-stainless-nameplate.jpg",
    "Gemini_Generated_Image_ngpmqhngpmqhngpm.jpeg": "engraved-brass-plate.jpg",
    "Gemini_Generated_Image_c2fpq6c2fpq6c2fp.jpeg": "engraved-hand-tool.jpg",
    "Gemini_Generated_Image_bijszxbijszxbijs.jpeg": "engraved-rotor-disc.jpg",
    "Gemini_Generated_Image_bv6c37bv6c37bv6c.jpeg": "engraved-steel-test-block.jpg",
    "Gemini_Generated_Image_tt8b9ftt8b9ftt8b.jpeg": "engraved-machined-gear-housing.jpg",
    "Gemini_Generated_Image_s5gqbvs5gqbvs5gq.jpeg": "engraved-calibration-scale.jpg",
}


def main():
    os.makedirs(OUT, exist_ok=True)
    for src_name, out_name in MAP.items():
        src = os.path.join(SRC, src_name)
        if not os.path.exists(src):
            print(f"✗ مفقود: {src_name}")
            continue
        im = Image.open(src).convert("RGB")
        im.thumbnail((MAX_DIM, MAX_DIM), Image.LANCZOS)
        dst = os.path.join(OUT, out_name)
        im.save(dst, "JPEG", quality=QUALITY, optimize=True, progressive=True)
        print(f"✓ {out_name}  {im.width}×{im.height}  ({os.path.getsize(dst)/1024:.0f} KB)")


if __name__ == "__main__":
    main()
