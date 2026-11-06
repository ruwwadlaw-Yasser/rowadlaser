# -*- coding: utf-8 -*-
"""الحفر بالليزر على البراص والنحاس — تحت الحفر والنقش بالليزر"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _eng import ENG_PARENT, GALLERY_NOTE, g, hero_img, process  # noqa: E402

WA = "مرحباً رواد الليزر، أرغب في عرض سعر لحفر بالليزر على براص أو نحاس."

PAGE = {
    "slug": "brass-engraving",
    "parent": ENG_PARENT,
    "crumb": ("الحفر على البراص والنحاس", "Brass and copper engraving"),
    "title": (
        "حفر ليزر على البراص والنحاس في جدة | لوحات ودروع ذهبية محفورة — رواد الليزر",
        "Laser Engraving on Brass &amp; Copper in Jeddah | Engraved Brass Plaques — Ruwwad Laser",
    ),
    "desc": (
        "حفر بالليزر على البراص (النحاس الأصفر) والنحاس في جدة: لوحات أسماء فاخرة، دروع تكريم، لوحات فلل ومكاتب، تاقات محابس، ولوحات بيانات — حفر غائر مع تعبئة لون أسود. بدء التنفيذ خلال 6 ساعات.",
        "Laser engraving on brass and copper in Jeddah: premium name plaques, recognition awards, villa and office plates, valve tags and data plates — recessed engraving with black colour fill. Production starts within 6 hours.",
    ),
    "og_image": "assets/img/svc/tags-brass-plaques.jpg",
    "service_type": ("حفر ليزر على البراص والنحاس", "Laser engraving on brass and copper"),
    "schema_name": ("الحفر بالليزر على البراص والنحاس في جدة", "Laser engraving on brass and copper in Jeddah"),
    "schema_desc": (
        "حفر ونقش بالفايبر ليزر على البراص والنحاس في جدة: لوحات أسماء ومداخل فاخرة، دروع ولوحات تكريم، تاقات محابس، لوحات بيانات، وهدايا معدنية، بحفر غائر يمكن تعبئته باللون الأسود لتباين أعلى.",
        "Fibre laser engraving on brass and copper in Jeddah: premium name and entrance plaques, awards and recognition plates, valve tags, data plates and metal gifts, with recessed engraving that can be colour-filled black for higher contrast.",
    ),
    "schema_offers": [
        ("لوحات براص محفورة", "Engraved brass plaques"),
        ("دروع ولوحات تكريم", "Awards and recognition plates"),
        ("تاقات محابس براص", "Brass valve tags"),
        ("حفر على النحاس الأحمر", "Copper engraving"),
    ],
    "hero": {
        "eyebrow": ("براص · نحاس · حفر بالليزر", "Brass · copper · laser engraving"),
        "h1": ("حفر بالليزر على البراص والنحاس", "Laser engraving on brass and copper"),
        "sub": (
            "البراص يعطي اللوحة حضوراً فاخراً لا تعطيه أي مادة أخرى. نحفر عليه لوحات الأسماء والمداخل ودروع التكريم وتاقات المحابس بحفر غائر نظيف، ونعبّئه باللون الأسود عند الحاجة ليبرز النص على اللمعة الذهبية.",
            "Brass gives a plate a premium presence no other material can. We engrave name and entrance plaques, awards and valve tags with clean recessed engraving, colour-filled black when needed so text stands out on the golden shine.",
        ),
        "chips": [
            ("مظهر ذهبي فاخر", "Premium golden look", "target"),
            ("حفر غائر + تعبئة لون", "Recessed + colour fill", "engrave"),
            ("لا يصدأ", "Rust-free", "shield"),
            ("تعبئة لون أسود", "Black colour fill", "check"),
        ],
        "img": ("assets/img/svc/tags-brass-plaques.jpg", ("درع تكريم براص ولوحة فيلا وتاق براص محفورة بالليزر", "Laser engraved brass award plaque, villa plate and brass tag"), 1200, 900),
        "wa": WA,
    },
    "facts": [
        (("2", "2"), ("معدنان: براص ونحاس أحمر", "Two metals: brass and copper")),
        (("0", "0"), ("صدأ — يغمق بشكل طبيعي فقط", "Rust — only a natural patina")),
        (("0.2 mm", "0.2 mm"), ("أدق تفاصيل في الشعارات", "Finest logo detail")),
        (("6", "6"), ("ساعات لبدء التنفيذ", "Hours to start production")),
    ],
    "intro": {
        "h2": ("الحفر على البراص: فخامة تدوم", "Brass engraving: lasting elegance"),
        "paras": [
            (
                "البراص (النحاس الأصفر) سبيكة من النحاس والزنك، لونها ذهبي دافئ ولا تصدأ. لهذا تُستخدم منذ عقود في لوحات المداخل والمكاتب الفاخرة ودروع التكريم وتاقات المحابس التقليدية.",
                "Brass is a copper-zinc alloy with a warm golden colour that doesn't rust. That's why it has been used for decades in entrance and executive plaques, recognition awards and traditional valve tags.",
            ),
            (
                "البراص والنحاس يعكسان ضوء الليزر أكثر من الستانلس، لذلك نستخدم معهما الحفر الغائر بدلاً من النقش السطحي الأسود. وللحصول على أعلى تباين، نعبّئ الحفر بلون أسود أو أي لون آخر بعد التنفيذ، ثم نلمّع السطح فيبقى النص داكناً واضحاً على الذهبي.",
                "Brass and copper reflect laser light more than stainless, so we use recessed engraving rather than black surface marking. For maximum contrast we fill the engraving with black or another colour afterwards, then polish the surface so the text stays dark and clear on gold.",
            ),
        ],
        "h3": ("متى تختار البراص؟", "When to choose brass?"),
        "bullets": [
            ("لوحات المداخل والفلل ومكاتب الإدارة حيث يهمّ الانطباع الأول.", "Entrance, villa and executive office plaques where first impressions matter."),
            ("دروع ولوحات التكريم والشكر في المناسبات والشركات.", "Awards and appreciation plaques for events and companies."),
            ("تاقات المحابس وعلامات المسارات بمظهرها التقليدي المعروف.", "Valve tags and route markers in their familiar traditional look."),
            ("الهدايا الشخصية والمنتجات الحرفية الفاخرة.", "Personal gifts and premium crafted products."),
        ],
    },
    "cards": {
        "eyebrow": ("الطلبات الشائعة", "Common requests"),
        "h2": ("ماذا نحفر على البراص؟", "What we engrave on brass"),
        "items": [
            {"icon": "store", "h3": ("لوحات المداخل والفلل", "Entrance and villa plaques"), "p": ("اسم العائلة أو رقم الفيلا بحفر فاخر.", "Family name or villa number in premium engraving."), "href": "signage-plates.html", "more": ("اللوحات الإرشادية", "Signage plates")},
            {"icon": "user", "h3": ("لوحات المكاتب", "Office plates"), "p": ("اسم المدير ومسمّاه على لوحة براص مصقولة.", "The manager's name and title on polished brass.")},
            {"icon": "target", "h3": ("دروع التكريم", "Recognition awards"), "p": ("لوحات شكر وتقدير ودروع مناسبات بشعار الجهة.", "Appreciation plaques and event awards with the organisation's logo.")},
            {"icon": "sliders", "h3": ("تاقات المحابس", "Valve tags"), "p": ("أقراص براص مرقّمة بحفر غائر لا يُمحى.", "Numbered brass discs with indelible recessed engraving."), "href": "valve-tags.html", "more": ("تاقات المحابس", "Valve tags")},
            {"icon": "file", "h3": ("لوحات البيانات", "Data plates"), "p": ("لوحات معدات بمظهر كلاسيكي للمعدات الفاخرة.", "Classic-look plates for premium equipment.")},
            {"icon": "engrave", "h3": ("هدايا وحِرف", "Gifts and crafts"), "p": ("أقلام، علب، لوحات تذكارية بأسماء أو آيات أو تواريخ.", "Pens, boxes and keepsake plates with names, verses or dates.")},
        ],
    },
    "specs": {
        "soft": True,
        "eyebrow": ("الخيارات", "Options"),
        "h2": ("التشطيبات وطرق الحفر", "Finishes and engraving methods"),
        "cols": [("الخيار", "Option"), ("النتيجة", "Result"), ("ملاحظة", "Note")],
        "rows": [
            [("براص مصقول لامع", "Polished brass"), ("لمعة ذهبية كالمرآة", "Mirror-like golden shine"), ("يُسلَّم بفيلم حماية", "Supplied with protective film")],
            [("براص مخدوش (Brushed)", "Brushed brass"), ("ذهبي مطفي أنيق، يخفي البصمات", "Elegant matte gold that hides fingerprints"), ("الأكثر عملية للوحات اليومية", "Most practical for everyday plates")],
            [("حفر غائر", "Recessed engraving"), ("نص محسوس باللمس", "Text you can feel"), ("الأساس في البراص", "The standard on brass")],
            [("حفر + تعبئة أسود", "Engraved + black fill"), ("أعلى تباين ووضوح", "Highest contrast and clarity"), ("نرشّحه للوحات الأسماء", "Recommended for name plates")],
            [("نحاس أحمر", "Copper"), ("لون نحاسي دافئ مميز", "Distinctive warm copper colour"), ("للهدايا والديكور", "For gifts and décor")],
        ],
        "note": (
            "البراص يغمق تدريجياً مع الوقت (باتينا طبيعية). يمكن إضافة طبقة ورنيش شفافة تحافظ على اللمعة لفترة أطول.",
            "Brass gradually darkens over time (a natural patina). A clear lacquer coat can keep the shine longer.",
        ),
    },
    "gallery": {
        "eyebrow": ("نماذج", "Samples"),
        "h2": ("الحفر على البراص والنحاس", "Brass and copper engraving"),
        "items": [
            ("assets/img/svc/tags-route-markers.jpg", ("علامات براص وستانلس دائرية محفورة", "Engraved round brass and stainless markers"), ("براص وستانلس", "Brass and stainless"), 1200, 900),
            ("assets/img/svc/tags-mixed-materials.jpg", ("تاقات براص مع تاقات ستانلس وألمنيوم", "Brass tags with stainless and aluminium tags"), ("تاقات براص", "Brass tags"), 1200, 900),
            g("engraved-brass-plate", ("صورة لوحة براص محفورة بالليزر", "Photo of a laser engraved brass plate"), ("لوحة براص", "Brass plate")),
        ],
        "note": GALLERY_NOTE,
    },
    "process": process(),
    "related": {
        "eyebrow": ("مواد أخرى", "Other materials"),
        "h2": ("الحفر على بقية المواد", "Engraving on other materials"),
        "items": [
            {"icon": "shield", "href": "engraving-stainless-steel.html", "h3": ("الحفر على الستانلس", "Stainless engraving"), "p": ("نقش أسود عالي التباين لا يصدأ.", "High-contrast black marking, rust-free.")},
            {"icon": "layers", "href": "aluminum-engraving.html", "h3": ("الحفر على الألمنيوم", "Aluminium engraving"), "p": ("ألمنيوم ذهبي مؤكسد كبديل اقتصادي.", "Gold anodised aluminium as an economical alternative.")},
            {"icon": "cut", "href": "copper-brass-laser-cutting.html", "h3": ("قص النحاس والبراص", "Copper and brass cutting"), "p": ("قص لوحات البراص بالشكل قبل الحفر.", "Cutting brass plates to shape before engraving.")},
        ],
    },
    "faq": [
        {
            "q": ("لماذا لا يكون الحفر أسود مباشرة على البراص مثل الستانلس؟", "Why isn't brass engraving black directly like stainless?"),
            "a": (
                "البراص لا يكوّن طبقة أكسيد سوداء تحت الليزر كما يفعل الستانلس، فالحفر يظهر بلون ذهبي أفتح أو أغمق قليلاً من السطح. لذلك نعبّئ الحفر بلون أسود بعد التنفيذ عندما يكون التباين العالي مطلوباً.",
                "Brass doesn't form a black oxide layer under the laser as stainless does, so the engraving shows slightly lighter or darker gold than the surface. That's why we fill it with black afterwards when high contrast is needed.",
            ),
        },
        {
            "q": ("هل يمكن الحفر على درع أو لوحة براص جاهزة؟", "Can you engrave a ready-made brass award or plate?"),
            "a": (
                "نعم، إذا كانت المساحة مستوية وتسمح بالتثبيت تحت الليزر. أرسل صورة القطعة ومقاس المساحة المطلوب حفرها.",
                "Yes, if the area is flat and can be fixtured under the laser. Send a photo of the piece and the size of the area to engrave.",
            ),
        },
        {
            "q": ("هل تصلح لوحة البراص للخارج؟", "Is a brass plate suitable for outdoors?"),
            "a": (
                "نعم، البراص لا يصدأ ويصلح للمداخل الخارجية، لكنه يغمق مع الشمس والرطوبة. يمكن تلميعه دورياً أو حمايته بورنيش شفاف، أو اختيار الستانلس إن كنت تريد لوناً ثابتاً.",
                "Yes, brass doesn't rust and works for outdoor entrances, but darkens with sun and humidity. It can be polished periodically or protected with clear lacquer, or choose stainless for a constant colour.",
            ),
        },
        {
            "q": ("هل تحفرون الخط العربي والزخارف على البراص؟", "Do you engrave Arabic calligraphy and patterns on brass?"),
            "a": (
                "نعم، الخط العربي والزخارف الإسلامية من أجمل ما يُحفر على البراص. أرسل التصميم كملف متجه (AI أو PDF أو SVG) أو صورة واضحة ونجهّزه للحفر.",
                "Yes, Arabic calligraphy and Islamic patterns are among the most beautiful things to engrave on brass. Send the design as a vector file (AI, PDF or SVG) or a clear image and we prepare it for engraving.",
            ),
        },
    ],
    "form_services": [
        ("لوحة براص محفورة", "Engraved brass plaque"),
        ("دروع ولوحات تكريم", "Awards and plaques"),
        ("تاقات محابس براص", "Brass valve tags"),
        ("حفر على النحاس", "Copper engraving"),
        ("أخرى / غير متأكد", "Other / not sure"),
    ],
    "form_wa": WA,
    "quote_h2": ("أرسل التصميم أو النص", "Send your design or text"),
    "quote_lead": (
        "اذكر المقاس والتشطيب (لامع أو مطفي) والكمية، وهل تريد تعبئة لون.",
        "Tell us the size, finish (polished or brushed), quantity and whether you want a colour fill.",
    ),
    "cta": {
        "h2": ("لوحة ذهبية تليق بمكانك", "A golden plaque worthy of your place"),
        "p": ("أرسل التصميم، وتصلك معاينة وعرض سعر في نفس يوم العمل غالباً.", "Send the design and usually get a proof and quote the same working day."),
        "wa": WA,
    },
}
