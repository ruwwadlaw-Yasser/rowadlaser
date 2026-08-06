#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تحويل صور كتلوج رواد الليزر (PNG ضخمة) إلى JPEG مضغوطة جاهزة للويب
داخل assets/img/svc/ — مع أسماء ملفات وصفية صديقة لمحركات البحث.

يُشغَّل مرة واحدة عند إضافة صور جديدة للكتلوج:
    python3 tools/optimize-catalog-images.py
"""
import os
from PIL import Image

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.abspath(os.path.join(SITE, "..", "صور كتلوج رواد الليزر"))
OUT = os.path.join(SITE, "assets", "img", "svc")

MAX_DIM = 1400
QUALITY = 74

# اسم المصدر  ->  اسم الملف الناتج (وصفي وصديق للـ SEO)
MAP = {
    "ChatGPT Image 3 أغسطس 2026، 10_25_12 م.png": "laser-cutting-machine-wide.jpg",
    "ChatGPT Image 3 أغسطس 2026، 10_25_32 م.png": "stainless-laser-cutting-head.jpg",
    "ChatGPT Image 3 أغسطس 2026، 10_32_27 م.png": "metal-projects-showroom.jpg",
    "ChatGPT Image 3 أغسطس 2026، 10_35_11 م.png": "laser-cut-metal-parts-poster.jpg",
    "ChatGPT Image 3 أغسطس 2026، 10_44_14 م.png": "industrial-laser-engraving-wide.jpg",
    "ChatGPT Image 3 أغسطس 2026، 10_46_06 م.png": "metal-nameplate-before-after.jpg",
    "الحلول المخصصة .png": "custom-metal-solutions-range.jpg",
    "القطع الصناعية.png": "industrial-metal-parts-set.jpg",
    "النحت الصناعي الاحترافي.png": "industrial-engraving-plates.jpg",
    "تجهيزات المطاعم.png": "stainless-restaurant-kitchen.jpg",
    "رواد الليزر.png": "engraved-metal-plates-collection.jpg",
    "صور الفايبر ماركينق ( مقدمة ).png": "fiber-marking-metal-plates.jpg",
    "صور الفايبر ماركينق.png": "fiber-marking-plates-wide.jpg",
    "صور واجهات المحلات رواد الليزر.png": "metal-storefront-facade.jpg",
    "صورة ليزر يحفر.png": "laser-engraving-metal-closeup.jpg",
    "صورة ليزر يقص ستيل ( المقدمة) .png": "laser-cutting-steel-sheet.jpg",
    "صورة ليزر يقطع وبجانبه قطع معدنية ( الصورة الثانية ).png": "stainless-cutting-and-parts.jpg",
    "فايبر ماركينق حلول متكاملة.png": "fiber-marking-complete-solutions.jpg",
    "فايبر ماركينق عن قرب.png": "fiber-marking-precision-closeup.jpg",
    "قبل وبعد فايبر ماركينق.png": "dataplate-before-after-engraving.jpg",
    "صور عامة/ChatGPT Image 4 أغسطس 2026، 12_37_06 ص.png": "stainless-steel-sheets-rack.jpg",
    "صور عامة/ChatGPT Image 4 أغسطس 2026، 12_39_32 ص.png": "finished-metal-parts-store.jpg",
    "صور عامة/ChatGPT Image 4 أغسطس 2026، 12_41_13 ص.png": "metal-fabrication-workshop.jpg",
    "صور عامة/ChatGPT Image 4 أغسطس 2026، 12_44_49 ص.png": "metal-material-samples.jpg",
    "صور عامة/ChatGPT Image 4 أغسطس 2026، 12_47_51 ص.png": "brushed-stainless-steel-sheet.jpg",
}
# ملاحظة: 12_38_26 و 12_43_51 مستخدمتان أصلاً في assets/img/lp (parts-shelf / metals-range)


def main():
    os.makedirs(OUT, exist_ok=True)
    total = 0
    for src_name, out_name in MAP.items():
        src = os.path.join(SRC, src_name)
        if not os.path.exists(src):
            print("!! مفقود:", src_name)
            continue
        im = Image.open(src).convert("RGB")
        im.thumbnail((MAX_DIM, MAX_DIM), Image.LANCZOS)
        dst = os.path.join(OUT, out_name)
        im.save(dst, "JPEG", quality=QUALITY, optimize=True, progressive=True)
        kb = os.path.getsize(dst) / 1024
        total += kb
        print(f"{out_name:44s} {im.width}x{im.height}  {kb:6.0f} KB")
    print(f"\nالمجموع: {total/1024:.2f} MB  في  {OUT}")


if __name__ == "__main__":
    main()
