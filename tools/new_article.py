#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مولّد مقالات مدونة رواد الليزر
================================
ينشئ صفحة مقال كاملة (بنفس تصميم الموقع + بيانات SEO)، ويضيف بطاقة المقال
في أعلى صفحة المدونة، ويحدّث خريطة الموقع sitemap.xml تلقائياً.

الاستخدام:
    python3 tools/new_article.py path/to/spec.json

ملف الـ spec عبارة عن JSON بالحقول التالية (انظر tools/spec-example.json):
    slug        : اسم الملف بدون امتداد، مثل "post13"
    title_ar    : عنوان المقال بالعربية (يظهر في H1 والبطاقة)
    title_en    : عنوان المقال بالإنجليزية
    page_title  : عنوان صفحة المتصفح (يفضّل "... | مدونة رواد الليزر")
    desc_ar     : وصف الميتا بالعربية (للسيو)
    tag_ar/tag_en : تصنيف المقال (مثل "أسعار" / "Pricing")
    date        : تاريخ ISO للسيو، مثل "2026-08-05"
    date_ar/date_en : التاريخ المعروض، مثل "5 أغسطس 2026" / "Aug 5, 2026"
    read_ar/read_en : مدة القراءة، مثل "5 دقائق قراءة" / "5 min read"
    excerpt_ar/excerpt_en : نص مختصر يظهر في بطاقة المدونة
    body_html   : محتوى المقال HTML (فقرات <p> و<h2> و<ul class="bullets"> ...)
                  كل عنصر يفضّل أن يحمل data-ar و data-en للّغتين.

ملاحظة: هذا السكربت لا يرفع للموقع تلقائياً. بعد تشغيله راجِع الناتج ثم:
    git add -A && git commit -m "مقال جديد" && git push
"""
import sys, os, re, json

DOMAIN = "https://rowadlaser.com"
LOGO = f"{DOMAIN}/assets/logos/logo-steel-trans-1100.png"
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)

def esc(s):
    return s.replace('&', '&amp;').replace('"', '&quot;')

def seo_block(url, page_title, desc, title_ar, date):
    t, d = esc(page_title), esc(desc)
    blog = {
        "@context": "https://schema.org", "@type": "BlogPosting",
        "headline": title_ar, "description": desc,
        "datePublished": date, "dateModified": date, "inLanguage": "ar",
        "author": {"@type": "Organization", "name": "رواد الليزر"},
        "publisher": {"@type": "Organization", "name": "رواد الليزر",
                      "logo": {"@type": "ImageObject", "url": LOGO}},
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
    }
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList",
              "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "الرئيسية", "item": f"{DOMAIN}/"},
                  {"@type": "ListItem", "position": 2, "name": "المدونة", "item": f"{DOMAIN}/blog.html"},
                  {"@type": "ListItem", "position": 3, "name": title_ar, "item": url}]}
    lines = [
        f'  <link rel="canonical" href="{url}" />',
        '  <!-- Open Graph / Twitter -->',
        f'  <meta property="og:title" content="{t}" />',
        f'  <meta property="og:description" content="{d}" />',
        '  <meta property="og:type" content="article" />',
        f'  <meta property="og:url" content="{url}" />',
        f'  <meta property="og:image" content="{LOGO}" />',
        '  <meta property="og:site_name" content="رواد الليزر" />',
        '  <meta property="og:locale" content="ar_SA" />',
        '  <meta name="twitter:card" content="summary_large_image" />',
        f'  <meta name="twitter:title" content="{t}" />',
        f'  <meta name="twitter:description" content="{d}" />',
        f'  <meta name="twitter:image" content="{LOGO}" />',
        '  <script type="application/ld+json">\n  ' + json.dumps(blog, ensure_ascii=False, indent=2).replace('\n', '\n  ') + '\n  </script>',
        '  <script type="application/ld+json">\n  ' + json.dumps(crumbs, ensure_ascii=False) + '\n  </script>',
    ]
    return "\n".join(lines) + "\n"

def build_top(s, url):
    top = open(os.path.join(HERE, "_top.html"), encoding="utf-8").read()
    top = re.sub(r'<title>.*?</title>', f'<title>{s["page_title"]}</title>', top, count=1, flags=re.S)
    top = re.sub(r'(<meta\s+name="description"\s+content=")[^"]*(")',
                 lambda m: m.group(1) + s["desc_ar"] + m.group(2), top, count=1)
    top = re.sub(r'\s*<link[^>]*rel="canonical"[^>]*>\s*', '\n', top)
    top = re.sub(r'\s*<meta[^>]*property="og:[^"]*"[^>]*>\s*', '\n', top)
    top = re.sub(r'\s*<meta[^>]*name="twitter:[^"]*"[^>]*>\s*', '\n', top)
    top = re.sub(r'\s*<script[^>]*application/ld\+json[^>]*>.*?</script>\s*', '\n', top, flags=re.S)
    top = re.sub(r'\s*<!--\s*Open Graph[^>]*-->\s*', '\n', top)
    top = re.sub(r'\n?</head>', '\n' + seo_block(url, s["page_title"], s["desc_ar"], s["title_ar"], s["date"]) + '</head>', top, count=1)
    return re.sub(r'\n{3,}', '\n\n', top)

def build_body(s):
    return f'''
<section class="page-hero">
  <div class="container" style="max-width:800px">
    <nav class="crumbs"><a href="index.html" data-ar="الرئيسية" data-en="Home">الرئيسية</a><svg><use href="#i-chev"/></svg><a href="blog.html" data-ar="المدونة" data-en="Blog">المدونة</a><svg><use href="#i-chev"/></svg><span data-ar="مقال" data-en="Article">مقال</span></nav>
    <div class="meta" style="color:var(--muted);font-family:var(--font-head);margin-bottom:10px" data-ar="{s['tag_ar']} · {s['date_ar']} · {s['read_ar']}" data-en="{s['tag_en']} · {s['date_en']} · {s['read_en']}">{s['tag_ar']} · {s['date_ar']} · {s['read_ar']}</div>
    <h1 data-ar="{esc(s['title_ar'])}" data-en="{esc(s['title_en'])}">{s['title_ar']}</h1>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <article class="article reveal">
      <div style="aspect-ratio:16/7;border-radius:var(--r-lg);background:linear-gradient(135deg,#eef1f5,#cfd6df 55%,#aeb7c2);margin-bottom:32px"></div>
{s['body_html']}
      <div style="margin-top:36px;padding:28px;border-radius:var(--r-lg);background:var(--paper-2);border:1px solid var(--line);text-align:center">
        <b style="font-family:var(--font-head);font-size:1.2rem;display:block;margin-bottom:8px" data-ar="جاهز لتنفيذ مشروعك؟" data-en="Ready to execute your project?">جاهز لتنفيذ مشروعك؟</b>
        <p style="color:var(--muted);margin-bottom:18px" data-ar="احصل على عرض سعر مجاني خلال وقت قصير." data-en="Get a free quote in no time.">احصل على عرض سعر مجاني خلال وقت قصير.</p>
        <a href="contact.html" class="btn btn-primary" data-ar="اطلب عرض سعر" data-en="Get a Quote">اطلب عرض سعر</a>
      </div>
    </article>
  </div>
</section>
'''

def blog_card(s):
    fn = s["slug"] + ".html"
    return (f'''      <a class="post reveal" href="{fn}">
        <div class="cover"><span class="tag" data-ar="{esc(s['tag_ar'])}" data-en="{esc(s['tag_en'])}">{s['tag_ar']}</span></div>
        <div class="body"><div class="meta" data-ar="{s['date_ar']} · {s['read_ar']}" data-en="{s['date_en']} · {s['read_en']}">{s['date_ar']} · {s['read_ar']}</div><h3 data-ar="{esc(s['title_ar'])}" data-en="{esc(s['title_en'])}">{s['title_ar']}</h3><p data-ar="{esc(s['excerpt_ar'])}" data-en="{esc(s['excerpt_en'])}">{s['excerpt_ar']}</p><span class="more" data-ar="اقرأ المقال" data-en="Read article">اقرأ المقال <svg><use href="#i-arrow"/></svg></span></div>
      </a>\n''')

def insert_blog_card(s):
    path = os.path.join(SITE, "blog.html")
    h = open(path, encoding="utf-8").read()
    if f'href="{s["slug"]}.html"' in h:
        print(f"  · بطاقة {s['slug']} موجودة مسبقاً في blog.html — تم التخطي")
        return
    marker = '<div class="grid grid-3">\n'
    h = h.replace(marker, marker + blog_card(s), 1)
    open(path, "w", encoding="utf-8").write(h)
    print("  · أُضيفت بطاقة المقال في أعلى blog.html")

def update_sitemap(s):
    path = os.path.join(SITE, "sitemap.xml")
    x = open(path, encoding="utf-8").read()
    loc = f"{DOMAIN}/{s['slug']}.html"
    if loc in x:
        print("  · الرابط موجود في sitemap.xml — تم التخطي")
        return
    entry = f'  <url><loc>{loc}</loc><lastmod>{s["date"]}</lastmod><priority>0.4</priority></url>\n'
    x = x.replace("</urlset>", entry + "</urlset>", 1)
    open(path, "w", encoding="utf-8").write(x)
    print("  · أُضيف الرابط إلى sitemap.xml")

def main():
    if len(sys.argv) < 2:
        print("الاستخدام: python3 tools/new_article.py spec.json"); sys.exit(1)
    s = json.load(open(sys.argv[1], encoding="utf-8"))
    required = ["slug","title_ar","title_en","page_title","desc_ar","tag_ar","tag_en",
                "date","date_ar","date_en","read_ar","read_en","excerpt_ar","excerpt_en","body_html"]
    missing = [k for k in required if k not in s]
    if missing:
        print("حقول ناقصة في الـ spec:", missing); sys.exit(1)
    url = f"{DOMAIN}/{s['slug']}.html"
    page = build_top(s, url) + build_body(s) + open(os.path.join(HERE, "_footer.html"), encoding="utf-8").read()
    out = os.path.join(SITE, s["slug"] + ".html")
    open(out, "w", encoding="utf-8").write(page)
    print(f"✓ أُنشئت صفحة المقال: {s['slug']}.html ({len(page)} bytes)")
    insert_blog_card(s)
    update_sitemap(s)
    print("تم. راجِع الناتج ثم ارفعه: git add -A && git commit && git push")

if __name__ == "__main__":
    main()
