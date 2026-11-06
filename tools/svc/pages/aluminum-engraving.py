# -*- coding: utf-8 -*-
"""الحفر بالليزر على الألمنيوم — تحت الحفر والنقش بالليزر"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _eng import ENG_PARENT, GALLERY_NOTE, g, hero_img, process  # noqa: E402

WA = "مرحباً رواد الليزر، أرغب في عرض سعر لحفر بالليزر على ألمنيوم."

PAGE = {
    "slug": "aluminum-engraving",
    "parent": ENG_PARENT,
    "crumb": ("الحفر على الألمنيوم", "Aluminium engraving"),
    "title": (
        "حفر ليزر على الألمنيوم في جدة | لوحات ألمنيوم مؤكسد ملوّن — رواد الليزر",
        "Laser Engraving on Aluminium in Jeddah | Anodised Aluminium Plates — Ruwwad Laser",
    ),
    "desc": (
        "حفر ونقش بالليزر على الألمنيوم في جدة: لوحات ألمنيوم مؤكسد (أنودايز) بالأسود والأزرق والأحمر والذهبي يظهر فيها الحفر فضياً لامعاً، ولوحات بيانات وتحكم وتاقات وبادجات. خفيف ولا يصدأ — وبدء التنفيذ خلال 6 ساعات.",
        "Laser engraving on aluminium in Jeddah: anodised aluminium plates in black, blue, red and gold where the engraving shows bright silver, plus data plates, control panels, tags and badges. Light and rust-free, with production starting within 6 hours.",
    ),
    "og_image": "assets/img/svc/tags-aluminium-colours.jpg",
    "service_type": ("حفر ليزر على الألمنيوم", "Laser engraving on aluminium"),
    "schema_name": ("الحفر بالليزر على الألمنيوم في جدة", "Laser engraving on aluminium in Jeddah"),
    "schema_desc": (
        "حفر ونقش بالفايبر ليزر على الألمنيوم الخام والمؤكسد (أنودايز) في جدة: لوحات بيانات، لوحات تحكم، لوحات تعريف ملوّنة، تاقات محابس وأصول، بادجات أسماء، ومنتجات ألمنيوم بشعار العميل.",
        "Fibre laser engraving and marking on raw and anodised aluminium in Jeddah: data plates, control panels, coloured ID plates, valve and asset tags, name badges and aluminium products with the client's logo.",
    ),
    "schema_offers": [
        ("حفر على ألمنيوم مؤكسد ملوّن", "Engraving on coloured anodised aluminium"),
        ("نقش أسود على ألمنيوم خام", "Black marking on raw aluminium"),
        ("لوحات بيانات وتحكم ألمنيوم", "Aluminium data and control plates"),
        ("تاقات وبادجات ألمنيوم", "Aluminium tags and badges"),
    ],
    "hero": {
        "eyebrow": ("ألمنيوم · حفر بالليزر", "Aluminium · laser engraving"),
        "h1": ("حفر ونقش بالليزر على الألمنيوم", "Laser engraving on aluminium"),
        "sub": (
            "الألمنيوم المؤكسد (أنودايز) من أجمل المواد للحفر: الليزر يزيل الطبقة الملوّنة فيظهر المعدن الفضي تحتها بحدّة ونظافة. لوحات خفيفة لا تصدأ، بألوان هويتك — للوحات البيانات والتحكم والتاقات والبادجات.",
            "Anodised aluminium is one of the most beautiful materials to engrave: the laser removes the coloured layer and the silver metal underneath shows crisp and clean. Light, rust-free plates in your brand colours — for data plates, control panels, tags and badges.",
        ),
        "chips": [
            ("أسود · أزرق · أحمر · ذهبي", "Black · blue · red · gold", "target"),
            ("خفيف ولا يصدأ", "Light and rust-free", "shield"),
            ("حفر فضي حادّ", "Crisp silver engraving", "engrave"),
            ("بدء خلال 6 ساعات", "Start within 6 hours", "bolt"),
        ],
        "img": ("assets/img/svc/tags-aluminium-colours.jpg", ("لوحات ألمنيوم مؤكسد بالأسود والأزرق والأحمر والأخضر محفورة بالليزر", "Black, blue, red and green anodised aluminium plates laser engraved"), 1200, 900),
        "wa": WA,
    },
    "facts": [
        (("1/3", "1/3"), ("وزن الألمنيوم مقارنة بالستانلس", "Aluminium's weight vs stainless")),
        (("+6", "+6"), ("ألوان أنودايز متاحة", "Anodised colours available")),
        (("0.2 mm", "0.2 mm"), ("أدق خط واضح", "Finest clear line")),
        (("6", "6"), ("ساعات لبدء التنفيذ", "Hours to start production")),
    ],
    "intro": {
        "h2": ("كيف يعمل الحفر على الألمنيوم؟", "How aluminium engraving works"),
        "paras": [
            (
                "الألمنيوم المؤكسد مغطّى بطبقة أكسيد ملوّنة رقيقة وصلبة. عند تمرير شعاع الفايبر ليزر عليها، يزيل الطبقة الملوّنة في مكان التصميم فقط، فيظهر الألمنيوم الفضي اللامع تحتها. النتيجة تباين قوي ونظيف — نص فضي على أسود أو أزرق أو أحمر — دون أي حبر.",
                "Anodised aluminium is covered by a thin, hard coloured oxide layer. When the fibre laser passes over it, it removes the coloured layer only where the design is, revealing bright silver aluminium underneath. The result is strong, clean contrast — silver text on black, blue or red — with no ink at all.",
            ),
            (
                "أما الألمنيوم الخام (غير المؤكسد) فنقش عليه علامات رمادية داكنة أو حفر غائر. وهو مناسب لقطع الغيار والقطع المصنّعة التي تحتاج ترقيماً دائماً، بينما يبقى المؤكسد هو الخيار الأول للوحات الظاهرة والملوّنة.",
                "On raw (non-anodised) aluminium we produce dark grey marks or recessed engraving. It suits spare parts and machined components that need permanent numbering, while anodised remains the first choice for visible, coloured plates.",
            ),
        ],
        "h3": ("لماذا تختار الألمنيوم؟", "Why choose aluminium?"),
        "bullets": [
            ("خفيف جداً — ثلث وزن الستانلس تقريباً — مناسب للبادجات واللوحات الكبيرة.", "Very light — about a third of stainless's weight — ideal for badges and large plates."),
            ("لا يصدأ، ويتحمل الرطوبة في جدة جيداً للاستخدام الداخلي وشبه الخارجي.", "Rust-free and handles Jeddah's humidity well indoors and semi-outdoors."),
            ("ألوان متعددة تطابق هوية شركتك أو نظام ألوان السلامة.", "Multiple colours to match your brand or a safety colour code."),
            ("أوفر من الستانلس والبراص للكميات الكبيرة من اللوحات والتاقات.", "More economical than stainless and brass for large quantities of plates and tags."),
        ],
    },
    "cards": {
        "eyebrow": ("الطلبات الشائعة", "Common requests"),
        "h2": ("ماذا نحفر على الألمنيوم؟", "What we engrave on aluminium"),
        "items": [
            {"icon": "file", "h3": ("لوحات البيانات", "Data plates"), "p": ("الموديل والرقم التسلسلي والمواصفات للمعدات والمكائن.", "Model, serial and specs for equipment and machines."), "href": "metal-nameplates-serial-numbers.html", "more": ("لوحات البيانات", "Data plates")},
            {"icon": "sliders", "h3": ("لوحات التحكم", "Control panels"), "p": ("واجهات لوحات التشغيل بأسماء المفاتيح والمؤشرات.", "Operating panel fascias with switch and indicator labels.")},
            {"icon": "target", "h3": ("تاقات المحابس الملوّنة", "Coloured valve tags"), "p": ("لون لكل خدمة: أحمر للحريق، أزرق للمياه، أصفر للغاز.", "A colour per service: red for fire, blue for water, yellow for gas."), "href": "valve-tags.html", "more": ("تاقات المحابس", "Valve tags")},
            {"icon": "user", "h3": ("بادجات الأسماء", "Name badges"), "p": ("خفيفة وأنيقة بألوان الهوية مع مغناطيس.", "Light and smart in brand colours with a magnet."), "href": "name-badges.html", "more": ("بادجات الأسماء", "Name badges")},
            {"icon": "store", "h3": ("اللوحات الإرشادية", "Signage plates"), "p": ("أرقام الأبواب وأسماء الأقسام بألوان موحّدة.", "Door numbers and department names in unified colours."), "href": "signage-plates.html", "more": ("اللوحات الإرشادية", "Signage plates")},
            {"icon": "cube", "h3": ("منتجات وقطع ألمنيوم", "Aluminium products and parts"), "p": ("شعارات على العلب والأجهزة وأرقام على القطع المصنّعة.", "Logos on cases and devices, numbers on machined parts.")},
        ],
    },
    "specs": {
        "soft": True,
        "eyebrow": ("الأنواع", "Types"),
        "h2": ("نتيجة الحفر حسب نوع الألمنيوم", "Engraving result by aluminium type"),
        "cols": [("النوع", "Type"), ("نتيجة الحفر", "Result"), ("الأنسب لـ", "Best for")],
        "rows": [
            [("مؤكسد أسود", "Black anodised"), ("فضي لامع على أسود — أعلى تباين", "Bright silver on black — highest contrast"), ("لوحات البيانات والتحكم", "Data and control plates")],
            [("مؤكسد ملوّن", "Coloured anodised"), ("فضي على أزرق أو أحمر أو أخضر", "Silver on blue, red or green"), ("التاقات والبادجات واللوحات الإرشادية", "Tags, badges and signage")],
            [("مؤكسد ذهبي", "Gold anodised"), ("فضي على ذهبي — بديل اقتصادي للبراص", "Silver on gold — an economical brass alternative"), ("البادجات والدروع", "Badges and awards")],
            [("ألمنيوم خام", "Raw aluminium"), ("نقش رمادي داكن أو حفر غائر", "Dark grey mark or recessed"), ("قطع الغيار والقطع المصنّعة", "Spare and machined parts")],
            [("ألمنيوم مطلي (بودرة)", "Powder-coated"), ("إزالة الطلاء وكشف المعدن", "Coating removed to reveal metal"), ("الأجهزة والهياكل المطلية", "Coated devices and housings")],
        ],
        "note": (
            "سماكات اللوحات الشائعة 0.5 – 1.5 مم، ويمكن قصّ اللوحة بالشكل المطلوب وعمل الثقوب في نفس الطلب.",
            "Common plate thicknesses are 0.5 – 1.5 mm, and the plate can be cut to shape with holes in the same order.",
        ),
    },
    "gallery": {
        "eyebrow": ("نماذج", "Samples"),
        "h2": ("الحفر على الألمنيوم", "Aluminium engraving"),
        "items": [
            ("assets/img/svc/tags-valve-colours.jpg", ("تاقات ألمنيوم ملوّنة محفورة بالأرقام", "Coloured aluminium tags engraved with numbers"), ("تاقات ملوّنة", "Coloured tags"), 1200, 900),
            ("assets/img/svc/tags-panel-labels.jpg", ("لوحات ألمنيوم ملوّنة للوحات الكهرباء والتحكم", "Coloured aluminium labels for electrical and control panels"), ("لوحات الكهرباء", "Electrical panels"), 1200, 900),
            ("assets/img/svc/tags-aluminium-test.jpg", ("عيّنات ألمنيوم مؤكسد بأربعة ألوان", "Anodised aluminium samples in four colours"), ("عيّنات الألوان", "Colour samples"), 1200, 670),
        ],
        "note": GALLERY_NOTE,
    },
    "process": process(),
    "related": {
        "eyebrow": ("معادن أخرى", "Other metals"),
        "h2": ("الحفر على بقية المواد", "Engraving on other materials"),
        "items": [
            {"icon": "shield", "href": "engraving-stainless-steel.html", "h3": ("الحفر على الستانلس", "Stainless engraving"), "p": ("للخارج والمطابخ والبيئات الساحلية.", "For outdoors, kitchens and coastal environments.")},
            {"icon": "target", "href": "brass-engraving.html", "h3": ("الحفر على البراص", "Brass engraving"), "p": ("لوحات ودروع ذهبية فاخرة.", "Premium golden plaques and awards.")},
            {"icon": "cut", "href": "aluminum-laser-cutting.html", "h3": ("قص الألمنيوم بالليزر", "Aluminium laser cutting"), "p": ("نقصّ اللوح بالشكل المطلوب ثم نحفره.", "We cut the sheet to shape then engrave it.")},
        ],
    },
    "faq": [
        {
            "q": ("هل يمكن الحفر على ألمنيوم بلون معيّن من هويتنا؟", "Can you engrave aluminium in our brand colour?"),
            "a": (
                "نعم، نوفّر الألمنيوم المؤكسد بألوان شائعة (أسود، أزرق، أحمر، أخضر، ذهبي، فضي). وللألوان الخاصة جداً يمكن استخدام ألمنيوم مطلي بلون هويتك ثم الحفر عليه.",
                "Yes, we supply anodised aluminium in common colours (black, blue, red, green, gold, silver). For very specific colours we can use aluminium coated in your brand colour and engrave it.",
            ),
        },
        {
            "q": ("هل يصلح الألمنيوم للخارج؟", "Is aluminium suitable for outdoors?"),
            "a": (
                "الألمنيوم لا يصدأ ويصلح لكثير من الاستخدامات الخارجية، لكن لون الأنودايز قد يفقد بعض حدّته مع سنوات من الشمس المباشرة. للوحات المعرّضة للشمس طوال اليوم أو القريبة من البحر نرشّح الستانلس 316.",
                "Aluminium doesn't rust and suits many outdoor uses, but anodised colour can lose some vibrancy over years of direct sun. For plates in full sun all day or near the sea we recommend stainless 316.",
            ),
        },
        {
            "q": ("هل يمكن الحفر على قطعة ألمنيوم جاهزة؟", "Can you engrave a finished aluminium part?"),
            "a": (
                "نعم: علب الأجهزة، الحوافظ، القطع المصنّعة، والترامس. أرسل صورة القطعة ومقاساتها لنتأكد من إمكانية تثبيتها تحت الليزر.",
                "Yes: device cases, holders, machined parts and flasks. Send a photo and dimensions so we can confirm it can be fixtured under the laser.",
            ),
        },
        {
            "q": ("ما الفرق بين الحفر والنقش على الألمنيوم؟", "What is the difference between engraving and marking on aluminium?"),
            "a": (
                "على المؤكسد، النقش السطحي يزيل الطبقة الملوّنة فقط وهو الأكثر استخداماً. الحفر الغائر يزيل جزءاً من المعدن ليصبح النص محسوساً باللمس، ويُستخدم للقطع المعرّضة للاحتكاك.",
                "On anodised aluminium, surface marking removes only the coloured layer and is the most common. Recessed engraving removes some metal so the text can be felt, used for parts exposed to abrasion.",
            ),
        },
    ],
    "form_services": [
        ("حفر على ألمنيوم مؤكسد", "Anodised aluminium engraving"),
        ("لوحات بيانات ألمنيوم", "Aluminium data plates"),
        ("تاقات أو بادجات ألمنيوم", "Aluminium tags or badges"),
        ("حفر على قطعة جاهزة", "Engraving a finished part"),
        ("أخرى / غير متأكد", "Other / not sure"),
    ],
    "form_wa": WA,
    "quote_h2": ("أرسل التصميم واللون المطلوب", "Send the design and colour"),
    "quote_lead": (
        "اذكر اللون والمقاس والكمية، وأرفق التصميم أو قائمة النصوص.",
        "Tell us the colour, size and quantity, and attach the design or text list.",
    ),
    "cta": {
        "h2": ("ألمنيوم بألوانك، وحفر لا يُمحى", "Aluminium in your colours, engraving that lasts"),
        "p": ("أرسل التصميم، وتصلك معاينة وعرض سعر في نفس يوم العمل غالباً.", "Send the design and usually get a proof and quote the same working day."),
        "wa": WA,
    },
}
