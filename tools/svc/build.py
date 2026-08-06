#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مولّد صفحات الخدمات — رواد الليزر
=================================
كل خدمة = صفحة HTML مستقلة، مبنية من ملف بيانات واحد في tools/svc/pages/<slug>.py
الهيكل (الهيدر/الفوتر/أيقونات SVG) يُستخرج آلياً من laser-cutting-services.html
حتى يبقى شكل الموقع موحّداً 100%.

التشغيل:
    python3 tools/svc/build.py            # يبني كل الصفحات
    python3 tools/svc/build.py slug1 ...  # يبني صفحات محددة
"""
import html
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(os.path.dirname(HERE))
PAGES_DIR = os.path.join(HERE, "pages")
BASE = "https://rowadlaser.com/"
CSS_V = "6"
JS_V = "4"

# ============================================================
#  أدوات مساعدة
# ============================================================


def esc(s):
    return html.escape(str(s), quote=True)


def bi(ar, en):
    """سمات ثنائية اللغة + النص العربي الظاهر افتراضياً"""
    return f'data-ar="{esc(ar)}" data-en="{esc(en)}">{esc(ar)}'


def el(tag, ar, en, cls=None, attrs=""):
    c = f' class="{cls}"' if cls else ""
    a = f" {attrs}" if attrs else ""
    return f"<{tag}{c}{a} {bi(ar, en)}</{tag}>"


def ico(name):
    return f'<svg><use href="#i-{name}"/></svg>'


def pair(v):
    """يقبل (ar, en) أو نصاً واحداً"""
    if isinstance(v, (tuple, list)):
        return v[0], v[1]
    return v, v


# ============================================================
#  الهيكل المشترك (يُستخرج من صفحة قائمة أصلاً)
# ============================================================


def shared_chrome():
    src = open(os.path.join(SITE, "laser-cutting-services.html"), encoding="utf-8").read()

    sprite = re.search(r'<svg width="0" height="0".*?</defs></svg>', src, re.S).group(0)
    header = re.search(r"<header class=\"site-header\">.*?</header>", src, re.S).group(0)
    menu = re.search(r'<div class="mobile-menu">.*?(?=<section)', src, re.S).group(0)
    footer = re.search(r"<footer class=\"site-footer\">.*?</footer>", src, re.S).group(0)
    fab = re.search(r'<a class="fab-wa".*?</a>', src, re.S).group(0)

    # عمود «خدماتنا» في الفوتر — روابط الصفحات المستقلة الجديدة
    footer_services = """<div>
        <h4 data-ar="خدماتنا" data-en="Services">خدماتنا</h4>
        <ul>
          <li><a href="services.html" data-ar="كل الخدمات" data-en="All services">كل الخدمات</a></li>
          <li><a href="laser-metal-cutting.html" data-ar="قص المعادن بالليزر" data-en="Laser metal cutting">قص المعادن بالليزر</a></li>
          <li><a href="metal-bending-forming.html" data-ar="تشكيل وثني المعادن" data-en="Bending &amp; forming">تشكيل وثني المعادن</a></li>
          <li><a href="stainless-steel-fabrication.html" data-ar="تصنيع الستانلس ستيل" data-en="Stainless fabrication">تصنيع الستانلس ستيل</a></li>
          <li><a href="metal-fabrication.html" data-ar="تصنيع المعادن" data-en="Metal fabrication">تصنيع المعادن</a></li>
          <li><a href="fiber-marking.html" data-ar="الحفر والنحت على المعادن" data-en="Metal engraving">الحفر والنحت على المعادن</a></li>
          <li><a href="custom-metal-solutions.html" data-ar="حلول مخصصة حسب الطلب" data-en="Custom solutions">حلول مخصصة حسب الطلب</a></li>
          <li><a href="contracting-metal-projects.html" data-ar="مشاريع المقاولات والكميات" data-en="Contracting &amp; bulk">مشاريع المقاولات والكميات</a></li>
          <li><a href="metal-finishing-quality.html" data-ar="التشطيب وفحص الجودة" data-en="Finishing &amp; QC">التشطيب وفحص الجودة</a></li>
          <li><a href="laser-jeddah.html" data-ar="قص ليزر في جدة" data-en="Laser cutting in Jeddah">قص ليزر في جدة</a></li>
        </ul>
      </div>"""
    footer = re.sub(
        r"<div>\s*<h4 data-ar=\"خدماتنا\".*?</ul>\s*</div>",
        lambda m: footer_services,
        footer,
        count=1,
        flags=re.S,
    )
    return sprite, header, menu, footer, fab


SPRITE, HEADER, MENU, FOOTER, FAB = shared_chrome()

# ============================================================
#  أقسام الصفحة
# ============================================================


def sec_hero(p):
    h = p["hero"]
    ar_e, en_e = pair(h["eyebrow"])
    ar_h, en_h = pair(h["h1"])
    ar_s, en_s = pair(h["sub"])
    img, alt, w, hh = h["img"]
    alt_ar, alt_en = pair(alt)
    chips = "".join(
        f'<span class="chip">{ico(c[2] if len(c) > 2 else "check")}<span {bi(c[0], c[1])}</span></span>'
        for c in h.get("chips", [])
    )
    crumb_parent = ""
    if p.get("parent"):
        pa, pe = pair(p["parent"]["name"])
        crumb_parent = (
            f'<a href="{p["parent"]["slug"]}.html" {bi(pa, pe)}</a>{ico("chev")}'
        )
    mid = (
        ""
        if p.get("is_hub")
        else f'<a href="services.html" {bi("خدماتنا", "Services")}</a>{ico("chev")}'
    )
    crumbs = (
        '<nav class="crumbs" aria-label="مسار التنقل">'
        f'<a href="index.html" {bi("الرئيسية", "Home")}</a>{ico("chev")}'
        f"{mid}"
        f"{crumb_parent}"
        f'<span {bi(*pair(p["crumb"]))}</span>'
        "</nav>"
    )
    wa_msg = h.get("wa", "مرحباً رواد الليزر، أرغب في طلب عرض سعر.")
    return f"""<section class="lp-hero">
  <div class="container">
    {crumbs}
    <div class="lp-grid">
      <div>
        <span class="eyebrow" {bi(ar_e, en_e)}</span>
        <h1 {bi(ar_h, en_h)}</h1>
        <p class="lp-sub" {bi(ar_s, en_s)}</p>
        <div class="lp-cta">
          <a href="#quote" class="btn btn-primary btn-lg" {bi("اطلب عرض سعر", "Get a Quote")}</a>
          <a href="#" class="btn btn-wa btn-lg" data-wa="{esc(wa_msg)}">{ico('wa')}<span {bi("راسلنا واتساب", "WhatsApp us")}</span></a>
        </div>
        <div class="chips">{chips}</div>
      </div>
      <div class="lp-shot">
        <img src="{img}" alt="{esc(alt_ar)}" data-ar-alt="{esc(alt_ar)}" data-en-alt="{esc(alt_en)}" width="{w}" height="{hh}" fetchpriority="high" decoding="async" />
      </div>
    </div>
  </div>
</section>"""


def sec_subnav(p):
    subs = p.get("sub_pages")
    if not subs:
        return ""
    links = "".join(
        f'<a class="chip" href="{s["href"]}">{ico("arrow")}<span {bi(*pair(s["name"]))}</span></a>'
        for s in subs
    )
    ar, en = pair(p.get("subnav_title", ("صفحات متخصصة داخل هذه الخدمة", "Specialised pages inside this service")))
    return f"""<section class="strip">
  <div class="container">
    <p style="text-align:center;color:var(--muted);font-size:.92rem;margin-bottom:14px" {bi(ar, en)}</p>
    <div class="chips" style="justify-content:center;margin-top:0">{links}</div>
  </div>
</section>"""


def sec_facts(p):
    facts = p.get("facts")
    if not facts:
        return ""
    out = []
    for f in facts:
        va, ve = pair(f[0])
        la, le = pair(f[1])
        ltr = ' dir="ltr"' if re.match(r"^[\d\W]*[A-Za-z\d]", va) else ""
        out.append(
            f'<div class="fact reveal"><b{ltr} {bi(va, ve)}</b><span {bi(la, le)}</span></div>'
        )
    return f"""<section class="section section--tight section--soft">
  <div class="container"><div class="facts">{''.join(out)}</div></div>
</section>"""


def _head_block(d, center=True, dark=False):
    parts = []
    if d.get("eyebrow"):
        parts.append(f'<span class="eyebrow" {bi(*pair(d["eyebrow"]))}</span>')
    if d.get("h2"):
        style = ' style="margin-top:16px"' if d.get("eyebrow") else ""
        if dark:
            style = f' style="margin-top:16px;color:#fff"' if d.get("eyebrow") else ' style="color:#fff"'
        parts.append(f'<h2 class="h-section"{style} {bi(*pair(d["h2"]))}</h2>')
    if d.get("lead"):
        parts.append(f'<p class="lead" {bi(*pair(d["lead"]))}</p>')
    cls = "section-head center reveal" if center else "section-head reveal"
    return f'<div class="{cls}">{"".join(parts)}</div>'


def sec_intro(p):
    d = p.get("intro")
    if not d:
        return ""
    paras = "".join(f"<p {bi(*pair(x))}</p>" for x in d.get("paras", []))
    bullets = ""
    if d.get("bullets"):
        lis = "".join(f"<li {bi(*pair(x))}</li>" for x in d["bullets"])
        bullets = f'<ul class="bullets">{lis}</ul>'
    h3 = ""
    if d.get("h3"):
        h3 = f"<h3 {bi(*pair(d['h3']))}</h3>"
    paras2 = "".join(f"<p {bi(*pair(x))}</p>" for x in d.get("paras2", []))
    return f"""<section class="section">
  <div class="container">
    <div class="article reveal">
      <h2 style="margin-top:0" {bi(*pair(d["h2"]))}</h2>
      {paras}
      {h3}
      {bullets}
      {paras2}
    </div>
  </div>
</section>"""


def sec_cards(p):
    return _cards(p.get("cards"))


def sec_cards2(p):
    return _cards(p.get("cards2"))


def _cards(d):
    if not d:
        return ""
    items = []
    for c in d["items"]:
        more = ""
        if c.get("href"):
            ma, me = pair(c.get("more", ("تفاصيل الخدمة", "Service details")))
            more = f'<a class="more" href="{c["href"]}" {bi(ma, me)} {ico("arrow")}</a>'
        items.append(
            f'<article class="card reveal"><div class="ic-box">{ico(c["icon"])}</div>'
            f'<h3 {bi(*pair(c["h3"]))}</h3><p {bi(*pair(c["p"]))}</p>{more}</article>'
        )
    grid = d.get("grid", "grid-3")
    soft = " section--soft" if d.get("soft") else ""
    return f"""<section class="section{soft}">
  <div class="container">
    {_head_block(d)}
    <div class="grid {grid}">{''.join(items)}</div>
  </div>
</section>"""


def sec_specs(p):
    d = p.get("specs")
    if not d:
        return ""
    ths = "".join(f"<th {bi(*pair(c))}</th>" for c in d["cols"])
    rows = []
    for r in d["rows"]:
        tds = "".join(
            (f"<th scope=\"row\" {bi(*pair(c))}</th>" if i == 0 else f"<td {bi(*pair(c))}</td>")
            for i, c in enumerate(r)
        )
        rows.append(f"<tr>{tds}</tr>")
    note = ""
    if d.get("note"):
        note = f'<p class="form-note" style="margin-top:14px" {bi(*pair(d["note"]))}</p>'
    soft = " section--soft" if d.get("soft") else ""
    return f"""<section class="section{soft}">
  <div class="container" style="max-width:960px">
    {_head_block(d)}
    <div class="table-wrap reveal">
      <table class="spec-table">
        <thead><tr>{ths}</tr></thead>
        <tbody>{''.join(rows)}</tbody>
      </table>
    </div>
    {note}
  </div>
</section>"""


def sec_gallery(p):
    d = p.get("gallery")
    if not d:
        return ""
    shots = []
    for g in d["items"]:
        src, alt, label = g[0], g[1], g[2]
        aa, ae = pair(alt)
        la, le = pair(label)
        w, h = (g[3], g[4]) if len(g) > 4 else (1400, 1050)
        shots.append(
            f'<div class="shot"><img class="shot-img" src="{src}" alt="{esc(aa)}" '
            f'data-ar-alt="{esc(aa)}" data-en-alt="{esc(ae)}" width="{w}" height="{h}" loading="lazy" decoding="async" />'
            f'<span class="label" {bi(la, le)}</span></div>'
        )
    note = ""
    if d.get("note"):
        note = f'<p class="form-note" style="text-align:center;margin-top:20px" {bi(*pair(d["note"]))}</p>'
    soft = " section--soft" if d.get("soft") else ""
    return f"""<section class="section{soft}">
  <div class="container">
    {_head_block(d)}
    <div class="gallery reveal">{''.join(shots)}</div>
    {note}
  </div>
</section>"""


def sec_uses(p):
    d = p.get("uses")
    if not d:
        return ""
    items = "".join(
        f'<div class="use reveal"><div class="ic">{ico(u["icon"])}</div>'
        f'<h3 {bi(*pair(u["h3"]))}</h3><p {bi(*pair(u["p"]))}</p></div>'
        for u in d["items"]
    )
    soft = " section--soft" if d.get("soft") else ""
    return f"""<section class="section{soft}">
  <div class="container">
    {_head_block(d)}
    <div class="uses">{items}</div>
  </div>
</section>"""


def sec_sectors(p):
    d = p.get("sectors")
    if not d:
        return ""
    items = "".join(
        f'<div class="sector reveal"><div class="bg"></div><div class="ic">{ico(s["icon"])}</div>'
        f'<div class="txt"><h3 {bi(*pair(s["h3"]))}</h3><p {bi(*pair(s["p"]))}</p></div></div>'
        for s in d["items"]
    )
    soft = " section--soft" if d.get("soft") else ""
    return f"""<section class="section{soft}">
  <div class="container">
    {_head_block(d)}
    <div class="grid grid-4">{items}</div>
  </div>
</section>"""


def sec_process(p):
    d = p.get("process")
    if not d:
        return ""
    steps = "".join(
        f'<div class="step reveal"><div class="num"></div><h3 {bi(*pair(s["h3"]))}</h3>'
        f'<p {bi(*pair(s["p"]))}</p></div>'
        for s in d["steps"]
    )
    need = ""
    if d.get("need"):
        lis = "".join(f"<li {bi(*pair(x))}</li>" for x in d["need"]["items"])
        need = f"""<div class="card reveal" style="margin-top:clamp(36px,4vw,56px)">
      <h3 {bi(*pair(d["need"]["h3"]))}</h3>
      <ul class="bullets" style="margin-top:14px;margin-bottom:0">{lis}</ul>
    </div>"""
    soft = " section--soft" if d.get("soft") else ""
    return f"""<section class="section{soft}">
  <div class="container">
    {_head_block(d)}
    <div class="steps">{steps}</div>
    {need}
  </div>
</section>"""


def sec_why(p):
    d = p.get("why")
    if not d:
        return ""
    items = "".join(
        f'<div class="value reveal"><div class="ic" style="background:rgba(255,255,255,.06);border-color:var(--dark-line);color:#fff">{ico(v["icon"])}</div>'
        f'<div><h3 style="color:#fff" {bi(*pair(v["h3"]))}</h3>'
        f'<p style="color:var(--on-dark-muted)" {bi(*pair(v["p"]))}</p></div></div>'
        for v in d["items"]
    )
    return f"""<section class="section band-dark">
  <div class="container">
    {_head_block(d, dark=True)}
    <div class="grid grid-4" style="gap:clamp(22px,3vw,34px)">{items}</div>
  </div>
</section>"""


def sec_related(p):
    d = p.get("related")
    if not d:
        return ""
    items = "".join(
        f'<article class="card reveal"><div class="ic-box">{ico(r["icon"])}</div>'
        f'<h3 {bi(*pair(r["h3"]))}</h3><p {bi(*pair(r["p"]))}</p>'
        f'<a class="more" href="{r["href"]}" {bi("اذهب إلى الصفحة", "Open the page")} {ico("arrow")}</a></article>'
        for r in d["items"]
    )
    soft = " section--soft" if d.get("soft", True) else ""
    return f"""<section class="section{soft}">
  <div class="container">
    {_head_block(d)}
    <div class="grid grid-3">{items}</div>
    <p style="text-align:center;margin-top:clamp(30px,4vw,44px)">
      <a href="services.html" class="btn btn-ghost" {bi("استعرض كل خدمات رواد الليزر", "Browse all Ruwwad Laser services")}</a>
    </p>
  </div>
</section>"""


def sec_faq(p):
    faq = p.get("faq")
    if not faq:
        return ""
    items = "".join(
        f'<div class="faq-item"><button class="faq-q" type="button"><span {bi(*pair(f["q"]))}</span>'
        f'<span class="chev">{ico("chev")}</span></button>'
        f'<div class="faq-a"><p {bi(*pair(f["a"]))}</p></div></div>'
        for f in faq
    )
    d = p.get("faq_head", {"eyebrow": ("أسئلة شائعة", "FAQ"), "h2": ("أسئلة يسألها عملاؤنا كثيراً", "Questions our clients often ask")})
    return f"""<section class="section">
  <div class="container" style="max-width:820px">
    {_head_block(d)}
    <div class="reveal">{items}</div>
  </div>
</section>"""


def sec_quote(p):
    svc = p.get("form_services") or []
    opts = "".join(f"<option {bi(*pair(s))}</option>" for s in svc)
    wa = p.get("form_wa", "مرحباً رواد الليزر، أرغب في طلب عرض سعر.")
    ar, en = pair(p.get("quote_h2", ("أرسل تفاصيل طلبك الآن", "Send your request now")))
    la, le = pair(
        p.get(
            "quote_lead",
            (
                "املأ النموذج وسنرد عليك بعرض سعر واضح وجدول تنفيذ محدد — بدون أي التزام.",
                "Fill in the form and we will come back with a clear price and a defined schedule — with no obligation.",
            ),
        )
    )
    return f"""<section class="section section--soft" id="quote">
  <div class="container">
    <div class="contact-grid">
      <div>
        <span class="eyebrow" {bi("اطلب عرض سعر", "Request a quote")}</span>
        <h2 class="h-section" style="margin-top:10px" {bi(ar, en)}</h2>
        <p class="lead" {bi(la, le)}</p>
        <div style="margin-top:26px">
          <div class="info-item"><div class="ic">{ico('wa')}</div><div><b {bi("واتساب — الأسرع", "WhatsApp — fastest")}</b><a href="#" data-wa="{esc(wa)}" data-phone-text>0543225519</a></div></div>
          <div class="info-item"><div class="ic">{ico('mail')}</div><div><b {bi("البريد الإلكتروني", "Email")}</b><a data-mail href="#" data-mail-text>info@rowadlaser.com</a></div></div>
          <div class="info-item"><div class="ic">{ico('pin')}</div><div><b {bi("الموقع", "Location")}</b><span {bi("جدة، المملكة العربية السعودية", "Jeddah, Saudi Arabia")}</span></div></div>
          <div class="info-item"><div class="ic">{ico('clock')}</div><div><b {bi("أوقات العمل", "Working hours")}</b><span {bi("السبت – الخميس، 8 ص – 6 م", "Sat – Thu, 8AM – 6PM")}</span></div></div>
        </div>
      </div>
      <div class="form-card">
        <form id="quote-form" novalidate>
          <div class="form-row">
            <div class="field"><label {bi("الاسم", "Name")}</label><input name="name" required data-ar-ph="اسمك الكريم" data-en-ph="Your name" placeholder="اسمك الكريم" /></div>
            <div class="field"><label {bi("رقم الجوال", "Phone")}</label><input name="phone" required inputmode="tel" data-ar-ph="05xxxxxxxx" data-en-ph="05xxxxxxxx" placeholder="05xxxxxxxx" /></div>
          </div>
          <div class="field">
            <label {bi("الخدمة المطلوبة", "Service needed")}</label>
            <select name="service">{opts}</select>
          </div>
          <div class="field"><label {bi("تفاصيل الطلب", "Request details")}</label><textarea name="message" data-ar-ph="اشرح لنا نوع المعدن، السماكة، الكمية، القياسات، والموعد المطلوب…" data-en-ph="Tell us the metal type, thickness, quantity, dimensions, and deadline…" placeholder="اشرح لنا نوع المعدن، السماكة، الكمية، القياسات، والموعد المطلوب…"></textarea></div>
          <button type="submit" class="btn btn-primary btn-block btn-lg">{ico('wa')}<span {bi("إرسال عبر واتساب", "Send via WhatsApp")}</span></button>
          <p class="form-ok" hidden style="color:#1faf54;margin-top:12px;font-weight:600" {bi("تم تجهيز رسالتك، أكمل الإرسال عبر واتساب. شكراً!", "Your message is ready — complete sending on WhatsApp. Thank you!")}</p>
          <p class="form-note" {bi("بالضغط على الإرسال، سيفتح تطبيق واتساب برسالة تحتوي بياناتك لإرسالها إلينا.", "On submit, WhatsApp opens with a message containing your details to send to us.")}</p>
        </form>
      </div>
    </div>
  </div>
</section>"""


def sec_cta(p):
    d = p.get("cta", {})
    ar, en = pair(d.get("h2", ("جاهزون لتنفيذ طلبك", "Ready to execute your order")))
    la, le = pair(
        d.get(
            "p",
            ("أرسل لنا تفاصيل مشروعك الآن واحصل على عرض سعر سريع — بدون أي التزام.",
             "Send your project details now and get a fast quote — with no obligation."),
        )
    )
    wa = d.get("wa", "مرحباً رواد الليزر، أرغب في طلب عرض سعر.")
    return f"""<section class="section band-dark cta-band">
  <div class="container reveal">
    <h2 {bi(ar, en)}</h2>
    <p class="lead" {bi(la, le)}</p>
    <div class="btns">
      <a href="#quote" class="btn btn-primary btn-lg" {bi("اطلب عرض سعر", "Get a Quote")}</a>
      <a href="#" class="btn btn-wa btn-lg" data-wa="{esc(wa)}">{ico('wa')}<span {bi("واتساب", "WhatsApp")}</span></a>
    </div>
  </div>
</section>"""


# ============================================================
#  البيانات المنظمة (Structured Data)
# ============================================================

PROVIDER = """{
      "@type": "LocalBusiness",
      "@id": "https://rowadlaser.com/#business",
      "name": "رواد الليزر",
      "alternateName": "Ruwwad Laser",
      "url": "https://rowadlaser.com/",
      "logo": "https://rowadlaser.com/assets/logos/logo-brand-black.png",
      "telephone": "+966543225519",
      "email": "info@rowadlaser.com",
      "priceRange": "$$",
      "address": {"@type": "PostalAddress", "addressLocality": "جدة", "addressRegion": "منطقة مكة المكرمة", "addressCountry": "SA"}
    }"""


def j(s):
    """تهريب نص لـ JSON-LD"""
    return (
        str(s)
        .replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", " ")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
    )


def ld_service(p):
    sa, _ = pair(p["service_type"])
    na, _ = pair(p["schema_name"])
    da, _ = pair(p["schema_desc"])
    offers = ""
    if p.get("schema_offers"):
        items = ",\n        ".join(
            '{"@type": "Offer", "itemOffered": {"@type": "Service", "name": "%s"}}' % j(pair(o)[0])
            for o in p["schema_offers"]
        )
        offers = f""",
    "hasOfferCatalog": {{
      "@type": "OfferCatalog",
      "name": "{j(na)}",
      "itemListElement": [
        {items}
      ]
    }}"""
    return f"""<script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "serviceType": "{j(sa)}",
    "name": "{j(na)}",
    "description": "{j(da)}",
    "url": "{BASE}{p['slug']}.html",
    "image": "{BASE}{p['og_image']}",
    "areaServed": [
      {{"@type": "City", "name": "جدة"}},
      {{"@type": "City", "name": "مكة المكرمة"}},
      {{"@type": "AdministrativeArea", "name": "منطقة مكة المكرمة"}}
    ],
    "availableChannel": {{
      "@type": "ServiceChannel",
      "serviceUrl": "{BASE}{p['slug']}.html#quote",
      "servicePhone": {{"@type": "ContactPoint", "telephone": "+966543225519", "contactType": "sales"}}
    }},
    "provider": {PROVIDER}{offers}
  }}
  </script>"""


def ld_breadcrumb(p):
    if p.get("is_hub"):
        crumbs = [("الرئيسية", BASE), (pair(p["crumb"])[0], f"{BASE}{p['slug']}.html")]
        items = ",\n    ".join(
            '{"@type":"ListItem","position":%d,"name":"%s","item":"%s"}' % (i + 1, j(n), u)
            for i, (n, u) in enumerate(crumbs)
        )
        return f"""<script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
    {items}
  ]}}
  </script>"""
    crumbs = [("الرئيسية", BASE), ("خدماتنا", BASE + "services.html")]
    if p.get("parent"):
        crumbs.append((pair(p["parent"]["name"])[0], f"{BASE}{p['parent']['slug']}.html"))
    crumbs.append((pair(p["crumb"])[0], f"{BASE}{p['slug']}.html"))
    items = ",\n    ".join(
        '{"@type":"ListItem","position":%d,"name":"%s","item":"%s"}' % (i + 1, j(n), u)
        for i, (n, u) in enumerate(crumbs)
    )
    return f"""<script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
    {items}
  ]}}
  </script>"""


def ld_faq(p):
    if not p.get("faq"):
        return ""
    items = ",\n    ".join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
        % (j(pair(f["q"])[0]), j(pair(f["a"])[0]))
        for f in p["faq"]
    )
    return f"""<script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
    {items}
  ]}}
  </script>"""


def ld_extra(p):
    return "\n  ".join(p.get("schema_extra", []))


# ============================================================
#  بناء الصفحة
# ============================================================

SECTIONS = [
    sec_hero,
    sec_subnav,
    sec_facts,
    sec_intro,
    sec_cards,
    sec_specs,
    sec_gallery,
    sec_cards2,
    sec_uses,
    sec_sectors,
    sec_process,
    sec_why,
    sec_related,
    sec_faq,
    sec_quote,
    sec_cta,
]


def render(p):
    ta, _ = pair(p["title"])
    da, _ = pair(p["desc"])
    url = f"{BASE}{p['slug']}.html"
    og = f"{BASE}{p['og_image']}"
    hero_img = p["hero"]["img"][0]
    body = "\n\n".join(filter(None, (f(p) for f in SECTIONS)))
    order = p.get("section_order")
    if order:
        fn = {f.__name__: f for f in SECTIONS}
        body = "\n\n".join(filter(None, (fn[n](p) for n in order)))
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl" data-default-lang="ar">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(ta)}</title>
  <meta name="description" content="{esc(da)}" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1" />
  <meta name="theme-color" content="#ffffff" />
  <link rel="icon" type="image/png" href="assets/img/favicon.png?v=2" />
  <link rel="preload" href="assets/fonts/ThmanyahSans-Black.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="preload" href="assets/fonts/ThmanyahSans-Bold.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="preload" href="{hero_img}" as="image" fetchpriority="high" />
  <link rel="stylesheet" href="assets/css/styles.css?v={CSS_V}" />
  <link rel="canonical" href="{url}" />
  <!-- Open Graph / Twitter -->
  <meta property="og:title" content="{esc(ta)}" />
  <meta property="og:description" content="{esc(da)}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{og}" />
  <meta property="og:image:alt" content="{esc(pair(p['hero']['img'][1])[0])}" />
  <meta property="og:site_name" content="رواد الليزر" />
  <meta property="og:locale" content="ar_SA" />
  <meta property="og:locale:alternate" content="en_US" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{esc(ta)}" />
  <meta name="twitter:description" content="{esc(da)}" />
  <meta name="twitter:image" content="{og}" />
  {ld_service(p)}
  {ld_breadcrumb(p)}
  {ld_faq(p)}
  {ld_extra(p)}
</head>
<body>

{SPRITE}

{HEADER}

{MENU}
{body}

{FOOTER}

{FAB}
<script src="assets/js/main.js?v={JS_V}" defer></script>
</body>
</html>
"""


def load_page(slug):
    path = os.path.join(PAGES_DIR, slug + ".py")
    spec = importlib.util.spec_from_file_location("page_" + slug.replace("-", "_"), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.PAGE


def main():
    slugs = sys.argv[1:]
    if not slugs:
        slugs = sorted(
            f[:-3] for f in os.listdir(PAGES_DIR) if f.endswith(".py") and not f.startswith("_")
        )
    for slug in slugs:
        p = load_page(slug)
        p.setdefault("slug", slug)
        out = os.path.join(SITE, p["slug"] + ".html")
        html_out = render(p)
        open(out, "w", encoding="utf-8").write(html_out)
        print(f"✓ {p['slug']}.html  ({len(html_out)/1024:.0f} KB)")


if __name__ == "__main__":
    main()
