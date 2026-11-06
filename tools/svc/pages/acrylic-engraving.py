# -*- coding: utf-8 -*-
"""الحفر على الأكريليك — تحت الحفر والنقش بالليزر"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _eng import ENG_PARENT, GALLERY_NOTE, g, hero_img, process  # noqa: E402

WA = "مرحباً رواد الليزر، أرغب في عرض سعر لحفر أو قص على أكريليك."

PAGE = {
    "slug": "acrylic-engraving",
    "parent": ENG_PARENT,
    "crumb": ("الحفر على الأكريليك", "Acrylic engraving"),
    "title": (
        "حفر ليزر على الأكريليك في جدة | لوحات ودروع أكريليك محفورة — رواد الليزر",
        "Laser Engraving on Acrylic in Jeddah | Engraved Acrylic Plaques &amp; Awards — Ruwwad Laser",
    ),
    "desc": (
        "حفر وقص الأكريليك بالليزر في جدة: لوحات استقبال ومكاتب بفواصل معدنية، دروع تكريم أكريليك، لوحات عيادات، بادجات وتسميات — حفر مثلّج أنيق على أكريليك شفاف أو ملوّن، وقص بأي شكل. بدء التنفيذ خلال 6 ساعات.",
        "Acrylic laser engraving and cutting in Jeddah: reception and office plaques with metal standoffs, acrylic awards, clinic signs, badges and labels — elegant frosted engraving on clear or coloured acrylic, cut to any shape. Production starts within 6 hours.",
    ),
    "og_image": "assets/img/svc/tags-reception.jpg",
    "service_type": ("حفر وقص الأكريليك بالليزر", "Acrylic laser engraving and cutting"),
    "schema_name": ("الحفر بالليزر على الأكريليك في جدة", "Laser engraving on acrylic in Jeddah"),
    "schema_desc": (
        "حفر وقص الأكريليك بليزر CO2 في جدة: لوحات استقبال ومكاتب وعيادات، دروع ولوحات تكريم، لوحات إرشادية، بادجات وتسميات، وقطع أكريليك بأشكال مخصصة، على الأكريليك الشفاف والملون والمرآة.",
        "CO2 laser engraving and cutting of acrylic in Jeddah: reception, office and clinic plaques, awards and recognition plates, signage, badges and labels, and custom-shaped acrylic pieces, on clear, coloured and mirror acrylic.",
    ),
    "schema_offers": [
        ("لوحات أكريليك بفواصل معدنية", "Acrylic plaques with standoffs"),
        ("دروع تكريم أكريليك", "Acrylic awards"),
        ("قص أكريليك بالليزر", "Acrylic laser cutting"),
        ("لوحات وتسميات أكريليك", "Acrylic signs and labels"),
    ],
    "hero": {
        "eyebrow": ("أكريليك · ليزر CO2", "Acrylic · CO2 laser"),
        "h1": ("حفر وقص الأكريليك بالليزر", "Acrylic laser engraving and cutting"),
        "sub": (
            "الأكريليك يعطي لوحاتك مظهراً عصرياً شفافاً يليق بالاستقبال والمكاتب والعيادات. الليزر يحفر عليه نقشاً مثلّجاً أبيض أنيقاً، ويقصّه بحواف لامعة كالزجاج بأي شكل تريده — لوحات بفواصل معدنية، دروع تكريم، وبادجات.",
            "Acrylic gives your signs a modern, transparent look that suits reception areas, offices and clinics. The laser engraves an elegant frosted-white mark and cuts it with glass-like polished edges in any shape — standoff plaques, awards and badges.",
        ),
        "chips": [
            ("حفر مثلّج أنيق", "Elegant frosted engraving", "engrave"),
            ("حواف لامعة كالزجاج", "Glass-like polished edges", "check"),
            ("شفاف · ملوّن · مرآة", "Clear · coloured · mirror", "layers"),
            ("قص بأي شكل", "Cut to any shape", "cut"),
        ],
        "img": ("assets/img/svc/tags-reception.jpg", ("لوحة استقبال من الأكريليك الأسود اللامع بجانب لوحة ستانلس", "Glossy black acrylic reception plate beside a stainless plate"), 1200, 900),
        "wa": WA,
    },
    "facts": [
        (("3 – 20 mm", "3 – 20 mm"), ("سماكات الأكريليك الشائعة", "Common acrylic thicknesses")),
        (("+10", "+10"), ("ألوان أكريليك متاحة", "Acrylic colours available")),
        (("0", "0"), ("تشطيب إضافي للحواف — تخرج لامعة", "Extra edge finishing — edges come out polished")),
        (("6", "6"), ("ساعات لبدء التنفيذ", "Hours to start production")),
    ],
    "intro": {
        "h2": ("لماذا الأكريليك والليزر ثنائي مثالي؟", "Why acrylic and laser are a perfect pair"),
        "paras": [
            (
                "الأكريليك المصبوب (Cast) يتفاعل مع ليزر CO2 بطريقة مميزة: عند الحفر يتحول السطح إلى لون أبيض مثلّج يشبه الزجاج المصنفر، وعند القص تذوب الحافة وتبرد لامعة وشفافة دون حاجة لأي تلميع. لهذا تبدو لوحات ودروع الأكريليك المصنوعة بالليزر فاخرة رغم أن تكلفتها معقولة.",
                "Cast acrylic reacts with a CO2 laser in a distinctive way: engraving turns the surface frosted white like sandblasted glass, and cutting melts the edge so it cools glossy and clear with no polishing needed. That's why laser-made acrylic plaques and awards look premium at a reasonable cost.",
            ),
            (
                "ويمكن الحفر من الخلف (Reverse Engraving) على الأكريليك الشفاف ثم تلوين الحفر، فيظهر التصميم من الأمام محمياً تحت طبقة الأكريليك ولا يُخدش أبداً — وهي طريقة شائعة للوحات الاستقبال والشعارات.",
                "Clear acrylic can also be engraved from the back (reverse engraving) and the engraving colour-filled, so the design shows from the front protected under the acrylic and can never scratch — a common technique for reception signs and logos.",
            ),
        ],
        "h3": ("أشهر استخدامات الأكريليك المحفور", "Most popular uses of engraved acrylic"),
        "bullets": [
            ("لوحات الاستقبال والشعارات خلف مكتب الاستقبال بفواصل معدنية.", "Reception signs and logos behind the front desk on metal standoffs."),
            ("لوحات المكاتب والعيادات وأرقام الغرف بمظهر عصري.", "Office and clinic signs and room numbers with a modern look."),
            ("دروع التكريم وجوائز المناسبات والموظف المثالي.", "Recognition awards, event trophies and employee-of-the-month plaques."),
            ("حوامل المنيو، لوحات الطاولات، وقطع العرض في المطاعم والمحلات.", "Menu holders, table signs and display pieces in restaurants and shops."),
        ],
    },
    "cards": {
        "eyebrow": ("الطلبات الشائعة", "Common requests"),
        "h2": ("ماذا نصنع من الأكريليك؟", "What we make in acrylic"),
        "items": [
            {"icon": "store", "h3": ("لوحات الاستقبال", "Reception signs"), "p": ("شعار الشركة على أكريليك شفاف أو ملوّن بفواصل معدنية.", "Company logo on clear or coloured acrylic with metal standoffs.")},
            {"icon": "target", "h3": ("دروع التكريم", "Awards"), "p": ("دروع بأشكال مخصصة وقاعدة، بالاسم والمناسبة والتاريخ.", "Custom-shaped awards with base, name, occasion and date.")},
            {"icon": "user", "h3": ("لوحات المكاتب والعيادات", "Office and clinic signs"), "p": ("رقم الغرفة واسم الطبيب أو القسم بنقش مثلّج.", "Room number and doctor or department name in frosted engraving."), "href": "signage-plates.html", "more": ("اللوحات الإرشادية", "Signage plates")},
            {"icon": "file", "h3": ("لوحات معلومات", "Information signs"), "p": ("لوحات إرشادات وأوقات عمل ورموز QR للمحلات.", "Notices, opening hours and QR code signs for shops.")},
            {"icon": "cut", "h3": ("قص أكريليك بالشكل", "Acrylic cut to shape"), "p": ("حروف وشعارات وقطع ديكور مقصوصة بحواف لامعة.", "Letters, logos and décor pieces cut with polished edges.")},
            {"icon": "layers", "h3": ("بادجات وتسميات", "Badges and labels"), "p": ("بادجات أكريليك خفيفة وتسميات منتجات.", "Light acrylic badges and product labels."), "href": "name-badges.html", "more": ("بادجات الأسماء", "Name badges")},
        ],
    },
    "specs": {
        "soft": True,
        "eyebrow": ("الأنواع", "Types"),
        "h2": ("أنواع الأكريليك ونتيجة الحفر", "Acrylic types and engraving result"),
        "cols": [("النوع", "Type"), ("نتيجة الحفر", "Result"), ("الأنسب لـ", "Best for")],
        "rows": [
            [("شفاف مصبوب", "Clear cast"), ("نقش أبيض مثلّج واضح", "Clear frosted-white mark"), ("لوحات الاستقبال والدروع", "Reception signs and awards")],
            [("ملوّن معتم", "Opaque coloured"), ("نقش بلون أفتح من السطح", "A lighter-tone mark"), ("اللوحات الإرشادية والشعارات", "Signage and logos")],
            [("مرآة ذهبي / فضي", "Gold / silver mirror"), ("حفر يكشف الطبقة أو قص بالشكل", "Engraving reveals the layer or cut to shape"), ("الديكور والشعارات الفاخرة", "Décor and premium logos")],
            [("أكريليك مصنفر (Frosted)", "Frosted acrylic"), ("مظهر ناعم مطفي", "Soft matte look"), ("لوحات العيادات والمكاتب", "Clinic and office signs")],
            [("حفر خلفي + تلوين", "Reverse engraved + colour"), ("تصميم ملوّن محمي لا يُخدش", "Protected coloured design that can't scratch"), ("الشعارات واللوحات الدائمة", "Logos and permanent signs")],
        ],
    },
    "gallery": {
        "eyebrow": ("نماذج", "Samples"),
        "h2": ("الأكريليك المحفور", "Engraved acrylic"),
        "items": [
            ("assets/img/svc/tags-office-signs.jpg", ("لوحات مكاتب من الأكريليك والمعدن", "Office plates in acrylic and metal"), ("لوحات المكاتب", "Office plates"), 1200, 900),
            ("assets/img/svc/tags-reception-2.jpg", ("لوحتا استقبال بالفضي والأسود", "Reception plates in silver and black"), ("استقبال", "Reception"), 1200, 655),
            g("ill-acrylic-engraving", ("لوحات ودروع أكريليك شفافة محفورة", "Engraved clear acrylic plaques and awards"), ("أكريليك شفاف", "Clear acrylic")),
        ],
        "note": GALLERY_NOTE,
    },
    "process": process(),
    "related": {
        "eyebrow": ("مواد أخرى", "Other materials"),
        "h2": ("خيارات أخرى", "Other options"),
        "items": [
            {"icon": "target", "href": "brass-engraving.html", "h3": ("الحفر على البراص", "Brass engraving"), "p": ("لوحات ودروع ذهبية فاخرة.", "Premium golden plaques and awards.")},
            {"icon": "cube", "href": "pvc-abs-engraving.html", "h3": ("لوحات PVC وABS", "PVC and ABS signs"), "p": ("خيار اقتصادي للكميات الكبيرة.", "An economical option for large quantities.")},
            {"icon": "store", "href": "metal-facades-signage.html", "h3": ("الواجهات واللوحات المعدنية", "Metal facades and signage"), "p": ("لوحات المحلات والحروف المعدنية.", "Shop signs and metal letters.")},
        ],
    },
    "faq": [
        {
            "q": ("هل يمكن حفر شعار ملوّن على الأكريليك؟", "Can a coloured logo be engraved on acrylic?"),
            "a": (
                "نعم بطريقتين: الحفر من الخلف ثم تعبئة الحفر بألوان الشعار، أو تثبيت طبقة أكريليك ملوّنة مقصوصة بشكل الشعار فوق لوحة شفافة.",
                "Yes, in two ways: reverse engraving then filling it with the logo colours, or fixing a coloured acrylic layer cut in the logo's shape on top of a clear plate.",
            ),
        },
        {
            "q": ("ما السماكة المناسبة للوحة الاستقبال؟", "What thickness suits a reception sign?"),
            "a": (
                "للوحات الجدارية بفواصل معدنية نرشّح 8 – 10 مم لمظهر فاخر ومتين، وللوحات الأبواب الصغيرة 3 – 5 مم، وللدروع 10 – 15 مم.",
                "For wall signs on standoffs we recommend 8–10 mm for a premium, sturdy look; 3–5 mm for small door signs; and 10–15 mm for awards.",
            ),
        },
        {
            "q": ("هل يتأثر الأكريليك بالشمس؟", "Is acrylic affected by sun?"),
            "a": (
                "الأكريليك الجيد مقاوم للاصفرار ويصلح لكثير من الاستخدامات شبه الخارجية، لكن الحرارة الشديدة والشمس المباشرة لسنوات قد تؤثر عليه. للواجهات الخارجية الدائمة نرشّح المعدن.",
                "Good acrylic resists yellowing and suits many semi-outdoor uses, but extreme heat and years of direct sun can affect it. For permanent outdoor facades we recommend metal.",
            ),
        },
        {
            "q": ("هل توفرون الفواصل المعدنية للتثبيت؟", "Do you supply the metal standoffs?"),
            "a": (
                "نعم، نوفّر فواصل ستانلس أو ذهبية أو سوداء بأطوال مختلفة، ونجهّز الثقوب في اللوحة بمكانها الصحيح.",
                "Yes, we supply stainless, gold or black standoffs in different lengths and drill the holes in the right positions.",
            ),
        },
    ],
    "form_services": [
        ("لوحة استقبال أكريليك", "Acrylic reception sign"),
        ("دروع تكريم أكريليك", "Acrylic awards"),
        ("لوحات مكاتب وعيادات", "Office and clinic signs"),
        ("قص أكريليك بالشكل", "Acrylic cut to shape"),
        ("أخرى / غير متأكد", "Other / not sure"),
    ],
    "form_wa": WA,
    "quote_h2": ("أرسل التصميم أو الشعار", "Send your design or logo"),
    "quote_lead": (
        "اذكر المقاس والسماكة واللون (شفاف أو ملوّن) والكمية.",
        "Tell us the size, thickness, colour (clear or coloured) and quantity.",
    ),
    "cta": {
        "h2": ("أكريليك أنيق يعكس هويتك", "Elegant acrylic that reflects your brand"),
        "p": ("أرسل التصميم، وتصلك معاينة وعرض سعر في نفس يوم العمل غالباً.", "Send the design and usually get a proof and quote the same working day."),
        "wa": WA,
    },
}
