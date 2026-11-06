# -*- coding: utf-8 -*-
"""لوحات المسارات (Route Marker Plates) — تحت اللوحات والتاقات التعريفية"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _eng import GALLERY_NOTE, TAGS_PARENT, g, hero_img, process  # noqa: E402

WA = "مرحباً رواد الليزر، أرغب في عرض سعر للوحات مسارات (Route Markers) محفورة."

PAGE = {
    "slug": "route-marker-plates",
    "parent": TAGS_PARENT,
    "crumb": ("لوحات المسارات", "Route marker plates"),
    "title": (
        "لوحات مسارات الكيابل والأنابيب في جدة | Route Markers براص وستانلس — رواد الليزر",
        "Route Marker Plates in Jeddah | Brass &amp; Stainless Cable and Pipe Markers — Ruwwad Laser",
    ),
    "desc": (
        "لوحات وعلامات مسارات الخدمات المدفونة في جدة: علامات أرضية من البراص والستانلس لمسارات الكيابل والمياه والغاز والاتصالات، محفورة بالنوع والاتجاه. لمشاريع البنية التحتية والمجمعات والمصانع.",
        "Route marker plates for buried services in Jeddah: brass and stainless ground markers for cable, water, gas and telecom routes, engraved with service type and direction. For infrastructure projects, compounds and plants.",
    ),
    "og_image": "assets/img/svc/tags-route-ground.jpg",
    "service_type": ("لوحات مسارات الخدمات المدفونة", "Buried service route markers"),
    "schema_name": ("لوحات المسارات في جدة", "Route marker plates in Jeddah"),
    "schema_desc": (
        "تصنيع لوحات وعلامات مسارات الخدمات المدفونة في جدة: علامات أرضية دائرية ومستطيلة من البراص والستانلس ستيل محفورة بنوع الخدمة (كهرباء، مياه، غاز، اتصالات، صرف) وسهم الاتجاه، تُثبت في الخرسانة أو الأسفلت أو على الجدران.",
        "Manufacture of buried service route markers in Jeddah: round and rectangular brass and stainless ground markers engraved with service type (power, water, gas, telecom, drainage) and direction arrow, fixed into concrete, asphalt or walls.",
    ),
    "schema_offers": [
        ("علامات مسارات الكيابل", "Cable route markers"),
        ("علامات مسارات المياه والغاز", "Water and gas route markers"),
        ("علامات براص أرضية", "Brass ground markers"),
        ("لوحات اتجاه ومسارات جدارية", "Wall-mounted route plates"),
    ],
    "hero": {
        "eyebrow": ("Route Markers · بنية تحتية", "Route markers · infrastructure"),
        "h1": ("لوحات مسارات الكيابل والأنابيب المدفونة", "Route markers for buried cables and pipes"),
        "sub": (
            "قبل أي حفر في الموقع، يجب أن يعرف الجميع ما الذي تحت الأرض. نصنع علامات المسارات من البراص والستانلس، محفورة بنوع الخدمة وسهم الاتجاه، لتُثبَّت في الأرضيات والأرصفة والجدران وتبقى ظاهرة لسنوات.",
            "Before any digging on site, everyone must know what lies underground. We make route markers in brass and stainless, engraved with the service type and a direction arrow, to be set in floors, pavements and walls and stay visible for years.",
        ),
        "chips": [
            ("براص وستانلس", "Brass and stainless", "layers"),
            ("أسهم الاتجاه والتفرّع", "Direction and branch arrows", "arrow"),
            ("تثبيت أرضي أو جداري", "Ground or wall fixing", "build"),
            ("عربي + إنجليزي", "Arabic + English", "globe"),
        ],
        "img": ("assets/img/svc/tags-route-ground.jpg", ("علامة مسار كيبل كهرباء أرضية مثبّتة في الخرسانة", "Electric cable ground route marker fixed in concrete"), 1200, 900),
        "wa": WA,
    },
    "facts": [
        (("75–100 mm", "75–100 mm"), ("أقطار العلامات الأرضية الشائعة", "Common ground marker diameters")),
        (("5", "5"), ("خدمات: كهرباء، مياه، غاز، اتصالات، صرف", "Services: power, water, gas, telecom, drainage")),
        (("0", "0"), ("صدأ مع البراص والستانلس", "Rust with brass and stainless")),
        (("6", "6"), ("ساعات لبدء التنفيذ", "Hours to start production")),
    ],
    "intro": {
        "h2": ("لماذا تُستخدم لوحات المسارات؟", "Why route markers are used"),
        "paras": [
            (
                "الكيابل والأنابيب المدفونة لا تُرى بعد ردم الحفريات وتشطيب الأرضيات. وعند أي أعمال لاحقة — توسعة، صيانة، أو تركيب جديد — يصبح الحفر العشوائي خطراً حقيقياً: قطع كيبل جهد عالٍ أو خط غاز قد يسبب حادثاً وخسائر كبيرة.",
                "Buried cables and pipes become invisible once trenches are backfilled and floors finished. During any later works — expansion, maintenance or new installation — blind digging becomes a real hazard: cutting a high-voltage cable or a gas line can cause an accident and heavy losses.",
            ),
            (
                "علامات المسارات تحل هذه المشكلة: تُثبَّت على سطح الأرض فوق المسار على مسافات منتظمة وعند كل انعطاف أو تفرّع، وتحمل نوع الخدمة وسهماً يوضح الاتجاه. ولأنها تُداس وتتعرض للشمس والأمطار، نصنعها من البراص أو الستانلس مع حفر عميق.",
                "Route markers solve this: they are set on the surface above the route at regular intervals and at every bend or branch, carrying the service type and an arrow showing direction. Since they are walked on and exposed to sun and rain, we make them in brass or stainless with deep engraving.",
            ),
        ],
        "h3": ("ما الذي يُحفر على علامة المسار؟", "What goes on a route marker?"),
        "bullets": [
            ("نوع الخدمة: كيبل كهرباء، جهد عالٍ، مياه، غاز، اتصالات، صرف، ري.", "Service type: power cable, high voltage, water, gas, telecom, drainage, irrigation."),
            ("سهم الاتجاه: مستقيم، انعطاف، تفرّع (T)، أو نهاية المسار.", "Direction arrow: straight, bend, tee branch or end of route."),
            ("رمز الخدمة واسم الجهة المالكة أو رقم المشروع إن لزم.", "Service symbol and owner name or project number if needed."),
            ("تحذير مختصر: «لا تحفر — كيبل تحت الأرض» بالعربي والإنجليزي.", "A short warning: “Do not dig — cable below” in Arabic and English."),
        ],
    },
    "cards": {
        "eyebrow": ("الأنواع", "Types"),
        "h2": ("أنواع علامات المسارات", "Route marker types"),
        "items": [
            {"icon": "target", "h3": ("علامة أرضية دائرية", "Round ground marker"), "p": ("قرص براص أو ستانلس بساق تثبيت يُغرس في الخرسانة أو الأسفلت.", "Brass or stainless disc with a stem set into concrete or asphalt.")},
            {"icon": "layers", "h3": ("لوحة مستطيلة", "Rectangular plate"), "p": ("تُثبَّت بالبراغي على الأرصفة أو قواعد الخرسانة.", "Screwed to pavements or concrete plinths.")},
            {"icon": "build", "h3": ("لوحة جدارية", "Wall plate"), "p": ("على الجدران والأسوار حيث يمر المسار بجانبها.", "On walls and fences where the route runs alongside.")},
            {"icon": "arrow", "h3": ("لوحات الاتجاه الداخلية", "Indoor route plates"), "p": ("مسارات المواقف والمخارج والمرافق داخل المجمعات.", "Routes to parking, exits and facilities inside compounds."), "href": "signage-plates.html", "more": ("اللوحات الإرشادية", "Signage plates")},
            {"icon": "bolt", "h3": ("كيابل الجهد العالي", "High-voltage cables"), "p": ("علامات واضحة بتحذير مزدوج لمسارات الجهد العالي.", "Clear markers with a double warning for HV routes.")},
            {"icon": "shield", "h3": ("الغاز والمياه", "Gas and water"), "p": ("لون ورمز مختلف لكل خدمة لتفادي الالتباس.", "A different colour and symbol per service to avoid confusion.")},
        ],
    },
    "specs": {
        "soft": True,
        "eyebrow": ("المادة", "Material"),
        "h2": ("براص أم ستانلس؟", "Brass or stainless?"),
        "cols": [("المادة", "Material"), ("المميزات", "Advantages"), ("الأنسب لـ", "Best for")],
        "rows": [
            [("براص", "Brass"), ("لا يصدأ، يغمق بلون طبيعي، الحفر يبقى واضحاً", "Rust-free, darkens naturally, engraving stays clear"), ("الأرصفة والطرق والمواقع الخارجية", "Pavements, roads and outdoor sites")],
            [("ستانلس 316", "Stainless 316"), ("الأقوى ضد الملوحة، مظهر عصري", "Strongest against salt, modern look"), ("المناطق الساحلية والمصانع", "Coastal areas and plants")],
            [("ألمنيوم", "Aluminium"), ("خفيف واقتصادي", "Light and economical"), ("اللوحات الجدارية والداخلية", "Wall and indoor plates")],
        ],
        "note": (
            "للعلامات الأرضية نرشّح حفراً عميقاً حتى يبقى النص مقروءاً رغم الاحتكاك والمشي عليه.",
            "For ground markers we recommend deep engraving so the text stays legible despite foot traffic and abrasion.",
        ),
    },
    "gallery": {
        "eyebrow": ("نماذج", "Samples"),
        "h2": ("علامات المسارات واللوحات المعدنية", "Route markers and metal plates"),
        "items": [
            ("assets/img/svc/tags-route-markers.jpg", ("علامات مسارات براص وستانلس للمياه والغاز والكهرباء والصرف", "Brass and stainless route markers for water, gas, electric and sewer lines"), ("براص وستانلس", "Brass and stainless"), 1200, 900),
            ("assets/img/svc/tags-route-markers-2.jpg", ("علامات مسارات دائرية مع أسهم الاتجاه", "Round route markers with direction arrows"), ("أسهم الاتجاه", "Direction arrows"), 1200, 670),
        ],
        "note": GALLERY_NOTE,
    },
    "process": process(("من مخطط المسارات إلى العلامات", "From the route drawing to the markers")),
    "related": {
        "eyebrow": ("للمشروع نفسه", "For the same project"),
        "h2": ("منتجات تعريف مكمّلة", "Complementary identification"),
        "items": [
            {"icon": "bolt", "href": "cable-id-tags.html", "h3": ("تاقات الكيابل", "Cable ID tags"), "p": ("تعريف الكيبل نفسه عند طرفيه وداخل غرف التفتيش.", "Identifying the cable at both ends and inside manholes.")},
            {"icon": "sliders", "href": "valve-tags.html", "h3": ("تاقات المحابس", "Valve tags"), "p": ("ترقيم المحابس على خطوط المياه والغاز.", "Numbering valves on water and gas lines.")},
            {"icon": "engrave", "href": "brass-engraving.html", "h3": ("الحفر على البراص", "Brass engraving"), "p": ("المادة الكلاسيكية للعلامات الخارجية.", "The classic material for outdoor markers.")},
        ],
    },
    "faq": [
        {
            "q": ("كيف تُثبّت العلامات الأرضية؟", "How are ground markers installed?"),
            "a": (
                "العلامة الدائرية تأتي بساق أسفلها تُغرس في ثقب بالخرسانة أو الأسفلت مع مادة لاصقة إيبوكسي، أو تُثبّت ببراغي على السطح. نحدد نوع التثبيت حسب سطح الموقع.",
                "The round marker comes with a stem underneath set into a hole in concrete or asphalt with epoxy, or it is screwed to the surface. We choose the fixing to suit the site surface.",
            ),
        },
        {
            "q": ("كم علامة يحتاج المسار؟", "How many markers does a route need?"),
            "a": (
                "يُحدد ذلك عادة في مواصفات المشروع أو اشتراطات الجهة المالكة للخدمة: علامة على مسافات منتظمة، وعند كل انعطاف وتفرّع ونقطة دخول للمبنى. أرسل المخطط ونقترح العدد والأسهم المطلوبة.",
                "This is usually set by the project specification or the utility owner: a marker at regular intervals and at every bend, branch and building entry. Send the drawing and we propose the count and arrows needed.",
            ),
        },
        {
            "q": ("هل يمكن إضافة شعار الجهة أو رقم المشروع؟", "Can the owner's logo or project number be added?"),
            "a": (
                "نعم، يُحفر الشعار أو رقم المشروع أو رقم الهاتف للطوارئ على العلامة إلى جانب نوع الخدمة والسهم.",
                "Yes, the logo, project number or emergency phone number can be engraved alongside the service type and arrow.",
            ),
        },
        {
            "q": ("هل يتغير لون البراص مع الوقت؟", "Does brass change colour over time?"),
            "a": (
                "نعم، يكتسب البراص طبقة داكنة طبيعية (باتينا) تحميه، لكن الحفر العميق يبقى واضحاً. إن كنت تفضّل لوناً ثابتاً فالستانلس 316 هو الخيار.",
                "Yes, brass develops a natural dark patina that protects it, but deep engraving stays clear. If you prefer a constant colour, stainless 316 is the choice.",
            ),
        },
    ],
    "form_services": [
        ("علامات أرضية براص", "Brass ground markers"),
        ("علامات أرضية ستانلس", "Stainless ground markers"),
        ("لوحات مسارات جدارية", "Wall route plates"),
        ("أخرى / غير متأكد", "Other / not sure"),
    ],
    "form_wa": WA,
    "quote_h2": ("أرسل مخطط المسارات أو القائمة", "Send the route drawing or list"),
    "quote_lead": (
        "اذكر أنواع الخدمات والعدد والمادة المفضلة وطريقة التثبيت.",
        "Tell us the service types, count, preferred material and fixing method.",
    ),
    "cta": {
        "h2": ("اعرف ما تحت الأرض قبل الحفر", "Know what's underground before you dig"),
        "p": ("أرسل التفاصيل، وتصلك معاينة وعرض سعر في نفس يوم العمل غالباً.", "Send the details and usually get a proof and quote the same working day."),
        "wa": WA,
    },
}
