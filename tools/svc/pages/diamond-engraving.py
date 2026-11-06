# -*- coding: utf-8 -*-
"""الحفر الماسي (Diamond Drag Engraving) للوحات البيانات — تحت الحفر والنقش بالليزر"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _eng import ENG_PARENT, GALLERY_NOTE, g, hero_img, process  # noqa: E402

WA = "مرحباً رواد الليزر، أرغب في عرض سعر لحفر لوحات بيانات (حفر ماسي أو ليزر)."

PAGE = {
    "slug": "diamond-engraving",
    "parent": ENG_PARENT,
    "crumb": ("الحفر الماسي ولوحات البيانات", "Diamond engraving &amp; data plates"),
    "title": (
        "الحفر الماسي في جدة | Diamond Engraving للوحات البيانات والمعدات — رواد الليزر",
        "Diamond Engraving in Jeddah | Data Plates &amp; Equipment Nameplates — Ruwwad Laser",
    ),
    "desc": (
        "الحفر الماسي (Diamond Drag Engraving) وحفر الليزر للوحات البيانات في جدة: لوحات معدات وأوعية ضغط ومكائن بخطوط دقيقة على الستانلس والألمنيوم والبراص، بجداول المواصفات والأرقام التسلسلية. بدء التنفيذ خلال 6 ساعات.",
        "Diamond drag engraving and laser marking for data plates in Jeddah: equipment, pressure-vessel and machine nameplates with fine lines on stainless, aluminium and brass, with spec tables and serial numbers. Production starts within 6 hours.",
    ),
    "og_image": "assets/img/svc/tags-dataplate-tank.jpg",
    "service_type": ("الحفر الماسي ولوحات البيانات", "Diamond engraving and data plates"),
    "schema_name": ("الحفر الماسي للوحات البيانات في جدة", "Diamond engraving for data plates in Jeddah"),
    "schema_desc": (
        "حفر لوحات البيانات والمعدات في جدة بالحفر الماسي (Diamond Drag) أو الفايبر ليزر: لوحات أوعية الضغط والمكائن والمضخات والمحولات، بجداول المواصفات والأرقام التسلسلية وأكواد QR، على الستانلس والألمنيوم والبراص.",
        "Data and equipment plate engraving in Jeddah by diamond drag or fibre laser: nameplates for pressure vessels, machines, pumps and transformers with spec tables, serial numbers and QR codes, on stainless, aluminium and brass.",
    ),
    "schema_offers": [
        ("الحفر الماسي على المعادن", "Diamond drag engraving on metal"),
        ("لوحات بيانات المعدات", "Equipment data plates"),
        ("لوحات أوعية الضغط", "Pressure vessel nameplates"),
        ("ترقيم تسلسلي للوحات", "Serialised nameplates"),
    ],
    "hero": {
        "eyebrow": ("Diamond Engraving · لوحات بيانات", "Diamond engraving · data plates"),
        "h1": ("الحفر الماسي ولوحات البيانات", "Diamond engraving and data plates"),
        "sub": (
            "لوحة بيانات المعدة هي هويتها الرسمية: الشركة المصنّعة، الموديل، الرقم التسلسلي، الضغط، القدرة، وسنة الصنع. ننفّذها بالحفر الماسي ذي الخطوط الفضية الدقيقة، أو بالفايبر ليزر بنقش أسود — حسب ما تتطلبه المعدة والمواصفات.",
            "An equipment data plate is its official identity: manufacturer, model, serial number, pressure, capacity and year. We produce it by diamond drag engraving with fine silver lines, or by fibre laser with black marking — whichever the equipment and specification require.",
        ),
        "chips": [
            ("خطوط فضية دقيقة", "Fine silver lines", "engrave"),
            ("جداول مواصفات كاملة", "Full spec tables", "file"),
            ("ترقيم تسلسلي", "Serial numbering", "target"),
            ("جداول مواصفات وأرقام تسلسلية", "Spec tables and serial numbers", "check"),
        ],
        "img": ("assets/img/svc/tags-dataplate-tank.jpg", ("لوحة بيانات ستانلس لخزان ضغط بجدول مواصفات محفور", "Stainless pressure tank data plate with an engraved spec table"), 1200, 900),
        "wa": WA,
    },
    "facts": [
        (("0.1 mm", "0.1 mm"), ("عرض خط الحفر الماسي تقريباً", "Approx. diamond line width")),
        (("2", "2"), ("تقنيتان: ماسي وفايبر ليزر", "Two methods: diamond and fibre laser")),
        (("6", "6"), ("ساعات لبدء التنفيذ", "Hours to start production")),
        (("100%", "100%"), ("مراجعة البيانات قبل الحفر", "Data checked before engraving")),
    ],
    "intro": {
        "h2": ("ما هو الحفر الماسي؟", "What is diamond engraving?"),
        "paras": [
            (
                "الحفر الماسي (Diamond Drag Engraving) طريقة ميكانيكية تستخدم رأساً مصنوعاً من الماس يُسحب فوق سطح المعدن تحت ضغط محسوب، فيرسم خطاً رفيعاً لامعاً يشبه الخدش المتقن. لا يدور الرأس ولا يزيل مادة تقريباً، بل يضغط السطح فيكوّن خطاً فضياً حاداً يعكس الضوء.",
                "Diamond drag engraving is a mechanical method using a diamond-tipped tool dragged across the metal surface under controlled pressure, drawing a fine bright line like a precise scratch. The tip doesn't spin and removes almost no material; it burnishes the surface into a sharp silver line that catches the light.",
            ),
            (
                "هذا الأسلوب كلاسيكي في لوحات بيانات المعدات وأوعية الضغط والمكائن، خصوصاً على الألمنيوم المؤكسد والبراص والمعادن المطلية. وعند الحاجة لتباين أعلى أو أكواد QR وباركود، ننفّذ اللوحة نفسها بالفايبر ليزر — ونرشّح لك الأنسب حسب المادة والمواصفات.",
                "It's a classic for equipment, pressure-vessel and machine data plates, especially on anodised aluminium, brass and coated metals. When higher contrast or QR codes and barcodes are needed, we produce the same plate by fibre laser — and recommend the best option for the material and specification.",
            ),
        ],
        "h3": ("ماذا تحتوي لوحة البيانات عادةً؟", "What a data plate usually contains"),
        "bullets": [
            ("اسم الشركة المصنّعة أو المالكة وشعارها.", "The manufacturer's or owner's name and logo."),
            ("الموديل والرقم التسلسلي وسنة الصنع.", "Model, serial number and year of manufacture."),
            ("المواصفات الفنية: الضغط، الحرارة، الجهد، القدرة، السعة، الوزن.", "Technical ratings: pressure, temperature, voltage, power, capacity, weight."),
            ("علامات المطابقة وكود QR يقود إلى دليل المعدة أو سجل الصيانة.", "Conformity marks and a QR code linking to the manual or maintenance log."),
        ],
    },
    "cards": {
        "eyebrow": ("الاستخدامات", "Uses"),
        "h2": ("أين تُستخدم لوحات البيانات المحفورة؟", "Where engraved data plates are used"),
        "items": [
            {"icon": "factory", "h3": ("أوعية الضغط والخزانات", "Pressure vessels and tanks"), "p": ("ضغط التصميم والاختبار والسعة ورقم الوعاء.", "Design and test pressure, capacity and vessel number.")},
            {"icon": "sliders", "h3": ("المكائن وخطوط الإنتاج", "Machines and production lines"), "p": ("الموديل والرقم التسلسلي والجهد والقدرة.", "Model, serial, voltage and power.")},
            {"icon": "bolt", "h3": ("المحولات ولوحات الكهرباء", "Transformers and switchgear"), "p": ("بيانات التصنيف والتوصيل.", "Rating and connection data.")},
            {"icon": "cube", "h3": ("المضخات والضواغط", "Pumps and compressors"), "p": ("التدفق والضغط والسرعة والمحرك.", "Flow, head, speed and motor.")},
            {"icon": "file", "h3": ("لوحات الأصول", "Asset plates"), "p": ("رقم الأصل وكود QR لنظام إدارة الصيانة.", "Asset number and QR for the maintenance system."), "href": "qr-barcode-marking.html", "more": ("حفر QR والباركود", "QR and barcode marking")},
            {"icon": "shield", "h3": ("لوحات المعايرة", "Calibration plates"), "p": ("تاريخ المعايرة والجهة ورقم الشهادة.", "Calibration date, body and certificate number.")},
        ],
    },
    "specs": {
        "soft": True,
        "eyebrow": ("مقارنة", "Comparison"),
        "h2": ("الحفر الماسي أم الفايبر ليزر؟", "Diamond engraving or fibre laser?"),
        "cols": [("البند", "Aspect"), ("الحفر الماسي", "Diamond drag"), ("الفايبر ليزر", "Fibre laser")],
        "rows": [
            [("شكل الخط", "Line look"), ("فضي لامع رفيع", "Fine bright silver"), ("أسود عميق أو غائر", "Deep black or recessed")],
            [("أفضل المواد", "Best materials"), ("ألمنيوم مؤكسد، براص، معادن مطلية", "Anodised aluminium, brass, coated metals"), ("كل المعادن، خاصة الستانلس", "All metals, especially stainless")],
            [("أكواد QR والباركود", "QR and barcodes"), ("محدود", "Limited"), ("ممتاز", "Excellent")],
            [("الشعارات المعبّأة", "Filled logos"), ("خطوط فقط", "Outline only"), ("تعبئة كاملة", "Fully filled")],
            [("الطابع", "Character"), ("كلاسيكي أنيق", "Classic and elegant"), ("صناعي عالي التباين", "Industrial, high contrast")],
        ],
        "note": (
            "لا تعرف أيهما تحتاج؟ أرسل صورة لوحة قديمة أو بند المواصفات، ونخبرك بالتقنية الأنسب قبل التسعير.",
            "Not sure which you need? Send a photo of an old plate or the specification clause and we tell you the best method before pricing.",
        ),
    },
    "gallery": {
        "eyebrow": ("نماذج", "Samples"),
        "h2": ("لوحات البيانات المحفورة", "Engraved data plates"),
        "items": [
            ("assets/img/svc/tags-pressure-vessel.jpg", ("لوحة بيانات مثبّتة على وعاء ضغط ستانلس", "Data plate fixed on a stainless pressure vessel"), ("على المعدّة", "On the equipment"), 1200, 900),
            ("assets/img/svc/tags-motor-plate.jpg", ("لوحة بيانات زرقاء على محرك صناعي", "Blue data plate on an industrial motor"), ("لوحة محرك", "Motor plate"), 1200, 900),
            g("dataplate-before-after-engraving", ("لوحة بيانات قبل الحفر وبعده", "A data plate before and after engraving"), ("قبل وبعد", "Before and after")),
        ],
        "note": GALLERY_NOTE,
    },
    "process": process(("من البيانات إلى اللوحة", "From the data to the plate")),
    "related": {
        "eyebrow": ("مرتبط", "Related"),
        "h2": ("خدمات مرتبطة", "Related services"),
        "items": [
            {"icon": "file", "href": "metal-nameplates-serial-numbers.html", "h3": ("لوحات البيانات والأرقام التسلسلية", "Data plates and serial numbers"), "p": ("لوحات بيانات بالفايبر ليزر وترقيم تسلسلي.", "Fibre laser data plates with serial numbering.")},
            {"icon": "shield", "href": "engraving-stainless-steel.html", "h3": ("الحفر على الستانلس", "Stainless engraving"), "p": ("نقش أسود عالي التباين لا يصدأ.", "High-contrast black marking, rust-free.")},
            {"icon": "target", "href": "qr-barcode-marking.html", "h3": ("حفر QR والباركود", "QR and barcode marking"), "p": ("أكواد قابلة للمسح على لوحات المعدات.", "Scannable codes on equipment plates.")},
        ],
    },
    "faq": [
        {
            "q": ("هل يدوم الحفر الماسي؟", "Is diamond engraving durable?"),
            "a": (
                "نعم، الخط مضغوط في سطح المعدن نفسه ولا يحتوي حبراً، فلا يبهت ولا يُمحى بالمسح أو المذيبات. لكنه أقل عمقاً من الحفر الغائر بالليزر، لذلك نرشّح الليزر للقطع المعرّضة لاحتكاك شديد.",
                "Yes, the line is burnished into the metal itself with no ink, so it doesn't fade or wipe off with cleaning or solvents. It is shallower than laser recessed engraving, so we recommend laser for parts under heavy abrasion.",
            ),
        },
        {
            "q": ("هل يمكن تصنيع لوحة بيانات بديلة لمعدة قديمة؟", "Can you make a replacement data plate for old equipment?"),
            "a": (
                "نعم، أرسل صورة واضحة للوحة القديمة (حتى لو كانت تالفة جزئياً) مع البيانات الصحيحة، ونعيد تصميمها وتصنيعها بنفس المقاس وأماكن الثقوب.",
                "Yes, send a clear photo of the old plate (even if partly damaged) with the correct data, and we redesign and make it to the same size and hole positions.",
            ),
        },
        {
            "q": ("هل تنفّذون لوحات بأرقام تسلسلية لعدة معدات؟", "Do you make serialised plates for multiple units?"),
            "a": (
                "نعم، نصمم قالباً موحّداً ونربطه بقائمة الأرقام التسلسلية والبيانات المتغيرة من إكسل، فتخرج كل لوحة ببياناتها الخاصة دون أخطاء نسخ.",
                "Yes, we design a unified template linked to your serial numbers and variable data from Excel, so every plate comes out with its own data and no retyping errors.",
            ),
        },
        {
            "q": ("ما المادة الأنسب للوحة البيانات؟", "Which material is best for a data plate?"),
            "a": (
                "الستانلس 304/316 للمعدات الخارجية والكيميائية، والألمنيوم المؤكسد للمعدات الداخلية لخفته وتكلفته، والبراص للمظهر الكلاسيكي. نرشّح لك حسب بيئة تشغيل المعدة.",
                "Stainless 304/316 for outdoor and chemical equipment, anodised aluminium for indoor equipment thanks to its weight and cost, and brass for a classic look. We recommend based on the equipment's operating environment.",
            ),
        },
    ],
    "form_services": [
        ("لوحة بيانات معدة", "Equipment data plate"),
        ("لوحة وعاء ضغط", "Pressure vessel nameplate"),
        ("لوحة بديلة لمعدة قديمة", "Replacement plate for old equipment"),
        ("لوحات بترقيم تسلسلي", "Serialised plates"),
        ("أخرى / غير متأكد", "Other / not sure"),
    ],
    "form_wa": WA,
    "quote_h2": ("أرسل بيانات اللوحة أو صورة القديمة", "Send the plate data or a photo of the old one"),
    "quote_lead": (
        "اذكر المادة والمقاس والكمية، وأرفق البيانات أو صورة اللوحة الحالية.",
        "Tell us the material, size and quantity, and attach the data or a photo of the current plate.",
    ),
    "cta": {
        "h2": ("هوية رسمية لكل معدة", "An official identity for every machine"),
        "p": ("أرسل البيانات، وتصلك معاينة وعرض سعر في نفس يوم العمل غالباً.", "Send the data and usually get a proof and quote the same working day."),
        "wa": WA,
    },
}
