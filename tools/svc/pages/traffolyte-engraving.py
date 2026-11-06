# -*- coding: utf-8 -*-
"""لوحات الترافوليت (Traffolyte) — تحت الحفر والنقش بالليزر"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _eng import ENG_PARENT, GALLERY_NOTE, g, hero_img, process  # noqa: E402

WA = "مرحباً رواد الليزر، أرغب في عرض سعر للوحات ترافوليت محفورة."

PAGE = {
    "slug": "traffolyte-engraving",
    "parent": ENG_PARENT,
    "crumb": ("لوحات الترافوليت", "Traffolyte labels"),
    "title": (
        "لوحات ترافوليت في جدة | Traffolyte Labels للوحات الكهرباء والتحكم — رواد الليزر",
        "Traffolyte Labels in Jeddah | Engraved Electrical &amp; Control Panel Labels — Ruwwad Laser",
    ),
    "desc": (
        "لوحات وتسميات ترافوليت (Traffolyte) محفورة في جدة للوحات التوزيع الكهربائية والقواطع ولوحات التحكم: أحمر/أبيض، أسود/أبيض، أصفر/أسود، أزرق، أخضر — بالعربي والإنجليزي. ترقيم من إكسل لمشاريع MEP.",
        "Engraved Traffolyte labels in Jeddah for distribution boards, breakers and control panels: red/white, black/white, yellow/black, blue and green — Arabic and English. Numbered from Excel for MEP projects.",
    ),
    "og_image": "assets/img/svc/tags-panel-labels.jpg",
    "service_type": ("لوحات ترافوليت محفورة", "Engraved Traffolyte labels"),
    "schema_name": ("لوحات الترافوليت في جدة", "Traffolyte labels in Jeddah"),
    "schema_desc": (
        "تصنيع لوحات وتسميات الترافوليت (بلاستيك طبقات) المحفورة في جدة للوحات التوزيع الكهربائية ومراكز التحكم بالمحركات ولوحات التشغيل والمعدات: حفر يكشف لون الطبقة الداخلية بألوان قياسية، باللغتين العربية والإنجليزية.",
        "Manufacture of engraved Traffolyte (laminated plastic) labels in Jeddah for distribution boards, motor control centres, operating panels and equipment: engraving reveals the core colour in standard combinations, in Arabic and English.",
    ),
    "schema_offers": [
        ("تسميات لوحات التوزيع", "Distribution board labels"),
        ("تسميات القواطع والدوائر", "Breaker and circuit labels"),
        ("لوحات تحذير ترافوليت", "Traffolyte warning labels"),
        ("واجهات لوحات التحكم", "Control panel fascias"),
    ],
    "hero": {
        "eyebrow": ("Traffolyte · لوحات كهرباء", "Traffolyte · electrical panels"),
        "h1": ("لوحات وتسميات ترافوليت محفورة", "Engraved Traffolyte labels"),
        "sub": (
            "الترافوليت هو المعيار المعروف لتسميات لوحات الكهرباء: بلاستيك من طبقتين بلونين، والحفر يزيل الطبقة العلوية فيظهر لون الطبقة الداخلية بحروف حادة لا تُمحى. نصنع تسميات لوحات التوزيع والقواطع ومراكز التحكم بالمقاسات والألوان المطلوبة في مشروعك.",
            "Traffolyte is the recognised standard for electrical panel labels: two-layer, two-colour plastic where engraving removes the top layer to reveal the core colour in crisp, indelible characters. We make labels for distribution boards, breakers and control centres in the sizes and colours your project requires.",
        ),
        "chips": [
            ("ألوان قياسية للكهرباء", "Standard electrical colours", "target"),
            ("عربي + إنجليزي", "Arabic + English", "globe"),
            ("ترقيم من إكسل", "Numbering from Excel", "file"),
            ("لاصق أو براغي", "Adhesive or screws", "check"),
        ],
        "img": ("assets/img/svc/tags-panel-labels.jpg", ("تسميات ملوّنة للوحات الكهرباء: المفتاح الرئيسي، لوحة التوزيع، لوحة التحكم، إيقاف الطوارئ", "Coloured labels for electrical panels: main switch, distribution board, control panel, emergency stop"), 1200, 900),
        "wa": WA,
    },
    "facts": [
        (("2", "2"), ("طبقتان بلونين في كل لوح", "Two coloured layers per sheet")),
        (("+6", "+6"), ("تركيبات ألوان قياسية", "Standard colour combinations")),
        (("1.6 – 3 mm", "1.6 – 3 mm"), ("السماكات الشائعة", "Common thicknesses")),
        (("100%", "100%"), ("مطابقة مع جدول اللوحات", "Matched to the board schedule")),
    ],
    "intro": {
        "h2": ("ما هو الترافوليت ولماذا يُطلب في لوحات الكهرباء؟", "What Traffolyte is and why electrical panels require it"),
        "paras": [
            (
                "«ترافوليت» اسم تجاري أصبح يُطلق على كل بلاستيك الطبقات المخصص للحفر: لوح من طبقة خارجية رقيقة بلون، وطبقة داخلية بلون آخر. عند الحفر تُزال الطبقة الخارجية في مكان الحروف فقط، فيظهر النص بلون الطبقة الداخلية — أبيض على أحمر، أو أسود على أصفر مثلاً.",
                "“Traffolyte” is a trade name now used for all laminated plastic made for engraving: a sheet with a thin coloured outer layer and an inner layer of another colour. Engraving removes the outer layer only where the characters are, so the text appears in the core colour — white on red, or black on yellow, for example.",
            ),
            (
                "ولأن النص محفور وليس مطبوعاً، لا يبهت ولا يتأثر بحرارة اللوحات الكهربائية. ولهذا تنص مواصفات كثير من المشاريع على تسميات ترافوليت لكل لوحة توزيع وكل قاطع ودائرة، بألوان تحدد طبيعة كل لوحة: تحذير، طوارئ، تغذية عادية، وغيرها.",
                "Because the text is engraved, not printed, it doesn't fade or suffer from the heat of electrical panels. That's why many project specifications call for Traffolyte labels on every distribution board, breaker and circuit, with colours indicating each board's nature: warning, emergency, normal supply and so on.",
            ),
        ],
        "h3": ("أين تُستخدم لوحات الترافوليت؟", "Where Traffolyte labels are used"),
        "bullets": [
            ("لوحات التوزيع الرئيسية والفرعية (MDB / SMDB / DB) وأسماء الدوائر.", "Main and sub distribution boards (MDB / SMDB / DB) and circuit names."),
            ("مراكز التحكم بالمحركات (MCC) ولوحات التشغيل في المصانع.", "Motor control centres (MCC) and operating panels in plants."),
            ("تحذيرات الجهد والعزل: DANGER 415V، تغذية مزدوجة، لا تفتح قبل الفصل.", "Voltage and isolation warnings: DANGER 415V, dual supply, isolate before opening."),
            ("تسميات المعدات الميكانيكية والمضخات وأنظمة التكييف داخل غرف المعدات.", "Labels for mechanical equipment, pumps and HVAC inside plant rooms."),
        ],
    },
    "cards": {
        "eyebrow": ("الأنواع", "Types"),
        "h2": ("تسميات الترافوليت الشائعة", "Common Traffolyte labels"),
        "items": [
            {"icon": "bolt", "h3": ("أسماء اللوحات", "Board names"), "p": ("اسم اللوحة ومصدر تغذيتها: MDB-01 FED FROM TX-1.", "Board name and supply source: MDB-01 FED FROM TX-1.")},
            {"icon": "sliders", "h3": ("تسميات القواطع", "Breaker labels"), "p": ("شريحة صغيرة لكل قاطع باسم الدائرة.", "A small strip per breaker with the circuit name.")},
            {"icon": "shield", "h3": ("لوحات التحذير", "Warning labels"), "p": ("أحمر بحروف بيضاء: خطر، جهد عالٍ، تغذية مزدوجة.", "Red with white letters: danger, high voltage, dual supply."), "href": "safety-signs.html", "more": ("لوحات السلامة", "Safety signs")},
            {"icon": "target", "h3": ("أزرار التشغيل والإيقاف", "Start/stop legends"), "p": ("تسميات حول الأزرار والمفاتيح: START، STOP، AUTO/MAN.", "Legends around buttons and switches: START, STOP, AUTO/MAN.")},
            {"icon": "file", "h3": ("جداول الدوائر", "Circuit schedules"), "p": ("لوحة كبيرة بجدول دوائر اللوحة تُثبّت داخل الباب.", "A larger plate with the board's circuit schedule fixed inside the door.")},
            {"icon": "factory", "h3": ("تسميات المعدات", "Equipment labels"), "p": ("المضخات ووحدات التكييف والمراوح في غرف المعدات.", "Pumps, AHUs and fans in plant rooms.")},
        ],
    },
    "specs": {
        "soft": True,
        "eyebrow": ("الألوان", "Colours"),
        "h2": ("تركيبات الألوان القياسية واستخدامها المعتاد", "Standard colour combinations and typical use"),
        "cols": [("الوجه / النص", "Face / text"), ("الاستخدام المعتاد", "Typical use"), ("ملاحظة", "Note")],
        "rows": [
            [("أبيض / أسود", "White / black"), ("التسميات العامة للوحات والدوائر", "General board and circuit labels"), ("الأكثر استخداماً", "Most common")],
            [("أسود / أبيض", "Black / white"), ("أسماء اللوحات الرئيسية", "Main board names"), ("مظهر احترافي واضح", "Clear professional look")],
            [("أحمر / أبيض", "Red / white"), ("التحذيرات والطوارئ والحريق", "Warnings, emergency and fire"), ("لوحات الطوارئ والحريق", "Emergency and fire boards")],
            [("أصفر / أسود", "Yellow / black"), ("تنبيهات الحذر", "Caution notices"), ("أسطح ساخنة، تغذية مزدوجة", "Hot surfaces, dual supply")],
            [("أزرق / أبيض", "Blue / white"), ("تعليمات إلزامية ولوحات خاصة", "Mandatory instructions and special boards"), ("حسب مواصفات المشروع", "Per project spec")],
            [("أخضر / أبيض", "Green / white"), ("الطوارئ والسلامة والتشغيل الآمن", "Emergency, safety and safe operation"), ("مثل الإيقاف الطارئ", "e.g. emergency stop")],
        ],
        "note": (
            "الاستخدامات أعلاه شائعة لكنها تختلف بين المشاريع — نلتزم دائماً بجدول الألوان في مواصفات مشروعك أو متطلبات الاستشاري.",
            "The uses above are common but vary between projects — we always follow the colour table in your project specification or consultant requirements.",
        ),
    },
    "gallery": {
        "eyebrow": ("نماذج", "Samples"),
        "h2": ("لوحات الترافوليت والتعريف الكهربائي", "Traffolyte and electrical identification"),
        "items": [
            g("ill-traffolyte-engraving", ("تسميات ترافوليت بألوان مختلفة للوحات الكهرباء", "Traffolyte labels in different colours for electrical panels"), ("ألوان الترافوليت", "Traffolyte colours")),
            ("assets/img/svc/tags-high-voltage-wall.jpg", ("لوحة تحذير بجانب لوحة كهرباء", "Warning sign beside an electrical panel"), ("غرف الكهرباء", "Electrical rooms"), 1200, 900),
            ("assets/img/svc/tags-cable-bundle.jpg", ("تاقات كيابل مرقّمة لنفس اللوحة", "Numbered cable tags for the same panel"), ("مع تاقات الكيابل", "With cable tags"), 1200, 900),
        ],
        "note": GALLERY_NOTE,
    },
    "process": process(("من جدول اللوحات إلى التركيب", "From the board schedule to installation")),
    "related": {
        "eyebrow": ("للمشروع نفسه", "For the same project"),
        "h2": ("ما يُطلب عادةً مع الترافوليت", "Usually ordered with Traffolyte"),
        "items": [
            {"icon": "bolt", "href": "cable-id-tags.html", "h3": ("تاقات الكيابل", "Cable ID tags"), "p": ("تعريف الكيابل الداخلة والخارجة من كل لوحة.", "Identifying cables in and out of every board.")},
            {"icon": "cube", "href": "pvc-abs-engraving.html", "h3": ("الحفر على ABS وPVC", "ABS and PVC engraving"), "p": ("لوحات بلاستيكية أكبر وأسمك.", "Larger, thicker plastic plates.")},
            {"icon": "layers", "href": "aluminum-engraving.html", "h3": ("الحفر على الألمنيوم", "Aluminium engraving"), "p": ("بديل معدني لتسميات اللوحات الخارجية.", "A metal alternative for outdoor board labels.")},
        ],
    },
    "faq": [
        {
            "q": ("هل الترافوليت يصلح للخارج؟", "Is Traffolyte suitable for outdoors?"),
            "a": (
                "الترافوليت مصمم أساساً للاستخدام الداخلي داخل اللوحات وغرف الكهرباء. للوحات الخارجية المعرّضة للشمس المباشرة نرشّح ألواح طبقات مقاومة للأشعة فوق البنفسجية، أو الانتقال إلى الألمنيوم أو الستانلس.",
                "Traffolyte is designed mainly for indoor use inside panels and electrical rooms. For outdoor boards in direct sun we recommend UV-stable laminates, or moving to aluminium or stainless.",
            ),
        },
        {
            "q": ("كيف تُثبّت التسميات على اللوحة؟", "How are labels fixed to the panel?"),
            "a": (
                "بلاصق صناعي ثنائي الوجه على الأبواب المعدنية الملساء، أو ببراغي/برشام عبر ثقوب في الزوايا عندما تشترط المواصفات تثبيتاً ميكانيكياً.",
                "With industrial double-sided tape on smooth metal doors, or with screws/rivets through corner holes when the specification requires mechanical fixing.",
            ),
        },
        {
            "q": ("هل يمكن طلب مئات التسميات بأسماء مختلفة؟", "Can I order hundreds of labels with different names?"),
            "a": (
                "نعم، وهذا هو المعتاد في المشاريع. أرسل جدول اللوحات والدوائر في ملف إكسل، ونحفر كل تسمية بنصها تلقائياً ونسلّمها مرتّبة ومغلّفة حسب اللوحة.",
                "Yes, that's the norm on projects. Send the board and circuit schedule in Excel; we engrave each label with its text automatically and deliver them sorted and bagged by board.",
            ),
        },
        {
            "q": ("بأي تقنية يُحفر الترافوليت؟", "What technology engraves Traffolyte?"),
            "a": (
                "يُحفر بماكينات CNC الدوّارة أو بليزر CO2 المناسب للبلاستيك، ونختار الطريقة حسب نوع اللوح وحجم الحروف للحصول على أنظف حواف.",
                "It's engraved with rotary CNC machines or a plastics-suitable CO2 laser; we choose the method by sheet type and character size for the cleanest edges.",
            ),
        },
    ],
    "form_services": [
        ("تسميات لوحات توزيع", "Distribution board labels"),
        ("تسميات قواطع ودوائر", "Breaker and circuit labels"),
        ("لوحات تحذير ترافوليت", "Traffolyte warning labels"),
        ("مشروع كامل MEP", "Complete MEP project"),
        ("أخرى / غير متأكد", "Other / not sure"),
    ],
    "form_wa": WA,
    "quote_h2": ("أرسل جدول اللوحات والدوائر", "Send your board and circuit schedule"),
    "quote_lead": (
        "اذكر الألوان والمقاسات والعدد التقريبي، وأرفق الجدول أو بند المواصفات.",
        "Tell us the colours, sizes and approximate count, and attach the schedule or specification clause.",
    ),
    "cta": {
        "h2": ("كل لوحة وكل قاطع باسمه", "Every board and breaker labelled"),
        "p": ("أرسل الجدول، وتصلك معاينة وعرض سعر في نفس يوم العمل غالباً.", "Send the schedule and usually get a proof and quote the same working day."),
        "wa": WA,
    },
}
