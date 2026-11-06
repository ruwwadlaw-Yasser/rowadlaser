# -*- coding: utf-8 -*-
"""الحفر على PVC وABS — تحت الحفر والنقش بالليزر"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _eng import ENG_PARENT, GALLERY_NOTE, g, hero_img, process  # noqa: E402

WA = "مرحباً رواد الليزر، أرغب في عرض سعر للوحات PVC أو ABS محفورة."

PAGE = {
    "slug": "pvc-abs-engraving",
    "parent": ENG_PARENT,
    "crumb": ("الحفر على PVC وABS", "PVC and ABS engraving"),
    "title": (
        "لوحات PVC وABS محفورة في جدة | لوحات بلاستيك إرشادية وتعريفية — رواد الليزر",
        "PVC &amp; ABS Engraving in Jeddah | Engraved Plastic Signs and Labels — Ruwwad Laser",
    ),
    "desc": (
        "حفر وتصنيع لوحات PVC وABS في جدة: لوحات إرشادية وأبواب، لوحات سلامة، تسميات معدات، وتاقات — بلاستيك طبقتين بألوان متعددة، خفيف واقتصادي ولا يصدأ. الخيار الأوفر للكميات الكبيرة.",
        "PVC and ABS engraving and signs in Jeddah: door and directional signs, safety signs, equipment labels and tags — two-layer plastic in many colours, light, economical and rust-free. The best-value option for large quantities.",
    ),
    "og_image": "assets/img/svc/tags-plastic-signs.jpg",
    "service_type": ("الحفر على PVC وABS", "PVC and ABS engraving"),
    "schema_name": ("لوحات PVC وABS المحفورة في جدة", "Engraved PVC and ABS signs in Jeddah"),
    "schema_desc": (
        "تصنيع لوحات وتسميات بلاستيكية محفورة من ABS ثنائي الطبقة وPVC في جدة: لوحات إرشادية، لوحات سلامة، تسميات معدات ولوحات تحكم، وتاقات تعريف، بالحفر الدوّار CNC أو الليزر حسب نوع المادة.",
        "Manufacture of engraved plastic signs and labels in two-layer ABS and PVC in Jeddah: directional signs, safety signs, equipment and panel labels and ID tags, by rotary CNC engraving or laser depending on the material.",
    ),
    "schema_offers": [
        ("لوحات ABS ثنائية الطبقة", "Two-layer ABS signs"),
        ("لوحات PVC محفورة", "Engraved PVC signs"),
        ("لوحات أبواب وإرشاد بلاستيكية", "Plastic door and directional signs"),
        ("تسميات معدات بلاستيكية", "Plastic equipment labels"),
    ],
    "hero": {
        "eyebrow": ("PVC · ABS · بلاستيك محفور", "PVC · ABS · engraved plastic"),
        "h1": ("لوحات PVC وABS محفورة", "Engraved PVC and ABS signs"),
        "sub": (
            "عندما تحتاج عشرات أو مئات اللوحات بسعر مناسب، البلاستيك المحفور هو الحل العملي: ABS بطبقتين لونيتين يظهر الحفر فيه بلون مختلف، وPVC خفيف وقوي. لوحات أبواب وإرشاد وسلامة وتسميات معدات — لا تصدأ ولا تبهت حروفها.",
            "When you need dozens or hundreds of signs at a sensible price, engraved plastic is the practical answer: two-colour ABS where engraving shows a different colour, and light, strong PVC. Door, directional and safety signs and equipment labels — rust-free with letters that never fade.",
        ),
        "chips": [
            ("الخيار الأوفر", "Best value", "check"),
            ("ألوان متعددة", "Many colours", "target"),
            ("خفيف ولا يصدأ", "Light and rust-free", "shield"),
            ("للكميات الكبيرة", "For large quantities", "layers"),
        ],
        "img": ("assets/img/svc/tags-plastic-signs.jpg", ("لوحات بلاستيك محفورة: مكتب، استقبال، دورات مياه، قاعة اجتماعات", "Engraved plastic signs: office, reception, restrooms, conference room"), 1200, 670),
        "wa": WA,
    },
    "facts": [
        (("+10", "+10"), ("تركيبات ألوان ABS", "ABS colour combinations")),
        (("1.5 – 3 mm", "1.5 – 3 mm"), ("السماكات الشائعة", "Common thicknesses")),
        (("0", "0"), ("صدأ أو تآكل", "Rust or corrosion")),
        (("6", "6"), ("ساعات لبدء التنفيذ", "Hours to start production")),
    ],
    "intro": {
        "h2": ("ABS وPVC: ما الفرق ومتى نستخدم كلاً منهما؟", "ABS and PVC: the difference and when to use each"),
        "paras": [
            (
                "ABS ثنائي الطبقة (المعروف أيضاً بلوح الحفر) يتكون من طبقة سطحية رقيقة بلون فوق قلب بلون آخر — مثل الترافوليت لكنه أخف وأكثر مرونة وأوفر. عند الحفر يظهر النص بلون القلب، فتحصل على لوحة بلونين دون أي طباعة. يناسب لوحات الأبواب والإرشاد وتسميات المعدات وتاقات اللوتو.",
                "Two-layer ABS (also called engraving laminate) has a thin coloured cap over a core of another colour — like Traffolyte but lighter, more flexible and more economical. Engraving reveals the core colour, giving a two-tone sign with no printing. It suits door and directional signs, equipment labels and LOTO tags.",
            ),
            (
                "أما PVC (والفوم بورد) فلوح صلب وخفيف، يُقصّ بالشكل ويُحفر أو تُضاف عليه طبقات وألوان، ويُستخدم للوحات الأكبر والمواقع المؤقتة واللوحات الاقتصادية. ولأسباب تتعلق بالسلامة لا يُقصّ PVC بالليزر — نحفره ونقصّه بماكينات CNC، بينما يمكن تنفيذ ABS بالليزر أو CNC حسب التصميم.",
                "PVC (and foam board) is a rigid, light sheet that's cut to shape and engraved or layered with colours, used for larger signs, temporary sites and economical signage. For safety reasons PVC is not laser cut — we engrave and cut it on CNC machines, while ABS can be done by laser or CNC depending on the design.",
            ),
        ],
        "h3": ("متى يكون البلاستيك المحفور الخيار الأفضل؟", "When engraved plastic is the best choice"),
        "bullets": [
            ("كميات كبيرة من لوحات الأبواب والمكاتب في مبنى واحد بميزانية محددة.", "Large quantities of door and office signs in one building on a set budget."),
            ("البيئات الرطبة أو الكيميائية حيث يُفضّل البلاستيك على المعدن.", "Humid or chemical environments where plastic is preferred to metal."),
            ("المواقع المؤقتة ومشاريع الإنشاء خلال فترة التنفيذ.", "Temporary sites and construction projects during the build phase."),
            ("تسميات المعدات ولوحات التحكم داخل المصانع والورش.", "Equipment and control panel labels inside plants and workshops."),
        ],
    },
    "cards": {
        "eyebrow": ("الاستخدامات", "Uses"),
        "h2": ("ماذا نصنع من PVC وABS؟", "What we make in PVC and ABS"),
        "items": [
            {"icon": "store", "h3": ("لوحات الأبواب والمكاتب", "Door and office signs"), "p": ("اسم ورقم الغرفة بلونين، بلاصق أو براغي.", "Room name and number in two colours, with adhesive or screws."), "href": "signage-plates.html", "more": ("اللوحات الإرشادية", "Signage plates")},
            {"icon": "shield", "h3": ("لوحات السلامة", "Safety signs"), "p": ("مخارج الطوارئ وطفايات الحريق ومعدات الوقاية.", "Emergency exits, fire extinguishers and PPE."), "href": "safety-signs.html", "more": ("لوحات السلامة", "Safety signs")},
            {"icon": "target", "h3": ("تاقات لوتو", "LOTO tags"), "p": ("تاقات ABS خفيفة قابلة للكتابة وإعادة الاستخدام.", "Light, writable, reusable ABS tags."), "href": "loto-safety-tags.html", "more": ("تاقات لوتو", "LOTO tags")},
            {"icon": "sliders", "h3": ("تسميات المعدات", "Equipment labels"), "p": ("أسماء الأجهزة والمفاتيح ولوحات التشغيل.", "Device names, switches and operating panels.")},
            {"icon": "arrow", "h3": ("لوحات الاتجاهات", "Directional signs"), "p": ("أسهم وأسماء أقسام بألوان موحّدة.", "Arrows and department names in unified colours.")},
            {"icon": "cube", "h3": ("لوحات بأشكال مخصصة", "Custom-shaped signs"), "p": ("قصّ بالشكل والشعار حسب تصميمك.", "Cut to any shape and logo per your design.")},
        ],
    },
    "specs": {
        "soft": True,
        "eyebrow": ("مقارنة", "Comparison"),
        "h2": ("ABS أم PVC أم ترافوليت؟", "ABS, PVC or Traffolyte?"),
        "cols": [("المادة", "Material"), ("المميزات", "Advantages"), ("الأنسب لـ", "Best for")],
        "rows": [
            [("ABS ثنائي الطبقة", "Two-layer ABS"), ("خفيف، مرن، ألوان كثيرة، اقتصادي", "Light, flexible, many colours, economical"), ("لوحات الأبواب وتاقات لوتو والتسميات", "Door signs, LOTO tags and labels")],
            [("PVC / فوم بورد", "PVC / foam board"), ("صلب، خفيف، مقاسات كبيرة", "Rigid, light, large sizes"), ("اللوحات الكبيرة والمواقع المؤقتة", "Large signs and temporary sites")],
            [("ترافوليت", "Traffolyte"), ("أصلب، يتحمل الحرارة، معيار الكهرباء", "Harder, heat-tolerant, the electrical standard"), ("لوحات التوزيع الكهربائية", "Electrical distribution boards")],
            [("أكريليك", "Acrylic"), ("شفاف وأنيق", "Clear and elegant"), ("الاستقبال والمكاتب الفاخرة", "Reception and premium offices")],
        ],
    },
    "gallery": {
        "eyebrow": ("نماذج", "Samples"),
        "h2": ("لوحات بلاستيكية محفورة", "Engraved plastic signs"),
        "items": [
            g("ill-pvc-abs-engraving", ("لوحات ABS وPVC محفورة بألوان متعددة", "Engraved ABS and PVC signs in several colours"), ("ألوان متعددة", "Several colours")),
            ("assets/img/svc/tags-panel-labels.jpg", ("تسميات ملوّنة للوحات الكهرباء", "Coloured labels for electrical panels"), ("لوحات الكهرباء", "Electrical panels"), 1200, 900),
            ("assets/img/svc/tags-office-signs.jpg", ("لوحات إرشادية للمكاتب", "Office signage plates"), ("لوحات إرشادية", "Signage plates"), 1200, 900),
        ],
        "note": GALLERY_NOTE,
    },
    "process": process(),
    "related": {
        "eyebrow": ("مواد أخرى", "Other materials"),
        "h2": ("خيارات أخرى للوحاتك", "Other options for your signs"),
        "items": [
            {"icon": "engrave", "href": "traffolyte-engraving.html", "h3": ("لوحات الترافوليت", "Traffolyte labels"), "p": ("للوحات الكهرباء والتحكم.", "For electrical and control panels.")},
            {"icon": "store", "href": "acrylic-engraving.html", "h3": ("الحفر على الأكريليك", "Acrylic engraving"), "p": ("لوحات ودروع شفافة أنيقة.", "Elegant clear plaques and awards.")},
            {"icon": "layers", "href": "aluminum-engraving.html", "h3": ("الحفر على الألمنيوم", "Aluminium engraving"), "p": ("بديل معدني خفيف للوحات الخارجية.", "A light metal alternative for outdoor signs.")},
        ],
    },
    "faq": [
        {
            "q": ("لماذا لا تقصّون PVC بالليزر؟", "Why don't you laser cut PVC?"),
            "a": (
                "قص PVC بالليزر يطلق غازات ضارة وأكّالة تضر بالعاملين وبالمعدات، لذلك نحفره ونقصّه بماكينات CNC الدوّارة بأمان ونتيجة نظيفة. أما ABS فيمكن تنفيذه بالليزر أو CNC.",
                "Laser cutting PVC releases harmful, corrosive gases that hurt people and equipment, so we engrave and cut it safely on rotary CNC machines with a clean result. ABS can be done by laser or CNC.",
            ),
        },
        {
            "q": ("هل اللوحات البلاستيكية تتحمل الخارج؟", "Do plastic signs survive outdoors?"),
            "a": (
                "هناك ألواح ABS مقاومة للأشعة فوق البنفسجية تصلح لفترات طويلة في الخارج، لكن للوحات المعرّضة لشمس جدة طوال اليوم لسنوات نرشّح الألمنيوم أو الستانلس.",
                "UV-stable ABS sheets handle long outdoor periods, but for signs in Jeddah's full sun for years we recommend aluminium or stainless.",
            ),
        },
        {
            "q": ("ما ألوان ABS المتاحة؟", "Which ABS colours are available?"),
            "a": (
                "أشهرها: أبيض/أسود، أسود/أبيض، أحمر/أبيض، أزرق/أبيض، أخضر/أبيض، أصفر/أسود، فضي/أسود، وذهبي/أسود. أرسل ألوان هويتك ونقترح أقرب تركيبة.",
                "The most popular: white/black, black/white, red/white, blue/white, green/white, yellow/black, silver/black and gold/black. Send your brand colours and we suggest the closest combination.",
            ),
        },
        {
            "q": ("هل يمكن إضافة شعار على اللوحات البلاستيكية؟", "Can a logo be added to plastic signs?"),
            "a": (
                "نعم، يُحفر الشعار بنفس طريقة النص بلون القلب، أو يُقصّ شعار منفصل بلون آخر ويُثبّت على اللوحة لمظهر بارز.",
                "Yes, the logo is engraved like the text in the core colour, or a separate logo is cut in another colour and fixed on for a raised look.",
            ),
        },
    ],
    "form_services": [
        ("لوحات ABS محفورة", "Engraved ABS signs"),
        ("لوحات PVC", "PVC signs"),
        ("لوحات أبواب ومكاتب", "Door and office signs"),
        ("تسميات معدات", "Equipment labels"),
        ("أخرى / غير متأكد", "Other / not sure"),
    ],
    "form_wa": WA,
    "quote_h2": ("أرسل قائمة اللوحات", "Send your sign list"),
    "quote_lead": (
        "اذكر الألوان والمقاسات والكمية ومكان التركيب.",
        "Tell us the colours, sizes, quantity and installation location.",
    ),
    "cta": {
        "h2": ("لوحات عملية بسعر مناسب", "Practical signs at a sensible price"),
        "p": ("أرسل القائمة، وتصلك معاينة وعرض سعر في نفس يوم العمل غالباً.", "Send the list and usually get a proof and quote the same working day."),
        "wa": WA,
    },
}
