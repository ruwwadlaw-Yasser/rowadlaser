#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
رسومات توضيحية لصفحات اللوحات والتاقات المحفورة — رواد الليزر
================================================================
كل مشهد = SVG يُرسم برمجياً ثم يُحوَّل إلى JPG عبر Chrome (headless)
ويُحفظ في assets/img/svc/ill-<name>.jpg بمقاس 1400×1050.

التشغيل:
    python3 tools/illustrations/make.py            # كل المشاهد
    python3 tools/illustrations/make.py valve ...  # مشاهد محددة
"""
import os
import subprocess
import sys
import tempfile

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(SITE, "assets", "img", "svc")
FONTS = os.path.join(SITE, "assets", "fonts")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
W, H = 1400, 1050

AR = "Thmanyah"
EN = "'Helvetica Neue', Arial, sans-serif"
MONO = "'DIN Alternate', 'Arial Narrow', 'Helvetica Neue', Arial, sans-serif"

# ============================================================
#  الأساسيات: خلفية، تدرّجات معدنية، ظلال
# ============================================================

DEFS = """
<defs>
  <radialGradient id="bg" cx="50%" cy="38%" r="80%">
    <stop offset="0" stop-color="#f7f8fa"/><stop offset=".6" stop-color="#e6e9ee"/><stop offset="1" stop-color="#cfd4dc"/>
  </radialGradient>
  <pattern id="grid" width="56" height="56" patternUnits="userSpaceOnUse">
    <path d="M56 0H0V56" fill="none" stroke="#0d0f12" stroke-opacity=".045" stroke-width="1"/>
  </pattern>
  <filter id="sh" x="-30%" y="-30%" width="160%" height="170%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="14"/><feOffset dy="18" result="b"/>
    <feComponentTransfer><feFuncA type="linear" slope=".28"/></feComponentTransfer>
    <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="shs" x="-30%" y="-30%" width="160%" height="170%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="6"/><feOffset dy="7"/>
    <feComponentTransfer><feFuncA type="linear" slope=".3"/></feComponentTransfer>
    <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="brush" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.002 0.85" numOctaves="2" seed="4" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .55 0" result="w"/>
    <feComposite in="w" in2="SourceGraphic" operator="in"/>
  </filter>
  <filter id="frost"><feTurbulence type="fractalNoise" baseFrequency="1.4" numOctaves="1" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .9 0" result="w"/>
    <feComposite in="w" in2="SourceGraphic" operator="in"/></filter>
  <linearGradient id="steel" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#eef0f3"/><stop offset=".35" stop-color="#c9ced6"/><stop offset=".55" stop-color="#e9ecf0"/><stop offset="1" stop-color="#a9b0ba"/>
  </linearGradient>
  <linearGradient id="brass" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#f3dc93"/><stop offset=".4" stop-color="#c99a3b"/><stop offset=".6" stop-color="#e8c66f"/><stop offset="1" stop-color="#9c7425"/>
  </linearGradient>
  <linearGradient id="copper" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#f0b08c"/><stop offset=".45" stop-color="#b8693f"/><stop offset=".6" stop-color="#d98a5f"/><stop offset="1" stop-color="#874424"/>
  </linearGradient>
  <linearGradient id="alu" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#f4f6f8"/><stop offset=".5" stop-color="#d7dce2"/><stop offset="1" stop-color="#b9c0c9"/>
  </linearGradient>
  <linearGradient id="gloss" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#fff" stop-opacity=".38"/><stop offset=".45" stop-color="#fff" stop-opacity=".04"/><stop offset="1" stop-color="#000" stop-opacity=".1"/>
  </linearGradient>
  <linearGradient id="acrylic" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#ffffff" stop-opacity=".75"/><stop offset=".5" stop-color="#dfe9f2" stop-opacity=".35"/><stop offset="1" stop-color="#ffffff" stop-opacity=".6"/>
  </linearGradient>
  <linearGradient id="cable" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#3a3f47"/><stop offset=".35" stop-color="#6b727d"/><stop offset=".6" stop-color="#2a2e34"/><stop offset="1" stop-color="#15171a"/>
  </linearGradient>
</defs>
"""

FILLS = {
    "steel": "url(#steel)",
    "brass": "url(#brass)",
    "copper": "url(#copper)",
    "alu": "url(#alu)",
}


def T(x, y, s, size=28, fill="#15181d", weight=700, anchor="middle", font=EN, extra=""):
    rtl = ' direction="rtl"' if font == AR else ""
    if font == AR and anchor in ("start", "end"):
        # في RTL تنعكس start/end — نُبقي المعنى البصري: start = يسار، end = يمين
        anchor = "end" if anchor == "start" else "start"
    return (
        f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" '
        f'fill="{fill}" text-anchor="{anchor}"{rtl} {extra}>{s}</text>'
    )


def hole(x, y, r=9, ring="#8b929c"):
    return (
        f'<circle cx="{x}" cy="{y}" r="{r}" fill="#d9dde3" stroke="{ring}" stroke-width="2"/>'
        f'<circle cx="{x}" cy="{y}" r="{r*0.45:.1f}" fill="#9aa1ab"/>'
    )


def through(x, y, r=11):
    """فتحة نافذة يظهر منها الخلفية"""
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#dfe3e8" stroke="#0d0f12" stroke-opacity=".25" stroke-width="2"/>'


def plate(x, y, w, h, fill="steel", r=14, rot=0, body="", brushed=True, stroke="#0d0f12", shadow="sh", gloss=True):
    f = FILLS.get(fill, fill)
    br = (
        f'<rect width="{w}" height="{h}" rx="{r}" fill="#fff" filter="url(#brush)" opacity=".55"/>'
        if brushed
        else ""
    )
    gl = f'<rect width="{w}" height="{h}" rx="{r}" fill="url(#gloss)"/>' if gloss else ""
    return (
        f'<g transform="translate({x} {y}) rotate({rot} {w/2} {h/2})" filter="url(#{shadow})">'
        f'<rect width="{w}" height="{h}" rx="{r}" fill="{f}"/>{br}{gl}'
        f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{r}" fill="none" stroke="{stroke}" stroke-opacity=".22" stroke-width="2"/>'
        f"{body}</g>"
    )


def group(x, y, rot=0, body="", shadow="sh", cx=0, cy=0):
    return f'<g transform="translate({x} {y}) rotate({rot} {cx} {cy})" filter="url(#{shadow})">{body}</g>'


def qr(x, y, s, fill="#15181d", seed=7):
    import random

    rnd = random.Random(seed)
    n = 21
    c = s / n
    out = []

    def finder(px, py):
        return (
            f'<rect x="{x+px*c}" y="{y+py*c}" width="{7*c}" height="{7*c}" fill="{fill}"/>'
            f'<rect x="{x+(px+1)*c}" y="{y+(py+1)*c}" width="{5*c}" height="{5*c}" fill="#fff" fill-opacity=".001" stroke="none"/>'
        )

    for i in range(n):
        for k in range(n):
            infinder = (i < 8 and k < 8) or (i < 8 and k > n - 9) or (i > n - 9 and k < 8)
            if infinder:
                continue
            if rnd.random() < 0.5:
                out.append(f'<rect x="{x+i*c:.1f}" y="{y+k*c:.1f}" width="{c:.1f}" height="{c:.1f}" fill="{fill}"/>')
    for px, py in ((0, 0), (n - 7, 0), (0, n - 7)):
        X, Y = x + px * c, y + py * c
        out.append(
            f'<rect x="{X:.1f}" y="{Y:.1f}" width="{7*c:.1f}" height="{7*c:.1f}" fill="none" stroke="{fill}" stroke-width="{c:.1f}" transform="translate({c/2:.1f} {c/2:.1f}) scale(1)" />'
        )
        out.append(f'<rect x="{X+2*c:.1f}" y="{Y+2*c:.1f}" width="{3*c:.1f}" height="{3*c:.1f}" fill="{fill}"/>')
    return "".join(out)


def barcode(x, y, w, h, fill="#15181d", seed=3):
    import random

    rnd = random.Random(seed)
    out, cx = [], x
    while cx < x + w:
        bw = rnd.choice((2, 2, 3, 4, 6))
        if rnd.random() < 0.55:
            out.append(f'<rect x="{cx}" y="{y}" width="{bw}" height="{h}" fill="{fill}"/>')
        cx += bw + rnd.choice((2, 3, 4))
    return "".join(out)


# أيقونات بسيطة للّوحات
def ico_bolt(cx, cy, s, fill):
    return f'<path transform="translate({cx-s/2} {cy-s/2}) scale({s/24})" d="M13 2 4 14h7l-1 8 9-12h-7z" fill="{fill}"/>'


def ico_exit(cx, cy, s, fill):
    k = s / 24
    return (
        f'<g transform="translate({cx-s/2} {cy-s/2}) scale({k})" fill="{fill}">'
        '<circle cx="14" cy="3.5" r="2.3"/><path d="M9 8l4-1.5 3 3 3 1-.6 1.8-3.8-1.2-1.4-1.3-1 4 3 3V22h-2v-4.5L11 15l-1 3-4 3-1.2-1.6L8 17l1.5-6-1.6.7V15H6v-4.5z"/></g>'
    )


def ico_person(cx, cy, s, fill):
    k = s / 24
    return (
        f'<g transform="translate({cx-s/2} {cy-s/2}) scale({k})" fill="{fill}">'
        '<circle cx="12" cy="4" r="2.6"/><path d="M8 8h8l1 7h-2.2l-.8 8h-4l-.8-8H7z"/></g>'
    )


def ico_lock(cx, cy, s, fill):
    k = s / 24
    return (
        f'<g transform="translate({cx-s/2} {cy-s/2}) scale({k})"><path d="M7 10V7a5 5 0 0 1 10 0v3" fill="none" stroke="{fill}" stroke-width="2.4"/>'
        f'<rect x="4" y="10" width="16" height="12" rx="2" fill="{fill}"/></g>'
    )


def ico_helmet(cx, cy, s, fill):
    k = s / 24
    return (
        f'<g transform="translate({cx-s/2} {cy-s/2}) scale({k})" fill="{fill}">'
        '<path d="M3 17a9 9 0 0 1 18 0z"/><rect x="2" y="17" width="20" height="2.6" rx="1.3"/><rect x="10.6" y="6" width="2.8" height="7" rx="1"/></g>'
    )


def ico_fire(cx, cy, s, fill):
    k = s / 24
    return (
        f'<path transform="translate({cx-s/2} {cy-s/2}) scale({k})" d="M12 2c1 4 6 6 6 12a6 6 0 0 1-12 0c0-3 2-5 3-6 0 2 1 3 2 3 0-4-1-6 1-9z" fill="{fill}"/>'
    )


def ico_cig(cx, cy, s, fill):
    k = s / 24
    return (
        f'<g transform="translate({cx-s/2} {cy-s/2}) scale({k})" fill="{fill}">'
        '<rect x="2" y="14" width="16" height="4" rx="1"/><rect x="19" y="14" width="3" height="4" rx="1"/>'
        '<path d="M17 4c2 2-1 3 1 6M20 3c2 2-1 3 1 6" fill="none" stroke="{fill}" stroke-width="1.4"/></g>'
    ).replace("{fill}", fill)


def ico_arrow(cx, cy, s, fill, rot=0):
    k = s / 24
    return (
        f'<path transform="translate({cx-s/2} {cy-s/2}) scale({k}) rotate({rot} 12 12)" d="M3 10.5h12V5l7 7-7 7v-5.5H3z" fill="{fill}"/>'
    )


def ico_drop(cx, cy, s, fill):
    k = s / 24
    return f'<path transform="translate({cx-s/2} {cy-s/2}) scale({k})" d="M12 2s7 8 7 13a7 7 0 0 1-14 0c0-5 7-13 7-13z" fill="{fill}"/>'


def ico_wc(cx, cy, s, fill):
    return ico_person(cx - s * 0.42, cy, s, fill) + (
        f'<rect x="{cx-1.5}" y="{cy-s/2}" width="3" height="{s}" fill="{fill}"/>'
    ) + ico_person(cx + s * 0.42, cy, s, fill)


# ============================================================
#  المشاهد
# ============================================================


def scene_aluminum():
    o = []
    cols = [("#15181d", "#e9edf2"), ("#1f4fbf", "#eaf1ff"), ("#b4232a", "#fff1f1"), ("#2e7d4f", "#eefaf3")]
    # لوحة كبيرة مؤكسدة سوداء
    body = (
        T(300, 92, "RUWWAD LASER", 34, "#eef1f5", 800)
        + T(300, 132, "ANODIZED ALUMINIUM", 20, "#aeb6c1", 600, extra='letter-spacing="4"')
        + '<line x1="60" y1="160" x2="540" y2="160" stroke="#cfd6df" stroke-opacity=".5" stroke-width="2"/>'
        + "".join(
            T(70, 205 + i * 46, k, 22, "#c6cdd6", 600, "start") + T(530, 205 + i * 46, v, 22, "#f2f5f8", 700, "end", MONO)
            for i, (k, v) in enumerate((("MODEL", "AL-6061-T6"), ("SERIAL NO.", "RL-2026-0418"), ("VOLTAGE", "380V / 3PH"), ("WEIGHT", "42 KG")))
        )
        + qr(452, 382, 86, "#e9edf2", 11)
        + T(70, 452, "MADE IN KSA", 18, "#aeb6c1", 600, "start", extra='letter-spacing="3"')
        + hole(28, 28, 8) + hole(572, 28, 8) + hole(28, 462, 8) + hole(572, 462, 8)
    )
    o.append(plate(150, 170, 600, 490, "#24282f", 18, -4, body, brushed=True))
    # لوحات ملوّنة صغيرة
    labels = [("PUMP P-101", "STARTER"), ("FIRE PANEL", "ZONE 03"), ("MAIN ISOLATOR", "415V"), ("COOLING", "LINE B")]
    pos = [(840, 150, 6), (900, 420, -5), (800, 690, 3), (240, 730, -3)]
    for (bg, fg), (a, b), (x, y, r) in zip(cols, labels, pos):
        body = T(200, 78, a, 34, fg, 800) + T(200, 122, b, 24, fg, 600, extra='letter-spacing="3" opacity=".85"') + hole(24, 24, 7) + hole(376, 24, 7)
        o.append(plate(x, y, 400, 160, bg, 14, r, body))
    # قرص ألمنيوم خام بحفر أسود
    body = (
        '<circle r="92" fill="url(#alu)"/><circle r="92" fill="#fff" filter="url(#brush)" opacity=".5"/>'
        '<circle r="92" fill="none" stroke="#0d0f12" stroke-opacity=".2" stroke-width="2"/>'
        + T(0, -6, "AL-5052", 30, "#1a1d22", 800, font=MONO)
        + T(0, 30, "LOT 2611", 20, "#3d434c", 600, extra='letter-spacing="2"')
        + '<circle cy="-66" r="9" fill="#dfe3e8" stroke="#8b929c" stroke-width="2"/>'
    )
    o.append(group(1210, 860, 0, body))
    return "".join(o)


def scene_brass():
    o = []
    body = (
        '<rect x="22" y="22" width="636" height="376" rx="10" fill="none" stroke="#5a3e0e" stroke-opacity=".55" stroke-width="3"/>'
        '<rect x="34" y="34" width="612" height="352" rx="6" fill="none" stroke="#5a3e0e" stroke-opacity=".35" stroke-width="1.5"/>'
        + T(340, 140, "شكر وتقدير", 64, "#3b2806", 900, font=AR)
        + T(340, 214, "تقديراً لجهودكم المتميزة في إنجاز المشروع", 30, "#4a3410", 500, font=AR)
        + '<line x1="200" y1="252" x2="480" y2="252" stroke="#4a3410" stroke-opacity=".6" stroke-width="2"/>'
        + T(340, 304, "م. خالد العتيبي", 36, "#3b2806", 800, font=AR)
        + T(340, 350, "جدة · 2026", 24, "#4a3410", 500, font=AR)
        + hole(56, 56, 8, "#7d5a1c") + hole(624, 56, 8, "#7d5a1c") + hole(56, 364, 8, "#7d5a1c") + hole(624, 364, 8, "#7d5a1c")
    )
    o.append(plate(120, 200, 680, 420, "brass", 16, -3, body))
    body = T(230, 70, "VILLA 27", 46, "#3b2806", 900) + T(230, 118, "فيلا آل سليمان", 30, "#4a3410", 700, font=AR) + hole(26, 80, 7, "#7d5a1c") + hole(434, 80, 7, "#7d5a1c")
    o.append(plate(870, 150, 460, 160, "brass", 12, 5, body))
    body = (
        '<circle r="96" fill="url(#brass)"/><circle r="96" fill="#fff" filter="url(#brush)" opacity=".45"/>'
        '<circle r="80" fill="none" stroke="#5a3e0e" stroke-opacity=".5" stroke-width="2"/>'
        + T(0, -8, "V-204", 36, "#3b2806", 900, font=MONO) + T(0, 30, "STEAM", 20, "#4a3410", 700, extra='letter-spacing="3"')
        + '<circle cy="-66" r="9" fill="#dfe3e8" stroke="#7d5a1c" stroke-width="2"/>'
    )
    o.append(group(1000, 520, 0, body))
    body = T(180, 62, "SERIAL", 18, "#4a3410", 700, extra='letter-spacing="4"') + T(180, 104, "BR-0091-26", 34, "#3b2806", 900, font=MONO)
    o.append(plate(880, 700, 360, 140, "copper", 12, -4, body))
    body = T(150, 54, "OFFICE 204", 30, "#3b2806", 900) + T(150, 92, "الإدارة المالية", 24, "#4a3410", 700, font=AR)
    o.append(plate(250, 720, 300, 120, "brass", 10, 4, body))
    return "".join(o)


def lam(x, y, w, h, top, core, rot=0, body="", r=10):
    """لوحة بلاستيك طبقات (ترافوليت/ABS): الطبقة العلوية ملوّنة والحفر يكشف لون اللب"""
    edge = f'<rect x="0" y="6" width="{w}" height="{h}" rx="{r}" fill="{core}"/>'
    face = f'<rect width="{w}" height="{h}" rx="{r}" fill="{top}"/><rect width="{w}" height="{h}" rx="{r}" fill="url(#gloss)"/>'
    return group(x, y, rot, edge + face + body, "sh", w / 2, h / 2)


def scene_traffolyte():
    o = []
    data = [
        (90, 150, 520, 170, "#c8202a", "#ffffff", -3, ("DANGER", "415 VOLTS")),
        (690, 120, 560, 170, "#111316", "#ffffff", 4, ("MAIN SWITCH", "DB-01  ·  لوحة التوزيع الرئيسية")),
        (130, 420, 470, 160, "#f3c316", "#111316", 2, ("CAUTION", "HOT SURFACE")),
        (700, 400, 520, 160, "#1d4fbf", "#ffffff", -3, ("PUMP P-02", "CHILLED WATER")),
        (180, 690, 440, 150, "#ffffff", "#111316", -2, ("MCC-3", "MOTOR CONTROL")),
        (730, 680, 480, 160, "#1f8a4c", "#ffffff", 3, ("EMERGENCY STOP", "زر الإيقاف الطارئ")),
    ]
    for x, y, w, h, top, core, rot, (a, b) in data:
        font_b = AR if any("؀" <= ch <= "ۿ" for ch in b) else EN
        body = (
            T(w / 2, h * 0.47, a, 44, core, 800)
            + T(w / 2, h * 0.8, b, 24, core, 600, font=font_b, extra="" if font_b == AR else 'letter-spacing="3"')
            + through(26, h / 2, 9) + through(w - 26, h / 2, 9)
        )
        o.append(lam(x, y, w, h, top, core if top != "#ffffff" else "#111316", rot, body))
    return "".join(o)


def scene_pvc():
    o = []
    body = (
        f'<rect x="0" y="0" width="300" height="300" rx="20" fill="#1f8a4c"/>'
        + ico_exit(150, 120, 150, "#fff")
        + T(150, 262, "EXIT  مخرج", 40, "#fff", 800, font=EN)
    )
    o.append(group(110, 170, -4, f'<rect y="8" width="300" height="300" rx="20" fill="#0f5a30"/>' + body))
    body = (
        '<rect y="8" width="520" height="200" rx="18" fill="#0d0f12"/>'
        '<rect width="520" height="200" rx="18" fill="#e9ecf0"/><rect width="520" height="200" rx="18" fill="url(#gloss)"/>'
        + T(260, 92, "غرفة الاجتماعات", 52, "#0d0f12", 900, font=AR)
        + T(260, 150, "MEETING ROOM  ·  2F", 28, "#3b414a", 700, extra='letter-spacing="3"')
    )
    o.append(group(500, 140, 3, body))
    body = (
        '<rect y="8" width="300" height="300" rx="20" fill="#0d2a7a"/><rect width="300" height="300" rx="20" fill="#1d4fbf"/>'
        '<circle cx="150" cy="130" r="92" fill="#fff"/>' + ico_helmet(150, 128, 120, "#1d4fbf")
        + T(150, 266, "ارتدِ الخوذة", 36, "#fff", 800, font=AR)
    )
    o.append(group(1060, 400, 5, body))
    body = (
        '<rect y="8" width="460" height="180" rx="16" fill="#e9ecf0"/><rect width="460" height="180" rx="16" fill="#111316"/>'
        + ico_wc(110, 90, 96, "#e9ecf0")
        + T(320, 82, "دورات المياه", 40, "#e9ecf0", 800, font=AR) + T(320, 130, "TOILETS", 26, "#c9ced6", 700, extra='letter-spacing="4"')
    )
    o.append(group(480, 470, -2, body))
    body = (
        '<rect y="8" width="380" height="150" rx="16" fill="#8f141b"/><rect width="380" height="150" rx="16" fill="#c8202a"/>'
        + ico_fire(70, 75, 80, "#fff") + T(230, 70, "FIRE HOSE", 36, "#fff", 800) + T(230, 114, "خرطوم الحريق", 28, "#fff", 700, font=AR)
    )
    o.append(group(150, 640, 3, body))
    body = (
        '<rect y="8" width="420" height="160" rx="16" fill="#0d0f12"/><rect width="420" height="160" rx="16" fill="#f3c316"/>'
        + T(210, 74, "RECEPTION", 44, "#111316", 900) + T(210, 124, "الاستقبال  →", 32, "#111316", 800, font=AR)
    )
    o.append(group(600, 760, -3, body))
    return "".join(o)


def scene_acrylic():
    o = []

    def acr(x, y, w, h, rot, inner, r=14):
        body = (
            f'<rect x="10" y="12" width="{w}" height="{h}" rx="{r}" fill="#0d0f12" opacity=".08"/>'
            f'<rect width="{w}" height="{h}" rx="{r}" fill="#ffffff" fill-opacity=".1" stroke="#cfe0ee" stroke-opacity=".9" stroke-width="3"/>'
            f'<rect x="6" y="6" width="{w-12}" height="{h-12}" rx="{r-4}" fill="none" stroke="#fff" stroke-opacity=".9" stroke-width="2"/>'
            f'<path d="M{w*0.08} 10 L{w*0.3} 10 L{w*0.12} {h-10} L{w*-0.1+20} {h-10}z" fill="#fff" opacity=".1"/>'
            + inner
        )
        return f'<g transform="translate({x} {y}) rotate({rot} {w/2} {h/2})">{body}</g>'

    def standoff(cx, cy):
        return (
            f'<circle cx="{cx}" cy="{cy}" r="18" fill="url(#steel)" stroke="#6b727d" stroke-width="2"/>'
            f'<circle cx="{cx}" cy="{cy}" r="9" fill="#c9ced6" stroke="#8b929c" stroke-width="1.5"/>'
        )

    o.append('<rect width="1400" height="1050" fill="#2b3038"/><rect width="1400" height="1050" fill="url(#grid)" opacity=".6"/>')
    frost = 'fill="#ffffff" fill-opacity=".92" stroke="#ffffff" stroke-width="1"'
    inner = (
        f'<text x="380" y="190" font-family="{AR}" font-size="96" font-weight="900" text-anchor="middle" direction="rtl" {frost}>رواد الليزر</text>'
        f'<text x="380" y="262" font-family="{EN}" font-size="34" font-weight="700" text-anchor="middle" letter-spacing="10" {frost}>RUWWAD LASER</text>'
        f'<line x1="200" y1="300" x2="560" y2="300" stroke="#fff" stroke-opacity=".7" stroke-width="2"/>'
        f'<text x="380" y="350" font-family="{AR}" font-size="30" font-weight="700" text-anchor="middle" direction="rtl" {frost}>الطابق الثالث · مكتب 305</text>'
        + standoff(46, 46) + standoff(714, 46) + standoff(46, 384) + standoff(714, 384)
    )
    o.append(acr(110, 160, 760, 430, -2, inner))
    # درع أكريليك
    shield_d = "M0 40 Q0 0 40 0 H260 Q300 0 300 40 V300 Q300 380 150 440 Q0 380 0 300z"
    inner2 = (
        f'<text x="150" y="150" font-family="{AR}" font-size="44" font-weight="900" text-anchor="middle" direction="rtl" {frost}>درع التميّز</text>'
        f'<text x="150" y="210" font-family="{AR}" font-size="26" font-weight="700" text-anchor="middle" direction="rtl" {frost}>الموظف المثالي</text>'
        f'<text x="150" y="262" font-family="{AR}" font-size="30" font-weight="800" text-anchor="middle" direction="rtl" {frost}>سارة الحربي</text>'
        f'<text x="150" y="320" font-family="{EN}" font-size="24" font-weight="700" text-anchor="middle" {frost}>2026</text>'
    )
    o.append(
        f'<g transform="translate(980 200) rotate(4 150 220)">'
        f'<path d="{shield_d}" transform="translate(10 12)" fill="#0d0f12" opacity=".1"/>'
        f'<path d="{shield_d}" fill="#ffffff" fill-opacity=".1" stroke="#cfe0ee" stroke-width="3"/>'
        f'<path d="M30 30 L110 30 L40 330 L20 300z" fill="#fff" opacity=".12"/>{inner2}'
        f'<rect x="40" y="440" width="220" height="70" rx="8" fill="#20242b"/><rect x="40" y="440" width="220" height="16" rx="6" fill="#3a3f47"/></g>'
    )
    # لوحة صغيرة
    inner3 = (
        f'<text x="230" y="98" font-family="{AR}" font-size="46" font-weight="900" text-anchor="middle" direction="rtl" {frost}>العيادة 3</text>'
        f'<text x="230" y="150" font-family="{EN}" font-size="26" font-weight="700" text-anchor="middle" letter-spacing="5" {frost}>CLINIC 3</text>'
        + standoff(36, 36) + standoff(424, 36)
    )
    o.append(acr(260, 700, 460, 190, 3, inner3))
    return "".join(o)


def scene_diamond():
    o = []
    rows = (
        ("MANUFACTURER", "RUWWAD LASER"),
        ("TYPE", "PRESSURE VESSEL"),
        ("SERIAL NO.", "PV-26-00731"),
        ("DESIGN PRESSURE", "16 BAR @ 120°C"),
        ("TEST PRESSURE", "24 BAR"),
        ("CAPACITY", "1500 L"),
        ("YEAR", "2026"),
    )
    line = 'stroke="#2a2f36" stroke-width="1.6" stroke-opacity=".75"'
    body = (
        T(470, 82, "NAMEPLATE  ·  لوحة البيانات", 34, "#1d2127", 600, font=EN, extra='letter-spacing="2" fill-opacity=".85"')
        + f'<line x1="50" y1="110" x2="890" y2="110" {line}/>'
        + "".join(
            f'<line x1="50" y1="{150+i*58}" x2="890" y2="{150+i*58}" stroke="#2a2f36" stroke-width="1" stroke-opacity=".35"/>'
            + T(70, 138 + i * 58, k, 22, "#2a2f36", 500, "start", extra='letter-spacing="2"')
            + T(870, 138 + i * 58, v, 26, "#1d2127", 600, "end", MONO)
            for i, (k, v) in enumerate(rows)
        )
        + f'<line x1="450" y1="110" x2="450" y2="556" {line} stroke-opacity=".35"/>'
        + T(70, 600, "CE  ·  ISO 9001", 24, "#2a2f36", 600, "start", extra='letter-spacing="3"')
        + qr(790, 560, 90, "#2a2f36", 21)
        + hole(26, 26, 9) + hole(914, 26, 9) + hole(26, 644, 9) + hole(914, 644, 9)
    )
    o.append(plate(230, 170, 940, 670, "steel", 12, -2, body))
    # عدسة تكبير توضح الخط المخدوش
    zoom = (
        '<circle r="150" fill="#eef0f3"/><circle r="150" fill="#fff" filter="url(#brush)" opacity=".6"/>'
        '<g stroke="#2a2f36" stroke-width="5" stroke-linecap="round" fill="none" opacity=".85">'
        '<path d="M-95 -50 V40 M-95 -50 H-60 Q-35 -50 -35 -28 Q-35 -6 -60 -6 H-95"/>'
        '<path d="M-15 -50 L15 40 L45 -50"/><path d="M60 -6 H95"/></g>'
        '<g stroke="#2a2f36" stroke-width="1.2" opacity=".5">' + "".join(f'<line x1="-120" y1="{y}" x2="120" y2="{y}"/>' for y in range(-90, 100, 9)) + '</g>'
        '<circle r="150" fill="none" stroke="#20242b" stroke-width="18"/>'
        '<rect x="96" y="96" width="34" height="150" rx="14" fill="#20242b" transform="rotate(-45 113 171)"/>'
    )
    o.append(group(1225, 860, 0, zoom))
    return "".join(o)


def scene_signage():
    o = []
    body = T(200, 128, "101", 110, "#15181d", 900) + T(200, 196, "مكتب المدير", 34, "#2a2f36", 800, font=AR) + T(200, 238, "MANAGER", 24, "#3d434c", 700, extra='letter-spacing="5"')
    o.append(plate(110, 140, 400, 290, "steel", 18, -3, body))
    body = (
        '<rect width="560" height="200" rx="16" fill="#111316"/>'
        + T(280, 96, "الاستقبال", 60, "#f2f5f8", 900, font=AR) + T(280, 152, "RECEPTION", 30, "#c6cdd6", 700, extra='letter-spacing="8"')
        + '<rect x="0" y="186" width="560" height="14" rx="6" fill="#2457e5"/>'
    )
    o.append(group(600, 130, 3, body))
    body = (
        '<rect width="380" height="200" rx="16" fill="url(#brass)"/><rect width="380" height="200" rx="16" fill="#fff" filter="url(#brush)" opacity=".4"/>'
        + ico_wc(190, 90, 110, "#3b2806") + T(190, 178, "WC  ·  دورات المياه", 26, "#3b2806", 800, font=EN)
    )
    o.append(group(990, 420, -4, body))
    body = (
        '<rect width="620" height="150" rx="14" fill="#1d4fbf"/><rect width="620" height="150" rx="14" fill="url(#gloss)"/>'
        + T(370, 70, "قاعة التدريب", 48, "#fff", 900, font=AR) + T(370, 116, "TRAINING HALL", 26, "#dfe8ff", 700, extra='letter-spacing="4"')
        + ico_arrow(90, 75, 90, "#fff", 180)
    )
    o.append(group(160, 520, 2, body))
    body = T(260, 92, "صالة الانتظار", 50, "#15181d", 900, font=AR) + T(260, 146, "WAITING AREA", 26, "#3d434c", 700, extra='letter-spacing="5"')
    o.append(plate(560, 760, 520, 190, "alu", 14, -2, body))
    body = '<rect width="200" height="200" rx="100" fill="#111316"/>' + T(100, 128, "2F", 80, "#f2f5f8", 900)
    o.append(group(230, 780, 0, body))
    return "".join(o)


def scene_route():
    o = []
    # أرضية خرسانية
    o.append('<rect x="0" y="0" width="1400" height="1050" fill="#d7d9dc"/>')
    o.append('<rect x="0" y="0" width="1400" height="1050" fill="#fff" filter="url(#frost)" opacity=".18"/>')
    o.append('<path d="M0 560 C 300 520, 700 600, 1400 540" stroke="#bfc3c8" stroke-width="160" fill="none" opacity=".6"/>')
    markers = [
        (230, 320, "brass", "WATER", "خط مياه", ico_drop, 0),
        (560, 300, "steel", "GAS", "خط غاز", ico_fire, 90),
        (900, 330, "brass", "HV CABLE", "كيبل جهد عالٍ", ico_bolt, 180),
        (1220, 300, "steel", "TELECOM", "اتصالات", ico_bolt, 270),
    ]
    for x, y, f, en, ar, icf, arot in markers:
        body = (
            f'<circle r="118" fill="{FILLS[f]}"/><circle r="118" fill="#fff" filter="url(#brush)" opacity=".45"/>'
            '<circle r="100" fill="none" stroke="#2a2f36" stroke-opacity=".5" stroke-width="3"/>'
            + icf(0, -42, 52, "#2a2f36")
            + T(0, 22, en, 30 if len(en) < 6 else 24, "#1d2127", 900)
            + T(0, 60, ar, 24, "#2a2f36", 700, font=AR)
            + ico_arrow(0, 90, 30, "#2a2f36", arot)
        )
        o.append(group(x, y, 0, body))
    for i, (x, y, f, en, ar, rot) in enumerate(
        ((180, 640, "steel", "ROUTE A  →", "المسار أ", -3), (560, 690, "brass", "TO PARKING", "إلى المواقف", 2), (960, 650, "steel", "FIRE MAIN", "خط الحريق", -2))
    ):
        body = T(170, 64, en, 34, "#1d2127", 900) + T(170, 108, ar, 28, "#2a2f36", 700, font=AR) + hole(22, 70, 7) + hole(318, 70, 7)
        o.append(plate(x, y, 340, 140, f, 12, rot, body))
    return "".join(o)


def tri(cx, cy, s, fill, stroke):
    h = s * 0.866
    return f'<path d="M{cx} {cy-h*0.6} L{cx+s/2} {cy+h*0.4} L{cx-s/2} {cy+h*0.4}z" fill="{fill}" stroke="{stroke}" stroke-width="{s*0.07}" stroke-linejoin="round"/>'


def scene_safety():
    o = []

    def sign(x, y, w, h, rot, inner, bg="#ffffff"):
        body = f'<rect width="{w}" height="{h}" rx="14" fill="{bg}"/><rect width="{w}" height="{h}" rx="14" fill="url(#gloss)"/>' + inner
        return group(x, y, rot, body, "sh", w / 2, h / 2)

    inner = (
        tri(170, 150, 210, "#f3c316", "#111316") + ico_bolt(170, 165, 80, "#111316")
        + '<rect x="0" y="270" width="340" height="110" rx="0" fill="#111316"/>'
        + T(170, 318, "خطر كهرباء", 40, "#f3c316", 900, font=AR) + T(170, 360, "DANGER HIGH VOLTAGE", 22, "#f3c316", 700, extra='letter-spacing="1"')
    )
    o.append(sign(110, 150, 340, 380, -4, inner))
    inner = (
        '<circle cx="170" cy="150" r="104" fill="#fff" stroke="#c8202a" stroke-width="22"/>'
        + ico_cig(170, 150, 120, "#111316")
        + '<line x1="98" y1="78" x2="242" y2="222" stroke="#c8202a" stroke-width="22"/>'
        + '<rect x="0" y="280" width="340" height="100" fill="#c8202a"/>'
        + T(170, 326, "ممنوع التدخين", 40, "#fff", 900, font=AR) + T(170, 364, "NO SMOKING", 24, "#fff", 700, extra='letter-spacing="3"')
    )
    o.append(sign(530, 120, 340, 380, 3, inner))
    inner = (
        '<circle cx="170" cy="150" r="108" fill="#1d4fbf"/>' + ico_helmet(170, 150, 130, "#fff")
        + '<rect x="0" y="280" width="340" height="100" fill="#1d4fbf"/>'
        + T(170, 326, "ارتدِ الخوذة", 40, "#fff", 900, font=AR) + T(170, 364, "WEAR HARD HAT", 24, "#fff", 700, extra='letter-spacing="2"')
    )
    o.append(sign(950, 160, 340, 380, -2, inner))
    inner = ico_exit(140, 100, 150, "#fff") + ico_arrow(300, 100, 110, "#fff") + T(230, 228, "مخرج طوارئ", 48, "#fff", 900, font=AR) + T(230, 270, "EMERGENCY EXIT", 24, "#e6f6ec", 700, extra='letter-spacing="3"')
    o.append(sign(250, 640, 460, 300, 2, inner, "#1f8a4c"))
    inner = (
        '<rect x="20" y="20" width="160" height="160" rx="10" fill="#fff"/>' + ico_fire(100, 100, 110, "#c8202a")
        + T(310, 96, "طفاية حريق", 40, "#fff", 900, font=AR) + T(310, 142, "FIRE EXTINGUISHER", 20, "#fff", 700)
    )
    o.append(sign(800, 660, 440, 200, -3, inner, "#c8202a"))
    return "".join(o)


def scene_badges():
    o = []

    def badge(x, y, rot, fill, name, role, fg, sub, logo_fg, shape_r=16, w=440, h=150):
        f = FILLS.get(fill, fill)
        brushed = f'<rect width="{w}" height="{h}" rx="{shape_r}" fill="#fff" filter="url(#brush)" opacity=".45"/>' if fill in FILLS else ""
        body = (
            f'<rect width="{w}" height="{h}" rx="{shape_r}" fill="{f}"/>{brushed}<rect width="{w}" height="{h}" rx="{shape_r}" fill="url(#gloss)"/>'
            f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{shape_r}" fill="none" stroke="#0d0f12" stroke-opacity=".2" stroke-width="2"/>'
            f'<rect x="{w-112}" y="28" width="86" height="86" rx="12" fill="none" stroke="{logo_fg}" stroke-width="3"/>'
            + T(w - 69, 84, "R", 52, logo_fg, 900)
            + T(w - 138, 68, name, 38, fg, 900, "end", AR)
            + T(w - 138, 110, role, 24, sub, 700, "end", AR)
        )
        return group(x, y, rot, body, "sh", w / 2, h / 2)

    o.append(badge(120, 170, -4, "steel", "أحمد الزهراني", "مدير المبيعات", "#15181d", "#3d434c", "#15181d"))
    o.append(badge(700, 140, 3, "brass", "نورة القحطاني", "خدمة العملاء", "#3b2806", "#5a3e0e", "#3b2806"))
    o.append(badge(160, 430, 2, "#111316", "فيصل الغامدي", "مهندس مشاريع", "#f2f5f8", "#aeb6c1", "#d9b25a"))
    o.append(badge(740, 420, -3, "#1d4fbf", "ريم الشهري", "استقبال", "#ffffff", "#dfe8ff", "#ffffff"))
    o.append(badge(430, 700, -1, "#ffffff", "عبدالله المالكي", "مشرف سلامة", "#15181d", "#c8202a", "#c8202a"))
    # مغناطيس خلفي
    back = (
        '<rect width="300" height="110" rx="14" fill="#2a2f36"/>'
        '<rect x="40" y="25" width="220" height="60" rx="8" fill="#6b727d"/>'
        + T(150, 64, "MAGNET", 22, "#e9edf2", 700, extra='letter-spacing="5"')
    )
    o.append(group(1020, 760, 6, back))
    return "".join(o)


def scene_cable():
    o = []
    for i, (y, c) in enumerate(((260, "#1d1f23"), (470, "#2b2f35"), (680, "#1d1f23"), (880, "#33373d"))):
        o.append(
            f'<g filter="url(#shs)"><rect x="-20" y="{y-38}" width="1440" height="76" rx="38" fill="url(#cable)"/>'
            f'<rect x="-20" y="{y-30}" width="1440" height="10" rx="5" fill="#fff" opacity=".08"/></g>'
        )
    tags = [(250, 260, "CB-01", "L1 · 400A"), (760, 470, "MDB-03", "TO DB-2F"), (420, 680, "PV-STR-07", "DC 1000V"), (980, 880, "FO-12", "FIBER")]
    for x, y, a, b in tags:
        tag = (
            T(150, 78, a, 40, "#1d2127", 900, font=MONO) + T(150, 116, b, 22, "#2a2f36", 700, extra='letter-spacing="2"')
            + f'<rect x="-36" y="48" width="36" height="56" rx="6" fill="#d9dde3" stroke="#8b929c" stroke-width="2"/>'
            + f'<rect x="300" y="48" width="36" height="56" rx="6" fill="#d9dde3" stroke="#8b929c" stroke-width="2"/>'
        )
        o.append(plate(x, y - 72, 300, 150, "steel", 10, 0, tag))
        # رباط كيبل
        for dx in (-18, 318):
            o.append(f'<rect x="{x+dx-7}" y="{y-46}" width="14" height="92" rx="5" fill="#9aa1ab" stroke="#6b727d" stroke-width="2"/>')
    # تاق ملفوف صغير
    body = T(100, 50, "N-14", 30, "#1d2127", 900, font=MONO)
    o.append(plate(1120, 150, 200, 76, "alu", 38, 6, body))
    return "".join(o)


def scene_tags():
    o = []
    # سلسلة كرات
    def chain(path, n=46):
        return f'<path d="{path}" fill="none" stroke="#9aa1ab" stroke-width="9" stroke-dasharray="1 13" stroke-linecap="round"/>'

    o.append(chain("M160 120 C 300 420, 520 420, 640 160"))
    dog = "M30 0 H230 Q260 0 260 30 V100 Q260 130 230 130 H30 Q0 130 0 100 V30 Q0 0 30 0z"

    def dogtag(x, y, rot, lines):
        txt = "".join(T(140, 52 + i * 34, s, 26 if i else 30, "#1d2127", 900 if i == 0 else 700, font=AR if any('؀' <= c <= 'ۿ' for c in s) else MONO) for i, s in enumerate(lines))
        body = (
            f'<path d="{dog}" transform="scale(1.08)" fill="url(#steel)"/><path d="{dog}" transform="scale(1.08)" fill="#fff" filter="url(#brush)" opacity=".5"/>'
            f'<path d="{dog}" transform="scale(1.08)" fill="none" stroke="#0d0f12" stroke-opacity=".25" stroke-width="2"/>'
            + through(20, 70, 9) + txt
        )
        return group(x, y, rot, body, "sh", 140, 70)

    o.append(dogtag(260, 360, -18, ["SALEH A.", "O+ · 1092-44", "JEDDAH KSA"]))
    o.append(dogtag(470, 310, 14, ["سعيد خالد", "فصيلة الدم A+", "0543·xxx·xxx"]))
    # عظمة للحيوانات
    bone = "M60 30 a30 30 0 1 1 30 -24 h140 a30 30 0 1 1 30 24 a30 30 0 1 1 -30 54 h-140 a30 30 0 1 1 -30 -54z"
    body = (
        f'<path d="{bone}" fill="url(#brass)"/><path d="{bone}" fill="#fff" filter="url(#brush)" opacity=".4"/>'
        + T(160, 46, "LUNA", 40, "#3b2806", 900) + T(160, 80, "05x xxx xxxx", 20, "#4a3410", 700)
    )
    o.append(group(860, 170, -6, body))
    # ميداليات مفاتيح
    for x, y, f, a, b, rot in ((870, 520, "steel", "R", "رواد الليزر", 0), (1150, 470, "#111316", "W", "WELCOME", 0)):
        fl = FILLS.get(f, f)
        fg = "#15181d" if f == "steel" else "#e9edf2"
        body = (
            '<circle cx="0" cy="-150" r="34" fill="none" stroke="#9aa1ab" stroke-width="10"/>'
            '<rect x="-8" y="-118" width="16" height="40" rx="6" fill="#9aa1ab"/>'
            f'<circle r="100" fill="{fl}"/>'
            + ('<circle r="100" fill="#fff" filter="url(#brush)" opacity=".45"/>' if f == "steel" else "")
            + '<circle r="100" fill="url(#gloss)"/>'
            + through(0, -78, 9)
            + T(0, 22, a, 80, fg, 900)
            + T(0, 66, b, 22, fg, 700, font=AR if a == "R" else EN)
        )
        o.append(group(x, y + 80, rot, body))
    # تاقات حقائب / معدات
    body = T(190, 62, "ASSET  ·  أصل رقم", 22, "#2a2f36", 700, font=EN) + T(190, 108, "IT-00482", 40, "#1d2127", 900, font=MONO) + barcode(60, 124, 260, 24, "#2a2f36")
    o.append(plate(170, 720, 380, 170, "alu", 14, 4, body))
    body = T(170, 64, "TOOL-17", 38, "#1d2127", 900, font=MONO) + T(170, 108, "ورشة الصيانة", 26, "#2a2f36", 700, font=AR) + through(24, 76, 8)
    o.append(plate(620, 780, 340, 150, "steel", 70, -3, body))
    return "".join(o)


def scene_loto():
    o = []

    def tag(x, y, rot, top, head, ar, en_lines, band="#c8202a", fg="#fff"):
        w, h = 260, 520
        body = (
            f'<rect width="{w}" height="{h}" rx="22" fill="#ffffff"/><rect width="{w}" height="{h}" rx="22" fill="url(#gloss)"/>'
            f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="22" fill="none" stroke="#0d0f12" stroke-opacity=".18" stroke-width="2"/>'
            f'<rect x="0" y="70" width="{w}" height="120" fill="{band}"/>'
            f'<circle cx="{w/2}" cy="38" r="20" fill="#dfe3e8" stroke="#8b929c" stroke-width="5"/>'
            + T(w / 2, 124, head, 46, fg, 900) + T(w / 2, 172, ar, 30, fg, 800, font=AR)
            + "".join(T(w / 2, 248 + i * 38, s, 26, "#15181d", 900 if i < 2 else 600, font=AR if any('؀' <= c <= 'ۿ' for c in s) else EN) for i, s in enumerate(en_lines))
            + ico_lock(w / 2, 440, 70, band)
        )
        return group(x, y, rot, body, "sh", w / 2, h / 2)

    o.append(tag(120, 220, -7, "#fff", "DANGER", "خطر", ["DO NOT", "OPERATE", "لا تشغّل المعدة", "Name: ________"]))
    o.append(tag(460, 170, 3, "#fff", "LOCKED", "مقفل", ["EQUIPMENT", "LOCKED OUT", "أعمال صيانة", "Date: ________"], "#111316"))
    o.append(tag(800, 230, -3, "#fff", "CAUTION", "تنبيه", ["DO NOT", "REMOVE TAG", "لا تُزِل البطاقة", "Dept: ________"], "#f3c316", "#111316"))
    # قفل أمان أحمر
    lock = (
        '<path d="M-60 -10 V-90 a60 60 0 0 1 120 0 V-10" fill="none" stroke="url(#steel)" stroke-width="26"/>'
        '<path d="M-60 -10 V-90 a60 60 0 0 1 120 0 V-10" fill="none" stroke="#6b727d" stroke-width="2" stroke-opacity=".6"/>'
        '<rect x="-95" y="-20" width="190" height="200" rx="26" fill="#c8202a"/><rect x="-95" y="-20" width="190" height="200" rx="26" fill="url(#gloss)"/>'
        '<circle cy="60" r="14" fill="#5a0e12"/><rect x="-5" y="60" width="10" height="40" fill="#5a0e12"/>'
        + T(0, 160, "LOTO-07", 24, "#fff", 800)
    )
    o.append(group(1220, 560, 6, lock))
    return "".join(o)


def scene_valve():
    o = []
    # أنبوب ومحبس
    o.append(
        '<g filter="url(#shs)"><rect x="-20" y="300" width="1440" height="110" fill="url(#steel)"/>'
        '<rect x="-20" y="300" width="1440" height="110" fill="#fff" filter="url(#brush)" opacity=".35"/>'
        '<rect x="-20" y="318" width="1440" height="12" fill="#fff" opacity=".4"/></g>'
    )
    o.append(
        '<g filter="url(#sh)"><rect x="560" y="270" width="200" height="170" rx="18" fill="#c8202a"/>'
        '<rect x="640" y="150" width="40" height="130" fill="#8b929c"/>'
        '<ellipse cx="660" cy="140" rx="150" ry="26" fill="#c8202a"/><ellipse cx="660" cy="132" rx="150" ry="20" fill="#e2454d"/>'
        '<circle cx="660" cy="132" r="18" fill="#8b929c"/></g>'
    )
    # سلسلة وتاق معلّق
    o.append('<path d="M760 420 C 800 470, 820 500, 830 540" fill="none" stroke="#9aa1ab" stroke-width="8" stroke-dasharray="2 12" stroke-linecap="round"/>')

    def disc(x, y, f, a, b, fg="#1d2127", r=110):
        fl = FILLS.get(f, f)
        body = (
            f'<circle r="{r}" fill="{fl}"/>'
            + (f'<circle r="{r}" fill="#fff" filter="url(#brush)" opacity=".45"/>' if f in FILLS else "")
            + f'<circle r="{r}" fill="url(#gloss)"/>'
            + f'<circle r="{r-14}" fill="none" stroke="{fg}" stroke-opacity=".45" stroke-width="2.5"/>'
            + through(0, -r + 26, 10)
            + T(0, 14, a, 46 if len(a) < 7 else 38, fg, 900, font=MONO)
            + T(0, 54, b, 22, fg, 700, font=AR if any('؀' <= c <= 'ۿ' for c in b) else EN, extra="" if any('؀' <= c <= 'ۿ' for c in b) else 'letter-spacing="2"')
        )
        return group(x, y, 0, body)

    o.append(disc(840, 660, "brass", "V-101", "CHW SUPPLY", "#3b2806"))
    o.append(disc(230, 640, "steel", "HV-2001", "محبس رئيسي"))
    o.append(disc(1160, 700, "#1d4fbf", "FW-14", "FIRE WATER", "#fff", 100))
    o.append(disc(520, 830, "#1f8a4c", "NC", "CLOSED", "#fff", 92))
    o.append(disc(1180, 160, "alu", "ST-07", "STEAM", "#1d2127", 92))
    o.append(disc(200, 150, "#f3c316", "GAS-3", "غاز", "#111316", 92))
    return "".join(o)


def scene_hub():
    o = []
    # مزيج: تاق محبس، تاق لوتو، لوحة سلامة، بادج، لوحة بيانات، تاق كيبل
    body = T(240, 70, "SERIAL NO.", 22, "#2a2f36", 700, extra='letter-spacing="3"') + T(240, 122, "RL-26-0418", 48, "#1d2127", 900, font=MONO) + qr(370, 150, 80, "#2a2f36", 5) + barcode(40, 160, 300, 60, "#2a2f36") + hole(22, 22, 7) + hole(458, 22, 7) + hole(22, 238, 7) + hole(458, 238, 7)
    o.append(plate(110, 140, 480, 260, "steel", 14, -4, body))
    sign = (
        '<rect width="300" height="340" rx="14" fill="#fff"/><rect width="300" height="340" rx="14" fill="url(#gloss)"/>'
        + tri(150, 130, 190, "#f3c316", "#111316") + ico_bolt(150, 144, 72, "#111316")
        + '<rect y="248" width="300" height="92" fill="#111316"/>' + T(150, 290, "خطر كهرباء", 36, "#f3c316", 900, font=AR) + T(150, 326, "HIGH VOLTAGE", 20, "#f3c316", 700, extra='letter-spacing="2"')
    )
    o.append(group(660, 110, 4, sign, "sh", 150, 170))
    loto = (
        '<rect width="200" height="400" rx="18" fill="#fff"/><rect y="56" width="200" height="96" fill="#c8202a"/>'
        '<circle cx="100" cy="30" r="15" fill="#dfe3e8" stroke="#8b929c" stroke-width="4"/>'
        + T(100, 100, "DANGER", 36, "#fff", 900) + T(100, 138, "خطر", 26, "#fff", 800, font=AR)
        + T(100, 200, "DO NOT", 24, "#15181d", 900) + T(100, 232, "OPERATE", 24, "#15181d", 900) + ico_lock(100, 330, 60, "#c8202a")
    )
    o.append(group(1060, 150, -6, loto, "sh", 100, 200))
    d = (
        '<circle r="105" fill="url(#brass)"/><circle r="105" fill="#fff" filter="url(#brush)" opacity=".4"/>'
        + through(0, -80, 9) + T(0, 16, "V-101", 44, "#3b2806", 900, font=MONO) + T(0, 54, "CHW", 22, "#3b2806", 700, extra='letter-spacing="3"')
    )
    o.append(group(260, 680, 0, d))
    b = (
        '<rect width="420" height="140" rx="16" fill="#111316"/><rect width="420" height="140" rx="16" fill="url(#gloss)"/>'
        '<rect x="316" y="26" width="80" height="80" rx="12" fill="none" stroke="#d9b25a" stroke-width="3"/>' + T(356, 82, "R", 48, "#d9b25a", 900)
        + T(292, 64, "فيصل الغامدي", 36, "#f2f5f8", 900, "end", AR) + T(292, 104, "مهندس مشاريع", 22, "#aeb6c1", 700, "end", AR)
    )
    o.append(group(470, 560, 2, b, "sh", 210, 70))
    lamb = T(240, 70, "MAIN SWITCH", 40, "#fff", 800) + T(240, 112, "DB-01", 24, "#fff", 600, extra='letter-spacing="4"') + through(24, 70, 8) + through(456, 70, 8)
    o.append(lam(880, 600, 480, 140, "#c8202a", "#ffffff", -3, lamb))
    ctag = T(140, 60, "CB-01", 38, "#1d2127", 900, font=MONO) + T(140, 98, "L1 · 400A", 20, "#2a2f36", 700)
    o.append(plate(540, 800, 280, 130, "steel", 10, -2, ctag))
    return "".join(o)


SCENES = {
    "aluminum-engraving": scene_aluminum,
    "brass-engraving": scene_brass,
    "traffolyte-engraving": scene_traffolyte,
    "pvc-abs-engraving": scene_pvc,
    "acrylic-engraving": scene_acrylic,
    "diamond-engraving": scene_diamond,
    "signage-plates": scene_signage,
    "route-marker-plates": scene_route,
    "safety-signs": scene_safety,
    "name-badges": scene_badges,
    "cable-id-tags": scene_cable,
    "engraved-tags": scene_tags,
    "loto-safety-tags": scene_loto,
    "valve-tags": scene_valve,
    "industrial-labels-tags": scene_hub,
}


def svg_doc(inner):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{DEFS}'
        f'<rect width="{W}" height="{H}" fill="url(#bg)"/><rect width="{W}" height="{H}" fill="url(#grid)"/>{inner}</svg>'
    )


def render(name):
    svg = svg_doc(SCENES[name]())
    page = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Thmanyah;src:url('file://{FONTS}/ThmanyahSans-Bold.woff2');font-weight:500 700}}
@font-face{{font-family:Thmanyah;src:url('file://{FONTS}/ThmanyahSans-Black.woff2');font-weight:800 900}}
@font-face{{font-family:Thmanyah;src:url('file://{FONTS}/ThmanyahSans-Medium.woff2');font-weight:100 499}}
html,body{{margin:0;padding:0;width:{W}px;height:{H}px;overflow:hidden}}</style></head><body>{svg}</body></html>"""
    tmp = tempfile.mkdtemp()
    hp = os.path.join(tmp, "s.html")
    png = os.path.join(tmp, "s.png")
    open(hp, "w", encoding="utf-8").write(page)
    subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
         f"--window-size={W},{H}", "--virtual-time-budget=3000", f"--screenshot={png}", "file://" + hp],
        check=True, capture_output=True,
    )
    out = os.path.join(OUT, f"ill-{name}.jpg")
    Image.open(png).convert("RGB").crop((0, 0, W, H)).save(out, "JPEG", quality=84, optimize=True, progressive=True)
    print(f"✓ ill-{name}.jpg  ({os.path.getsize(out)/1024:.0f} KB)")


if __name__ == "__main__":
    for n in sys.argv[1:] or SCENES:
        render(n)
