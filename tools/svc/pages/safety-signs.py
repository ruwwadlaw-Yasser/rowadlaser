# -*- coding: utf-8 -*-
"""لوحات السلامة والتحذير — تحت اللوحات والتاقات التعريفية"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _eng import GALLERY_NOTE, TAGS_PARENT, g, hero_img, process  # noqa: E402

WA = "مرحباً رواد الليزر، أرغب في عرض سعر للوحات سلامة وتحذير."

PAGE = {
    "slug": "safety-signs",
    "parent": TAGS_PARENT,
    "crumb": ("لوحات السلامة", "Safety signs"),
    "title": (
        "لوحات سلامة وتحذير في جدة | لوحات خطر ومخارج طوارئ ومعدات وقاية — رواد الليزر",
        "Safety Signs in Jeddah | Danger, Emergency Exit &amp; PPE Signs — Ruwwad Laser",
    ),
    "desc": (
        "تصنيع لوحات السلامة في جدة: لوحات تحذير وخطر كهرباء، ممنوع التدخين، ارتداء معدات الوقاية، مخارج الطوارئ وطفايات الحريق — بالعربي والإنجليزي على ألمنيوم وستانلس وأكريليك وPVC، بالألوان القياسية.",
        "Safety sign manufacturing in Jeddah: warning and high-voltage signs, no smoking, PPE mandatory, emergency exit and fire extinguisher signs — Arabic and English on aluminium, stainless, acrylic and PVC in standard colours.",
    ),
    "og_image": "assets/img/svc/tags-safety-set.jpg",
    "service_type": ("لوحات السلامة والتحذير", "Safety and warning signs"),
    "schema_name": ("لوحات السلامة في جدة", "Safety signs in Jeddah"),
    "schema_desc": (
        "تصنيع لوحات السلامة والتحذير في جدة للمصانع والمشاريع والمباني: لوحات تحذير، منع، إلزام، إسعاف وطوارئ، ومعدات الحريق، باللغتين العربية والإنجليزية وبالألوان والرموز القياسية، على الألمنيوم والستانلس والأكريليك وPVC.",
        "Manufacture of safety and warning signs in Jeddah for factories, projects and buildings: warning, prohibition, mandatory, first-aid/emergency and fire-equipment signs in Arabic and English with standard colours and symbols, on aluminium, stainless, acrylic and PVC.",
    ),
    "schema_offers": [
        ("لوحات تحذير وخطر", "Warning and danger signs"),
        ("لوحات منع", "Prohibition signs"),
        ("لوحات إلزام ومعدات وقاية", "Mandatory and PPE signs"),
        ("لوحات مخارج الطوارئ ومعدات الحريق", "Emergency exit and fire equipment signs"),
    ],
    "hero": {
        "eyebrow": ("لوحات سلامة · مصانع ومشاريع", "Safety signs · plants and projects"),
        "h1": ("لوحات السلامة والتحذير", "Safety and warning signs"),
        "sub": (
            "لوحة السلامة يجب أن تُفهم في ثانية واحدة: لون ورمز ونص واضح باللغتين. نصنع لوحات التحذير والمنع والإلزام ومخارج الطوارئ بالألوان القياسية، على مواد تتحمل الشمس والغبار والغسيل في المصانع والمواقع ومداخل المباني.",
            "A safety sign must be understood in one second: a colour, a symbol and clear text in both languages. We make warning, prohibition, mandatory and exit signs in standard colours, on materials that handle sun, dust and washing in plants, sites and building entrances.",
        ),
        "chips": [
            ("ألوان ورموز قياسية", "Standard colours and symbols", "target"),
            ("عربي + إنجليزي", "Arabic + English", "globe"),
            ("داخلي وخارجي", "Indoor and outdoor", "shield"),
            ("مقاسات حسب مسافة الرؤية", "Sized for viewing distance", "sliders"),
        ],
        "img": ("assets/img/svc/tags-safety-set.jpg", ("لوحات سلامة: جهد عالٍ، معدات حريق، ارتداء معدات الوقاية، مخرج طوارئ، ممنوع التدخين", "Safety signs: high voltage, fire equipment, wear PPE, emergency exit, no smoking"), 1200, 900),
        "wa": WA,
    },
    "facts": [
        (("5", "5"), ("فئات لوحات السلامة", "Safety sign categories")),
        (("2", "2"), ("لغتان على كل لوحة", "Two languages on every sign")),
        (("+4", "+4"), ("مواد للداخل والخارج", "Materials for indoor and outdoor")),
        (("6", "6"), ("ساعات لبدء التنفيذ", "Hours to start production")),
    ],
    "intro": {
        "h2": ("لغة لوحات السلامة: لون + رمز + نص", "The language of safety signs: colour + symbol + text"),
        "paras": [
            (
                "تعتمد لوحات السلامة على نظام ألوان وأشكال موحّد عالمياً حتى يفهمها أي شخص بأي لغة: المثلث الأصفر للتحذير، الدائرة الحمراء المشطوبة للمنع، الدائرة الزرقاء للإلزام، والمستطيل الأخضر للطوارئ والإسعاف، والأحمر لمعدات الحريق.",
                "Safety signs rely on a globally unified system of colours and shapes so anyone understands them in any language: yellow triangle for warning, red crossed circle for prohibition, blue circle for mandatory, green rectangle for emergency and first aid, and red for fire equipment.",
            ),
            (
                "ونضيف إلى الرمز نصاً عربياً وإنجليزياً واضحاً، ونختار المادة حسب المكان: ألمنيوم أو ستانلس للخارج والمصانع، أكريليك للمكاتب والمستشفيات، وPVC للمواقع المؤقتة والكميات الاقتصادية.",
                "We add clear Arabic and English text to the symbol, and choose the material by location: aluminium or stainless for outdoors and plants, acrylic for offices and hospitals, and PVC for temporary sites and economical quantities.",
            ),
        ],
        "h3": ("فئات لوحات السلامة", "Safety sign categories"),
        "bullets": [
            ("تحذير (أصفر): خطر كهرباء، أرضية زلقة، رافعة شوكية، سطح ساخن.", "Warning (yellow): high voltage, slippery floor, forklifts, hot surface."),
            ("منع (أحمر): ممنوع التدخين، ممنوع الدخول لغير المصرّح لهم، ممنوع الجوال.", "Prohibition (red): no smoking, authorised personnel only, no mobile phones."),
            ("إلزام (أزرق): ارتدِ الخوذة، النظارات، القفازات، واقي الأذن.", "Mandatory (blue): wear hard hat, goggles, gloves, ear protection."),
            ("طوارئ (أخضر) وحريق (أحمر): مخرج طوارئ، نقطة تجمّع، إسعافات، طفاية، خرطوم.", "Emergency (green) and fire (red): exit, assembly point, first aid, extinguisher, hose reel."),
        ],
    },
    "cards": {
        "eyebrow": ("المواد", "Materials"),
        "h2": ("على أي مادة تُصنع لوحتك؟", "Which material for your sign?"),
        "items": [
            {"icon": "layers", "h3": ("ألمنيوم", "Aluminium"), "p": ("لا يصدأ وخفيف، الأنسب للوحات الخارجية في المواقع والمصانع.", "Rust-free and light, best for outdoor signs on sites and plants."), "href": "aluminum-engraving.html", "more": ("الحفر على الألمنيوم", "Aluminium engraving")},
            {"icon": "shield", "h3": ("ستانلس ستيل", "Stainless steel"), "p": ("للبيئات القاسية والكيميائية، بنقش دائم لا يُمحى.", "For harsh and chemical environments, with permanent marking.")},
            {"icon": "store", "h3": ("أكريليك", "Acrylic"), "p": ("مظهر أنيق للمكاتب والمستشفيات والفنادق.", "An elegant look for offices, hospitals and hotels."), "href": "acrylic-engraving.html", "more": ("الحفر على الأكريليك", "Acrylic engraving")},
            {"icon": "cube", "h3": ("PVC / فوم بورد", "PVC / foam board"), "p": ("الخيار الاقتصادي للمواقع المؤقتة والكميات الكبيرة.", "The economical option for temporary sites and large quantities."), "href": "pvc-abs-engraving.html", "more": ("الحفر على PVC وABS", "PVC and ABS engraving")},
            {"icon": "engrave", "h3": ("ترافوليت", "Traffolyte"), "p": ("لوحات تحذير صغيرة على لوحات الكهرباء والمعدات.", "Small warning labels on electrical boards and equipment."), "href": "traffolyte-engraving.html", "more": ("لوحات الترافوليت", "Traffolyte labels")},
            {"icon": "target", "h3": ("لوحات مخصصة", "Custom signs"), "p": ("نصوص خاصة بمنشأتك: أرقام الطوارئ، نقطة التجمع، تعليمات المعدة.", "Text specific to your site: emergency numbers, assembly point, machine instructions.")},
        ],
    },
    "specs": {
        "soft": True,
        "eyebrow": ("المقاس الصحيح", "The right size"),
        "h2": ("مقاس اللوحة حسب مسافة الرؤية", "Sign size by viewing distance"),
        "cols": [("مسافة الرؤية", "Viewing distance"), ("المقاس المقترح", "Suggested size"), ("مثال", "Example")],
        "rows": [
            [("حتى 3 م", "Up to 3 m"), ("A5 تقريباً 150×200 مم", "About A5, 150×200 mm"), ("لوحات المعدات والأبواب", "Machine and door signs")],
            [("حتى 8 م", "Up to 8 m"), ("A4 تقريباً 200×300 مم", "About A4, 200×300 mm"), ("الممرات والمستودعات", "Corridors and warehouses")],
            [("حتى 15 م", "Up to 15 m"), ("A3 تقريباً 300×400 مم", "About A3, 300×400 mm"), ("مداخل المصانع والمواقع", "Plant and site entrances")],
            [("أكثر من 15 م", "Over 15 m"), ("600 مم فأكثر", "600 mm and above"), ("البوابات والساحات الخارجية", "Gates and outdoor yards")],
        ],
        "note": (
            "المقاسات استرشادية — إن كانت لديك مواصفات مشروع أو متطلبات جهة رقابية فنلتزم بها حرفياً.",
            "Sizes are indicative — if you have a project specification or regulator requirement we follow it exactly.",
        ),
    },
    "gallery": {
        "eyebrow": ("نماذج", "Samples"),
        "h2": ("لوحات السلامة والإرشاد", "Safety and directional signs"),
        "items": [
            ("assets/img/svc/tags-high-voltage-wall.jpg", ("لوحة خطر جهد عالٍ مثبّتة على الجدار", "High voltage danger sign fixed on the wall"), ("مركّبة في الموقع", "Installed on site"), 1200, 900),
            ("assets/img/svc/tags-caution-machinery.jpg", ("لوحة تحذير من الآلات المتحركة", "Caution moving machinery sign"), ("تحذير", "Caution"), 1200, 900),
            ("assets/img/svc/tags-safety-instructions.jpg", ("لوحة تعليمات سلامة ستانلس محفورة", "Engraved stainless safety instructions plate"), ("تعليمات السلامة", "Safety instructions"), 1200, 900),
        ],
        "note": GALLERY_NOTE,
    },
    "process": process(("من قائمة المواقع إلى التركيب", "From the location list to installation")),
    "related": {
        "eyebrow": ("للسلامة", "For safety"),
        "h2": ("منتجات مكمّلة", "Complementary products"),
        "items": [
            {"icon": "target", "href": "loto-safety-tags.html", "h3": ("تاقات لوتو LOTO", "LOTO tags"), "p": ("بطاقات العزل والإغلاق للصيانة.", "Lockout tags for maintenance.")},
            {"icon": "store", "href": "signage-plates.html", "h3": ("اللوحات الإرشادية", "Signage plates"), "p": ("أرقام الأبواب وأسماء الأقسام والاتجاهات.", "Door numbers, department names and directions.")},
            {"icon": "arrow", "href": "route-marker-plates.html", "h3": ("لوحات المسارات", "Route markers"), "p": ("تحذير من الكيابل والأنابيب المدفونة.", "Warning of buried cables and pipes.")},
        ],
    },
    "faq": [
        {
            "q": ("هل اللوحات مطابقة لرموز السلامة القياسية؟", "Do the signs follow standard safety symbols?"),
            "a": (
                "نعم، نستخدم الأشكال والألوان والرموز المعتمدة عالمياً للوحات السلامة، ونضيف النص العربي والإنجليزي. وإن كان مشروعك يشترط مرجعاً محدداً في المواصفات، أرسله ونلتزم به.",
                "Yes, we use the internationally recognised shapes, colours and symbols for safety signs, adding Arabic and English text. If your project specifies a particular reference, send it and we follow it.",
            ),
        },
        {
            "q": ("هل تتحمل اللوحات الشمس في المواقع الخارجية؟", "Do the signs survive outdoor sun?"),
            "a": (
                "للخارج نرشّح الألمنيوم أو الستانلس مع ألوان مقاومة للأشعة فوق البنفسجية أو حفر دائم، لأن اللوحات البلاستيكية الرخيصة تبهت وتتقصف بسرعة تحت شمس جدة.",
                "For outdoors we recommend aluminium or stainless with UV-resistant colours or permanent engraving, because cheap plastic signs fade and crack fast in Jeddah's sun.",
            ),
        },
        {
            "q": ("هل يمكن طلب لوحات بنص خاص بمنشأتنا؟", "Can we order signs with text specific to our site?"),
            "a": (
                "بالتأكيد: أرقام الطوارئ الداخلية، اسم نقطة التجمع، تعليمات تشغيل معدة معينة، أو تحذير خاص بمادة كيميائية — نصممها بنفس لغة لوحات السلامة القياسية.",
                "Certainly: internal emergency numbers, assembly point names, operating instructions for a machine, or a warning specific to a chemical — designed in the same language as standard safety signs.",
            ),
        },
        {
            "q": ("ما طرق التثبيت المتاحة؟", "What fixing options are available?"),
            "a": (
                "ثقوب للبراغي في الزوايا، لاصق صناعي ثنائي الوجه، فواصل (Standoffs) للأكريليك، أو أربطة للتثبيت على السياج والأعمدة في المواقع.",
                "Corner screw holes, industrial double-sided tape, standoffs for acrylic, or ties for fences and poles on sites.",
            ),
        },
    ],
    "form_services": [
        ("لوحات تحذير وخطر", "Warning and danger signs"),
        ("لوحات منع", "Prohibition signs"),
        ("لوحات إلزام ومعدات وقاية", "Mandatory and PPE signs"),
        ("لوحات طوارئ وحريق", "Emergency and fire signs"),
        ("مجموعة كاملة لمنشأة", "Complete set for a facility"),
        ("أخرى / غير متأكد", "Other / not sure"),
    ],
    "form_wa": WA,
    "quote_h2": ("أرسل قائمة لوحات السلامة", "Send your safety sign list"),
    "quote_lead": (
        "اذكر الأنواع والمقاسات والكمية، وهل التركيب داخلي أم خارجي.",
        "Tell us the types, sizes and quantity, and whether installation is indoor or outdoor.",
    ),
    "cta": {
        "h2": ("لوحات سلامة تُفهم في ثانية", "Safety signs understood in a second"),
        "p": ("أرسل القائمة، وتصلك معاينة وعرض سعر في نفس يوم العمل غالباً.", "Send the list and usually get a proof and quote the same working day."),
        "wa": WA,
    },
}
