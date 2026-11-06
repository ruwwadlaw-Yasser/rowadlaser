# -*- coding: utf-8 -*-
"""تاقات لوتو LOTO (العزل والإغلاق) — تحت اللوحات والتاقات التعريفية"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _eng import GALLERY_NOTE, TAGS_PARENT, g, hero_img, process  # noqa: E402

WA = "مرحباً رواد الليزر، أرغب في عرض سعر لتاقات لوتو (LOTO) محفورة."

PAGE = {
    "slug": "loto-safety-tags",
    "parent": TAGS_PARENT,
    "crumb": ("تاقات لوتو LOTO", "LOTO safety tags"),
    "title": (
        "تاقات لوتو LOTO في جدة | بطاقات العزل والإغلاق «خطر لا تشغّل» — رواد الليزر",
        "LOTO Safety Tags in Jeddah | Lockout/Tagout “Danger Do Not Operate” — Ruwwad Laser",
    ),
    "desc": (
        "تاقات لوتو (Lockout/Tagout) محفورة في جدة: بطاقات «خطر — لا تشغّل» و«معدة مقفلة» بالعربي والإنجليزي، من بلاستيك صناعي أو ألمنيوم، مع حقل اسم الفني وتاريخ العزل. لبرامج السلامة في المصانع والمحطات.",
        "Engraved lockout/tagout tags in Jeddah: “Danger — Do Not Operate” and “Locked Out” tags in Arabic and English, in industrial plastic or aluminium, with fields for technician name and date. For plant safety programmes.",
    ),
    "og_image": "assets/img/svc/tags-loto-isolator.jpg",
    "service_type": ("تاقات العزل والإغلاق LOTO", "Lockout/tagout safety tags"),
    "schema_name": ("تاقات لوتو LOTO المحفورة في جدة", "Engraved LOTO tags in Jeddah"),
    "schema_desc": (
        "تصنيع تاقات العزل والإغلاق (LOTO) المحفورة في جدة: بطاقات خطر ومعدة مقفلة وتنبيه، باللغتين العربية والإنجليزية، من ABS والألمنيوم المؤكسد والستانلس، مع ترقيم وشعار الشركة، لبرامج السلامة في المصانع ومحطات الطاقة والمياه.",
        "Manufacture of engraved lockout/tagout (LOTO) tags in Jeddah: danger, locked-out and caution tags in Arabic and English, in ABS, anodised aluminium and stainless, with numbering and company logo, for safety programmes in factories, power and water plants.",
    ),
    "schema_offers": [
        ("تاقات خطر لا تشغّل", "Danger do-not-operate tags"),
        ("تاقات معدة مقفلة", "Equipment locked-out tags"),
        ("تاقات أقفال شخصية مرقّمة", "Numbered personal lock tags"),
        ("تاقات لوتو بشعار الشركة", "Branded LOTO tags"),
    ],
    "hero": {
        "eyebrow": ("Lockout / Tagout · سلامة", "Lockout / Tagout · safety"),
        "h1": ("تاقات لوتو LOTO للعزل والإغلاق", "LOTO lockout/tagout tags"),
        "sub": (
            "عند صيانة أي معدة، تاق اللوتو هو الرسالة التي تقول لكل من في الموقع: «لا تشغّل — هناك من يعمل هنا». نصنعها محفورة بالعربي والإنجليزي، بألوان السلامة القياسية، ومتينة بما يكفي لتُستخدم مئات المرات.",
            "During any equipment maintenance, the LOTO tag tells everyone on site: “Do not operate — someone is working here.” We make them engraved in Arabic and English, in standard safety colours, durable enough for hundreds of uses.",
        ),
        "chips": [
            ("عربي + إنجليزي", "Arabic + English", "globe"),
            ("ألوان السلامة القياسية", "Standard safety colours", "target"),
            ("ترقيم لكل فني", "Numbered per technician", "user"),
            ("قابلة لإعادة الاستخدام", "Reusable", "check"),
        ],
        "img": ("assets/img/svc/tags-loto-isolator.jpg", ("تاق لوتو أحمر «خطر لا تشغّل» مع قفل أمان على مفتاح عزل كهربائي", "Red DANGER DO NOT OPERATE LOTO tag with a safety padlock on an isolator switch"), 1200, 900),
        "wa": WA,
    },
    "facts": [
        (("3", "3"), ("ألوان أساسية: أحمر، أسود، أصفر", "Core colours: red, black, yellow")),
        (("2", "2"), ("لغتان على نفس التاق", "Two languages on one tag")),
        (("100%", "100%"), ("فحص كل رقم وحرف قبل التسليم", "Every number and letter checked")),
        (("6", "6"), ("ساعات لبدء التنفيذ", "Hours to start production")),
    ],
    "intro": {
        "h2": ("ما هو نظام لوتو LOTO؟", "What is the LOTO system?"),
        "paras": [
            (
                "العزل والإغلاق (Lockout/Tagout) إجراء سلامة يُطبَّق قبل صيانة أي معدة: يُفصل مصدر الطاقة، ويُقفل بقفل شخصي، ويُعلَّق عليه تاق يحدد من قام بالعزل ولماذا ومتى. لا يُزال التاق إلا بيد صاحبه بعد انتهاء العمل.",
                "Lockout/tagout is a safety procedure applied before servicing any equipment: the energy source is isolated, locked with a personal padlock, and a tag is hung stating who isolated it, why and when. Only its owner removes the tag after work is complete.",
            ),
            (
                "التاقات المطبوعة على الورق المقوّى تتلف بسرعة في بيئة المصانع. التاق المحفور من بلاستيك صناعي أو ألمنيوم يبقى واضحاً رغم الزيوت والحرارة، ويمكن الكتابة عليه بقلم دائم ومسحه وإعادة استخدامه.",
                "Printed cardboard tags wear out fast on a factory floor. An engraved tag in industrial plastic or aluminium stays legible despite oil and heat, and can be written on with a marker, wiped and reused.",
            ),
        ],
        "h3": ("أنواع تاقات اللوتو الشائعة", "Common LOTO tag types"),
        "bullets": [
            ("خطر — لا تشغّل (DANGER — DO NOT OPERATE): أحمر، للتحذير الأشد.", "DANGER — DO NOT OPERATE: red, for the strongest warning."),
            ("معدة مقفلة (EQUIPMENT LOCKED OUT): أسود أو أحمر، يوضع مع القفل.", "EQUIPMENT LOCKED OUT: black or red, placed with the lock."),
            ("تنبيه — لا تُزِل التاق (CAUTION — DO NOT REMOVE): أصفر.", "CAUTION — DO NOT REMOVE TAG: yellow."),
            ("تاق القفل الشخصي: اسم الفني وصورته أو رقمه، يبقى مع قفله دائماً.", "Personal lock tag: the technician's name and photo or number, kept with their lock."),
        ],
    },
    "cards": {
        "eyebrow": ("خيارات", "Options"),
        "h2": ("اختر نوع التاق المناسب لبرنامجك", "Choose the tag for your programme"),
        "items": [
            {"icon": "cube", "h3": ("ABS صناعي", "Industrial ABS"), "p": ("خفيف، مقاوم للزيوت، ويُكتب عليه بقلم دائم ويُمسح.", "Light, oil-resistant, writable with a marker and wipeable.")},
            {"icon": "layers", "h3": ("ألمنيوم مؤكسد", "Anodised aluminium"), "p": ("أكثر متانة للمعدات الثقيلة والحرارة العالية.", "More durable for heavy equipment and high heat.")},
            {"icon": "shield", "h3": ("ستانلس ستيل", "Stainless steel"), "p": ("لتاقات الأقفال الشخصية الدائمة والبيئات الكيميائية.", "For permanent personal lock tags and chemical environments.")},
            {"icon": "user", "h3": ("تاق شخصي مرقّم", "Numbered personal tag"), "p": ("اسم كل فني ورقمه وقسمه — يُصنع لفريقك كاملاً بقائمة واحدة.", "Each technician's name, number and department — made for the whole team from one list.")},
            {"icon": "file", "h3": ("حقول للكتابة", "Write-in fields"), "p": ("الاسم، التاريخ، القسم، سبب العزل — محفورة كخطوط ثابتة.", "Name, date, department, reason — engraved as permanent lines.")},
            {"icon": "target", "h3": ("شعار الشركة", "Company logo"), "p": ("إضافة الشعار ورقم الطوارئ الداخلي على ظهر التاق.", "Add your logo and internal emergency number on the back.")},
        ],
    },
    "specs": {
        "soft": True,
        "eyebrow": ("مواصفات", "Specs"),
        "h2": ("المقاسات والمواد الشائعة", "Common sizes and materials"),
        "cols": [("البند", "Item"), ("الخيار المعتاد", "Usual option"), ("ملاحظة", "Note")],
        "rows": [
            [("المقاس", "Size"), ("75×145 مم تقريباً", "About 75×145 mm"), ("مقاس قياسي لتاقات اللوتو", "Standard LOTO tag size")],
            [("الثقب", "Hole"), ("ثقب علوي 9–10 مم بحلقة معدنية", "9–10 mm top hole with metal grommet"), ("يتسع لذراع القفل أو الرباط", "Fits a padlock shackle or tie")],
            [("الوجه الأمامي", "Front"), ("العنوان والتحذير باللغتين", "Heading and warning in both languages"), ("ألوان السلامة القياسية", "Standard safety colours")],
            [("الوجه الخلفي", "Back"), ("حقول: الاسم، التاريخ، القسم، الهاتف", "Fields: name, date, department, phone"), ("قابلة للكتابة والمسح", "Writable and wipeable")],
            [("التثبيت", "Fixing"), ("رباط نايلون قوي أو سلك ستانلس", "Heavy nylon tie or stainless wire"), ("نوفّره مع الطلب", "Supplied with the order")],
        ],
    },
    "gallery": {
        "eyebrow": ("نماذج", "Samples"),
        "h2": ("تاقات لوتو ولوحات سلامة", "LOTO tags and safety signs"),
        "items": [
            ("assets/img/svc/tags-loto-padlocks.jpg", ("تاقات لوتو بالأحمر والأصفر والأزرق مع أقفال الأمان", "Red, yellow and blue LOTO tags with safety padlocks"), ("مع الأقفال", "With padlocks"), 1200, 900),
            ("assets/img/svc/tags-loto-set.jpg", ("مجموعة تاقات لوتو: خطر، صيانة، معزول", "A set of LOTO tags: danger, maintenance, isolated"), ("مجموعة كاملة", "Full set"), 1200, 900),
            ("assets/img/svc/tags-loto-form.jpg", ("تاق لوتو محفور فيه خانات اسم الموظف والقسم والتاريخ", "LOTO tag engraved with fields for employee name, department and date"), ("خانات البيانات", "Data fields"), 1200, 900),
        ],
        "note": GALLERY_NOTE,
    },
    "process": process(("من برنامج السلامة إلى التاقات", "From the safety programme to the tags")),
    "related": {
        "eyebrow": ("للسلامة", "For safety"),
        "h2": ("منتجات سلامة مكمّلة", "Complementary safety products"),
        "items": [
            {"icon": "shield", "href": "safety-signs.html", "h3": ("لوحات السلامة", "Safety signs"), "p": ("لوحات تحذير وإلزام ومنع ومخارج طوارئ.", "Warning, mandatory, prohibition and exit signs.")},
            {"icon": "sliders", "href": "valve-tags.html", "h3": ("تاقات المحابس", "Valve tags"), "p": ("ترقيم المحابس لعزلها بسرعة وأمان.", "Numbering valves for fast, safe isolation.")},
            {"icon": "engrave", "href": "pvc-abs-engraving.html", "h3": ("الحفر على ABS وPVC", "ABS and PVC engraving"), "p": ("المادة الأشهر للتاقات واللوحات الاقتصادية.", "The most common material for economical tags and signs.")},
        ],
    },
    "faq": [
        {
            "q": ("هل التاقات قابلة لإعادة الاستخدام؟", "Are the tags reusable?"),
            "a": (
                "نعم. العناوين والتحذيرات محفورة بشكل دائم، والحقول (الاسم والتاريخ) تُكتب بقلم دائم وتُمسح بالكحول بعد انتهاء العمل، فيُستخدم التاق مرات كثيرة.",
                "Yes. Headings and warnings are permanently engraved, while fields (name and date) are written with a marker and wiped with alcohol after the job, so the tag can be used many times.",
            ),
        },
        {
            "q": ("هل يمكن تخصيص النص حسب إجراءات شركتنا؟", "Can the text follow our company procedures?"),
            "a": (
                "نعم. أرسل نص الإجراء المعتمد لديكم أو نموذج التاق الحالي، ونطابقه حرفياً بالعربي والإنجليزي مع شعاركم وأرقام الطوارئ الداخلية.",
                "Yes. Send your approved procedure text or current tag sample and we match it word for word in Arabic and English with your logo and internal emergency numbers.",
            ),
        },
        {
            "q": ("هل توفرون أقفال اللوتو نفسها؟", "Do you supply the LOTO padlocks?"),
            "a": (
                "تخصصنا هو التاقات واللوحات المحفورة. يمكننا حفر اسم الفني ورقمه على أقفال تحضرونها، أو على تاق معدني صغير يُعلَّق مع القفل.",
                "Our speciality is engraved tags and plates. We can engrave the technician's name and number on padlocks you provide, or on a small metal tag hung with the lock.",
            ),
        },
        {
            "q": ("هل تفي التاقات بمتطلبات المراجعة والتدقيق؟", "Do the tags satisfy audit requirements?"),
            "a": (
                "نصمم التاق وفق متطلبات برنامج السلامة لديكم (الألوان، العبارات، الحقول المطلوبة) ونرسل عيّنة للاعتماد من مسؤول السلامة قبل التصنيع الكامل.",
                "We design the tag to your safety programme's requirements (colours, wording, required fields) and send a sample for approval by your safety officer before full production.",
            ),
        },
    ],
    "form_services": [
        ("تاقات خطر لا تشغّل", "Danger do-not-operate tags"),
        ("تاقات معدة مقفلة", "Locked-out tags"),
        ("تاقات شخصية مرقّمة", "Numbered personal tags"),
        ("مجموعة كاملة لبرنامج لوتو", "Full LOTO programme set"),
        ("أخرى / غير متأكد", "Other / not sure"),
    ],
    "form_wa": WA,
    "quote_h2": ("أرسل نموذج التاق أو نص الإجراء", "Send your tag sample or procedure text"),
    "quote_lead": (
        "اذكر الأنواع والكمية وعدد الفنيين إن كانت التاقات شخصية.",
        "Tell us the types, quantity and number of technicians if tags are personal.",
    ),
    "cta": {
        "h2": ("سلامة فريقك تبدأ بتاق واضح", "Your team's safety starts with a clear tag"),
        "p": ("أرسل التفاصيل، وتصلك معاينة وعرض سعر في نفس يوم العمل غالباً.", "Send the details and usually get a proof and quote the same working day."),
        "wa": WA,
    },
}
