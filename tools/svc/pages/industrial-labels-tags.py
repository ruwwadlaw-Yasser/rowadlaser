# -*- coding: utf-8 -*-
"""اللوحات والتاقات التعريفية — صفحة أم لمنتجات التعريف الصناعي (تحت الحفر بالليزر)"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _eng import ENG_PARENT, GALLERY_NOTE, g, hero_img, process, why  # noqa: E402

PAGE = {
    "slug": "industrial-labels-tags",
    "parent": ENG_PARENT,
    "crumb": ("اللوحات والتاقات التعريفية", "Labels, plates &amp; tags"),
    "title": (
        "لوحات وتاقات تعريفية محفورة في جدة | لوحات سلامة، تاقات محابس وكيابل، لوتو — رواد الليزر",
        "Engraved Labels, Plates &amp; Tags in Jeddah | Safety Signs, Valve, Cable &amp; LOTO Tags — Ruwwad Laser",
    ),
    "desc": (
        "تصنيع لوحات وتاقات تعريفية محفورة بالليزر في جدة: لوحات إرشادية ولوحات سلامة، تاقات محابس وكيابل، تاقات لوتو، بادجات أسماء، ولوحات مسارات — على الستانلس والألمنيوم والبراص والترافوليت والأكريليك. بدء التنفيذ خلال 6 ساعات.",
        "Laser engraved identification labels and tags in Jeddah: signage plates, safety signs, valve and cable tags, LOTO tags, name badges and route markers — in stainless, aluminium, brass, Traffolyte and acrylic. Production starts within 6 hours.",
    ),
    "og_image": "assets/img/svc/tags-mixed-materials.jpg",
    "service_type": ("لوحات وتاقات تعريفية محفورة", "Engraved identification labels and tags"),
    "schema_name": ("لوحات وتاقات التعريف الصناعي في جدة", "Industrial identification labels and tags in Jeddah"),
    "schema_desc": (
        "تصنيع وحفر لوحات وتاقات التعريف للمصانع والمشاريع والمنشآت في جدة: لوحات إرشادية، لوحات سلامة، لوحات مسارات الخدمات، تاقات المحابس، تاقات الكيابل، تاقات العزل والإغلاق (LOTO)، بادجات الأسماء، والتاقات المعدنية — بالفايبر ليزر وCO2 وCNC حسب المادة.",
        "Manufacturing and engraving of identification plates and tags for factories, projects and facilities in Jeddah: signage plates, safety signs, utility route markers, valve tags, cable ID tags, lockout/tagout tags, name badges and metal tags — using fibre laser, CO2 or CNC depending on the material.",
    ),
    "schema_offers": [
        ("لوحات إرشادية وتعريفية", "Signage plates"),
        ("لوحات السلامة والتحذير", "Safety signs"),
        ("تاقات المحابس", "Valve tags"),
        ("تاقات الكيابل", "Cable ID tags"),
        ("تاقات العزل والإغلاق LOTO", "LOTO safety tags"),
        ("بادجات الأسماء", "Name badges"),
        ("لوحات مسارات الخدمات", "Route marker plates"),
        ("تاقات معدنية وميداليات", "Metal tags and keychains"),
    ],
    "sub_pages": [
        {"href": "signage-plates.html", "name": ("لوحات إرشادية", "Signage plates")},
        {"href": "safety-signs.html", "name": ("لوحات السلامة", "Safety signs")},
        {"href": "valve-tags.html", "name": ("تاقات المحابس", "Valve tags")},
        {"href": "cable-id-tags.html", "name": ("تاقات الكيابل", "Cable ID tags")},
        {"href": "loto-safety-tags.html", "name": ("تاقات لوتو LOTO", "LOTO tags")},
        {"href": "name-badges.html", "name": ("بادجات أسماء", "Name badges")},
        {"href": "route-marker-plates.html", "name": ("لوحات المسارات", "Route markers")},
        {"href": "engraved-tags.html", "name": ("تاقات وميداليات معدنية", "Metal tags &amp; keychains")},
    ],
    "subnav_title": ("اختر نوع اللوحة أو التاق", "Choose the type of plate or tag"),
    "hero": {
        "eyebrow": ("تعريف صناعي · جدة", "Industrial identification · Jeddah"),
        "h1": ("لوحات وتاقات تعريفية محفورة بالليزر", "Laser engraved labels, plates and tags"),
        "sub": (
            "كل منشأة تحتاج تعريفاً واضحاً: محابس مرقّمة، كيابل معروفة المسار، لوحات سلامة مطابقة، وموظفين ببادجات أنيقة. نصنعها لك محفورة لا تُمحى — من معدن أو بلاستيك صناعي — بقائمة واحدة وطلب واحد.",
            "Every facility needs clear identification: numbered valves, traceable cables, compliant safety signs and staff with smart badges. We make them engraved so they never wipe off — in metal or industrial plastic — from one list and one order.",
        ),
        "chips": [
            ("معادن وبلاستيك صناعي", "Metals and industrial plastics", "layers"),
            ("عربي وإنجليزي", "Arabic and English", "globe"),
            ("ترقيم تسلسلي من إكسل", "Serial numbering from Excel", "file"),
            ("بدء خلال 6 ساعات", "Start within 6 hours", "bolt"),
        ],
        "img": ("assets/img/svc/tags-mixed-materials.jpg", ("تاقات محفورة بالليزر من الستانلس والبراص والألمنيوم الملوّن مع سلاسل كروية", "Laser engraved tags in stainless, brass and coloured aluminium with ball chains"), 1200, 900),
        "wa": "مرحباً رواد الليزر، أرغب في عرض سعر للوحات وتاقات تعريفية محفورة.",
    },
    "facts": [
        (("8", "8"), ("أنواع منتجات تعريف", "Identification product types")),
        (("+6", "+6"), ("مواد: ستانلس، ألمنيوم، براص، ترافوليت…", "Materials: stainless, aluminium, brass, Traffolyte…")),
        (("6", "6"), ("ساعات لبدء التنفيذ", "Hours to start production")),
        (("100%", "100%"), ("مراجعة النصوص مقابل قائمتك", "Text checked against your list")),
    ],
    "intro": {
        "h2": ("لماذا التاقات واللوحات المحفورة أفضل من الملصقات؟", "Why engraved tags and plates beat stickers"),
        "paras": [
            (
                "الملصق المطبوع يبهت في شمس جدة، وينفصل مع الرطوبة، ويُمحى بالزيوت ومواد التنظيف. خلال سنة أو سنتين تتحوّل لوحة التعريف إلى قطعة بلا معنى — وهذا بالضبط ما يربك فرق الصيانة ويؤخّر الاستلام في المشاريع.",
                "A printed sticker fades in Jeddah's sun, peels with humidity and wipes off with oil and cleaning agents. Within a year or two an ID label becomes meaningless — exactly what confuses maintenance teams and delays project handover.",
            ),
            (
                "الحفر يغيّر سطح المادة نفسها، فالنص جزء من اللوحة لا طبقة فوقها. لذلك نصنع التاقات واللوحات بالحفر: فايبر ليزر للمعادن، وليزر CO2 أو CNC للترافوليت والأكريليك والـABS — ونختار المادة حسب مكان التركيب: داخلي، خارجي، ساحلي، أو بيئة كيميائية.",
                "Engraving changes the material surface itself, so the text is part of the plate, not a layer on top. That is why we make tags and plates by engraving: fibre laser for metals, CO2 laser or CNC for Traffolyte, acrylic and ABS — and we choose the material for the installation: indoor, outdoor, coastal or chemical environment.",
            ),
        ],
        "h3": ("من يطلب هذه المنتجات عادةً؟", "Who usually orders these products?"),
        "bullets": [
            (
                "مقاولو الكهرباء والميكانيكا (MEP) عند تسليم المشاريع: تاقات المحابس والكيابل ولوحات التوزيع.",
                "MEP contractors at project handover: valve tags, cable tags and distribution board labels.",
            ),
            (
                "المصانع ومحطات المياه والطاقة: لوحات السلامة، تاقات لوتو، ولوحات بيانات المعدات.",
                "Factories, water and power plants: safety signs, LOTO tags and equipment data plates.",
            ),
            (
                "المكاتب والمستشفيات والفنادق: لوحات إرشادية للأبواب والطوابق، وبادجات الموظفين.",
                "Offices, hospitals and hotels: door and floor signage plates and staff name badges.",
            ),
            (
                "الشركات والأفراد: تاقات معدنية، ميداليات، وتاقات تعريف للحيوانات الأليفة والحقائب.",
                "Companies and individuals: metal tags, keychains, pet and luggage ID tags.",
            ),
        ],
    },
    "cards": {
        "eyebrow": ("منتجات التعريف", "Identification products"),
        "h2": ("اختر ما تحتاجه منشأتك", "Choose what your facility needs"),
        "grid": "grid-4",
        "items": [
            {
                "icon": "store",
                "h3": ("لوحات إرشادية", "Signage plates"),
                "p": ("أرقام أبواب، أسماء أقسام، واتجاهات للمكاتب والمستشفيات.", "Door numbers, department names and directions for offices and hospitals."),
                "href": "signage-plates.html",
                "more": ("اللوحات الإرشادية", "Signage plates"),
            },
            {
                "icon": "shield",
                "h3": ("لوحات السلامة", "Safety signs"),
                "p": ("تحذير، منع، إلزام، ومخارج طوارئ بالألوان القياسية.", "Warning, prohibition, mandatory and emergency exit signs in standard colours."),
                "href": "safety-signs.html",
                "more": ("لوحات السلامة", "Safety signs"),
            },
            {
                "icon": "sliders",
                "h3": ("تاقات المحابس", "Valve tags"),
                "p": ("أقراص مرقّمة لكل محبس تطابق مخطط الأنابيب.", "Numbered discs for every valve, matching the piping drawing."),
                "href": "valve-tags.html",
                "more": ("تاقات المحابس", "Valve tags"),
            },
            {
                "icon": "bolt",
                "h3": ("تاقات الكيابل", "Cable ID tags"),
                "p": ("تعريف كل كيبل بمساره ودائرته — تُثبّت بأربطة ستانلس.", "Each cable identified by route and circuit — fixed with stainless ties."),
                "href": "cable-id-tags.html",
                "more": ("تاقات الكيابل", "Cable ID tags"),
            },
            {
                "icon": "target",
                "h3": ("تاقات لوتو LOTO", "LOTO tags"),
                "p": ("بطاقات العزل والإغلاق أثناء الصيانة — خطر، مقفل، لا تشغّل.", "Lockout/tagout tags during maintenance — danger, locked, do not operate."),
                "href": "loto-safety-tags.html",
                "more": ("تاقات لوتو", "LOTO tags"),
            },
            {
                "icon": "user",
                "h3": ("بادجات أسماء", "Name badges"),
                "p": ("بادجات معدنية أو أكريليك بمغناطيس أو دبوس، بشعار الشركة.", "Metal or acrylic badges with magnet or pin, carrying your logo."),
                "href": "name-badges.html",
                "more": ("بادجات الأسماء", "Name badges"),
            },
            {
                "icon": "arrow",
                "h3": ("لوحات المسارات", "Route markers"),
                "p": ("علامات أرضية تحدد مسار المياه والغاز والكيابل المدفونة.", "Ground markers showing buried water, gas and cable routes."),
                "href": "route-marker-plates.html",
                "more": ("لوحات المسارات", "Route markers"),
            },
            {
                "icon": "engrave",
                "h3": ("تاقات وميداليات", "Tags and keychains"),
                "p": ("تاقات معدنية، ميداليات مفاتيح، وتاقات للحيوانات والأصول.", "Metal tags, keychains, pet tags and asset tags."),
                "href": "engraved-tags.html",
                "more": ("التاقات المعدنية", "Metal tags"),
            },
        ],
    },
    "specs": {
        "soft": True,
        "eyebrow": ("اختيار المادة", "Choosing the material"),
        "h2": ("أي مادة تناسب لوحتك؟", "Which material suits your plate?"),
        "cols": [("المادة", "Material"), ("الأنسب لـ", "Best for"), ("طريقة الحفر", "Engraving method")],
        "rows": [
            [
                ("ستانلس ستيل 316", "Stainless steel 316"),
                ("الخارج، المناطق الساحلية، المحابس، تاقات الكيابل.", "Outdoors, coastal areas, valves, cable tags."),
                ("فايبر ليزر — نقش أسود أو حفر غائر", "Fibre laser — black marking or recessed"),
            ],
            [
                ("ألمنيوم مؤكسد", "Anodised aluminium"),
                ("لوحات ملوّنة خفيفة، لوحات تحكم، بادجات.", "Light coloured plates, control panels, badges."),
                ("فايبر ليزر — يكشف المعدن الفضي", "Fibre laser — reveals the silver metal"),
            ],
            [
                ("براص / نحاس", "Brass / copper"),
                ("لوحات فاخرة، دروع، تاقات محابس تقليدية.", "Premium plaques, awards, traditional valve tags."),
                ("فايبر ليزر — حفر غائر مع تعبئة لون", "Fibre laser — recessed with colour fill"),
            ],
            [
                ("ترافوليت (بلاستيك طبقات)", "Traffolyte (laminate)"),
                ("لوحات التوزيع الكهربائية ولوحات التحكم داخلياً.", "Indoor electrical boards and control panels."),
                ("CNC أو ليزر CO2 — يكشف لون الطبقة الداخلية", "CNC or CO2 laser — reveals the core colour"),
            ],
            [
                ("أكريليك", "Acrylic"),
                ("لوحات المكاتب والاستقبال والدروع.", "Office, reception plaques and awards."),
                ("ليزر CO2 — حفر مثلّج أو قص بالشكل", "CO2 laser — frosted engraving or contour cut"),
            ],
            [
                ("PVC / ABS", "PVC / ABS"),
                ("لوحات إرشادية اقتصادية وتاقات لوتو.", "Economical signs and LOTO tags."),
                ("CNC للـPVC، وليزر أو CNC للـABS", "CNC for PVC; laser or CNC for ABS"),
            ],
        ],
        "note": (
            "لا تعرف أي مادة تختار؟ أخبرنا أين ستُركَّب اللوحة (داخل/خارج، قرب البحر، حرارة، زيوت) ونرشّح لك المادة الأنسب والأوفر.",
            "Not sure which material? Tell us where the plate will be installed (indoor/outdoor, near the sea, heat, oils) and we recommend the best-value option.",
        ),
    },
    "gallery": {
        "eyebrow": ("نماذج", "Samples"),
        "h2": ("أمثلة على منتجات التعريف", "Examples of identification products"),
        "items": [
            ("assets/img/svc/tags-valves-pipeline.jpg", ("تاقات محابس مرقّمة معلّقة على خط أنابيب", "Numbered valve tags hanging on a pipeline"), ("تاقات المحابس", "Valve tags"), 1200, 900),
            ("assets/img/svc/tags-high-voltage-wall.jpg", ("لوحة خطر جهد عالٍ مثبّتة بجانب لوحة كهرباء", "High voltage danger sign fixed beside an electrical panel"), ("لوحات السلامة", "Safety signs"), 1200, 900),
            ("assets/img/svc/tags-cable-bundle.jpg", ("تاقات ستانلس مرقّمة مثبّتة على حزمة كيابل", "Numbered stainless tags fixed on a cable bundle"), ("تاقات الكيابل", "Cable tags"), 1200, 900),
        ],
        "note": GALLERY_NOTE,
    },
    "process": process(("من القائمة إلى التركيب", "From the list to installation")),
    "why": why(),
    "related": {
        "eyebrow": ("حسب المادة", "By material"),
        "h2": ("الحفر على مواد التعريف", "Engraving on identification materials"),
        "items": [
            {
                "icon": "engrave",
                "href": "traffolyte-engraving.html",
                "h3": ("لوحات ترافوليت", "Traffolyte labels"),
                "p": ("المادة القياسية للوحات التوزيع الكهربائية والتحكم.", "The standard material for electrical and control panel labels."),
            },
            {
                "icon": "layers",
                "href": "aluminum-engraving.html",
                "h3": ("الحفر على الألمنيوم", "Aluminium engraving"),
                "p": ("لوحات مؤكسدة بألوان متعددة، خفيفة ومقاومة للصدأ.", "Anodised plates in many colours, light and rust-free."),
            },
            {
                "icon": "file",
                "href": "metal-nameplates-serial-numbers.html",
                "h3": ("لوحات البيانات والأرقام التسلسلية", "Data plates and serial numbers"),
                "p": ("لوحات المعدات والآلات بمواصفاتها ورقمها التسلسلي.", "Equipment and machine plates with specs and serial number."),
            },
        ],
    },
    "faq": [
        {
            "q": ("هل يمكن إرسال قائمة طويلة من الأرقام في ملف إكسل؟", "Can I send a long list of numbers in Excel?"),
            "a": (
                "نعم، وهذه أسهل طريقة. أرسل جدولاً فيه نص كل تاق (مثلاً رقم المحبس ونوع الخط)، ونربطه مباشرة بملف الحفر فيُحفر كل تاق بنصه دون نسخ يدوي — ما يمنع الأخطاء في الطلبات التي تحتوي مئات التاقات.",
                "Yes, and it is the easiest way. Send a sheet with each tag's text (for example valve number and line type) and we link it directly to the engraving file, so every tag is engraved with its own text without manual retyping — preventing errors in orders with hundreds of tags.",
            ),
        },
        {
            "q": ("هل تنفّذون باللغتين العربية والإنجليزية؟", "Do you engrave in both Arabic and English?"),
            "a": (
                "نعم. نحفر الخط العربي بنفس وضوح الإنجليزي، ويمكن الجمع بين اللغتين في نفس اللوحة — وهو المطلوب عادة في لوحات السلامة والإرشاد داخل المملكة.",
                "Yes. We engrave Arabic script as clearly as English, and both languages can share the same plate — usually required for safety and directional signs in Saudi Arabia.",
            ),
        },
        {
            "q": ("كم تستغرق طلبية تاقات لمشروع كامل؟", "How long does a full project tag order take?"),
            "a": (
                "يبدأ التنفيذ خلال 6 ساعات من اعتماد المعاينة. الطلبات الصغيرة تُسلَّم عادة في يوم أو يومين، والطلبات الكبيرة نحدّد لها جدولاً واضحاً مع عرض السعر، ويمكن التسليم على دفعات حسب أولويات المشروع.",
                "Production starts within 6 hours of proof approval. Small orders usually ship in a day or two; large ones get a clear schedule with the quote, and can be delivered in batches by project priority.",
            ),
        },
        {
            "q": ("هل توفرون وسائل التثبيت؟", "Do you supply the fixings?"),
            "a": (
                "نعم: أربطة كيابل ستانلس، سلاسل كرات، حلقات S، براغي ومسامير تثبيت، لاصق صناعي ثنائي الوجه، أو مغناطيس ودبابيس للبادجات. حدّد طريقة التركيب ونجهّز اللوحات بالثقوب المناسبة.",
                "Yes: stainless cable ties, ball chains, S-hooks, screws and rivets, industrial double-sided tape, or magnets and pins for badges. Tell us how they will be installed and we prepare the plates with suitable holes.",
            ),
        },
    ],
    "form_services": [
        ("تاقات محابس", "Valve tags"),
        ("تاقات كيابل", "Cable ID tags"),
        ("لوحات سلامة", "Safety signs"),
        ("تاقات لوتو LOTO", "LOTO tags"),
        ("لوحات إرشادية", "Signage plates"),
        ("بادجات أسماء", "Name badges"),
        ("لوحات مسارات", "Route marker plates"),
        ("تاقات وميداليات معدنية", "Metal tags and keychains"),
        ("أخرى / غير متأكد", "Other / not sure"),
    ],
    "form_wa": "مرحباً رواد الليزر، أرغب في عرض سعر للوحات وتاقات تعريفية محفورة.",
    "quote_h2": ("أرسل قائمة التاقات أو اللوحات", "Send your list of tags or plates"),
    "quote_lead": (
        "اذكر نوع المنتج والكمية ومكان التركيب، وأرفق قائمة النصوص إن وجدت — نرد عليك بمعاينة وعرض سعر.",
        "Tell us the product type, quantity and installation place, and attach the text list if you have one — we reply with a proof and a quote.",
    ),
    "cta": {
        "h2": ("تعريف واضح لكل محبس وكيبل وباب", "Clear identification for every valve, cable and door"),
        "p": (
            "أرسل القائمة اليوم، واستلم معاينة وعرض سعر في نفس يوم العمل غالباً.",
            "Send the list today and usually receive a proof and a quote the same working day.",
        ),
        "wa": "مرحباً رواد الليزر، أرغب في عرض سعر للوحات وتاقات تعريفية محفورة.",
    },
}
