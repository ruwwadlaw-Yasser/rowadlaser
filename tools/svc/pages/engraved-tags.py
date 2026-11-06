# -*- coding: utf-8 -*-
"""التاقات والميداليات المعدنية (Dog tags, pet tags, keychains, asset tags) — تحت اللوحات والتاقات"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _eng import GALLERY_NOTE, TAGS_PARENT, g, hero_img, process  # noqa: E402

WA = "مرحباً رواد الليزر، أرغب في عرض سعر لتاقات أو ميداليات معدنية محفورة."

PAGE = {
    "slug": "engraved-tags",
    "parent": TAGS_PARENT,
    "crumb": ("التاقات والميداليات المعدنية", "Metal tags and keychains"),
    "title": (
        "تاقات معدنية وميداليات محفورة في جدة | دوق تاق، تاقات حيوانات، تاقات أصول — رواد الليزر",
        "Engraved Metal Tags &amp; Keychains in Jeddah | Dog Tags, Pet Tags, Asset Tags — Ruwwad Laser",
    ),
    "desc": (
        "تاقات معدنية محفورة بالليزر في جدة: دوق تاق (Dog Tag) بالاسم وفصيلة الدم، تاقات حيوانات أليفة، ميداليات مفاتيح بشعار الشركة، وتاقات أصول ومعدات بباركود. ستانلس وبراص وألمنيوم — للهدايا الشخصية وطلبات الشركات.",
        "Laser engraved metal tags in Jeddah: dog tags with name and blood type, pet ID tags, branded keychains, and asset/equipment tags with barcodes. Stainless, brass and aluminium — for personal gifts and company orders.",
    ),
    "og_image": "assets/img/svc/tags-dog-pet-tags.jpg",
    "service_type": ("تاقات وميداليات معدنية محفورة", "Engraved metal tags and keychains"),
    "schema_name": ("التاقات والميداليات المعدنية المحفورة في جدة", "Engraved metal tags and keychains in Jeddah"),
    "schema_desc": (
        "حفر التاقات المعدنية بالليزر في جدة: تاقات تعريف شخصية (Dog Tags)، تاقات الحيوانات الأليفة، ميداليات المفاتيح الدعائية، تاقات الأصول والمعدات بالباركود وQR، وتاقات الحقائب — على الستانلس والبراص والألمنيوم.",
        "Laser engraving of metal tags in Jeddah: personal ID dog tags, pet tags, promotional keychains, asset and equipment tags with barcodes and QR, and luggage tags — on stainless, brass and aluminium.",
    ),
    "schema_offers": [
        ("دوق تاق محفور", "Engraved dog tags"),
        ("تاقات الحيوانات الأليفة", "Pet ID tags"),
        ("ميداليات مفاتيح بالشعار", "Branded keychains"),
        ("تاقات أصول ومعدات", "Asset and equipment tags"),
    ],
    "hero": {
        "eyebrow": ("تاقات · ميداليات · أصول", "Tags · keychains · assets"),
        "h1": ("تاقات معدنية وميداليات محفورة", "Engraved metal tags and keychains"),
        "sub": (
            "تاق بالاسم وفصيلة الدم، تاق لقطّتك برقم جوالك، ميدالية بشعار شركتك لعملائك، أو تاق أصول لكل جهاز في مكتبك. نحفرها بالليزر على ستانلس وبراص وألمنيوم — لهدية شخصية أو لطلبات شركتك بالكميات.",
            "A tag with your name and blood type, a tag for your cat with your number, a keychain with your logo for clients, or an asset tag for every device in your office. We laser engrave them on stainless, brass and aluminium — as a personal gift or in quantity for your company.",
        ),
        "chips": [
            ("هدايا وطلبات شركات", "Gifts and company orders", "check"),
            ("أسماء وأرقام مختلفة", "Different names and numbers", "file"),
            ("ستانلس · براص · ألمنيوم", "Stainless · brass · aluminium", "layers"),
            ("باركود وQR", "Barcodes and QR", "target"),
        ],
        "img": ("assets/img/svc/tags-dog-pet-tags.jpg", ("دوق تاق وتاق حيوان أليف على شكل عظمة وتاق أصول وميدالية مفاتيح", "Dog tag, bone-shaped pet tag, asset tag and keyring"), 1200, 900),
        "wa": WA,
    },
    "facts": [
        (("100%", "100%"), ("فحص كل رقم وحرف قبل التسليم", "Every number and letter checked")),
        (("4", "4"), ("أنواع رئيسية من التاقات", "Main tag types")),
        (("2", "2"), ("الحفر على الوجهين", "Engraving on both sides")),
        (("6", "6"), ("ساعات لبدء التنفيذ", "Hours to start production")),
    ],
    "intro": {
        "h2": ("تاق صغير، معلومة لا تضيع", "A small tag, information that never gets lost"),
        "paras": [
            (
                "التاق المعدني المحفور يحمل معلومة مهمة في مساحة صغيرة: اسم شخص، رقم تواصل، رقم أصل، أو شعار علامة تجارية. وبما أن الحفر بالليزر جزء من المعدن نفسه، فالمعلومة لا تُمحى بالاحتكاك اليومي في الجيب أو على الطوق أو في الحقيبة.",
                "An engraved metal tag carries important information in a small space: a person's name, a contact number, an asset number or a brand logo. Since laser engraving is part of the metal itself, the information doesn't rub off from daily wear in a pocket, on a collar or in a bag.",
            ),
            (
                "ولأن الحفر يتم من ملف رقمي، يمكن أن يحمل كل تاق نصاً مختلفاً — اسم كل موظف، رقم كل جهاز، أو باركود متسلسل — دون تكلفة إضافية تُذكر.",
                "And because engraving runs from a digital file, every tag can carry different text — each employee's name, each device's number or a sequential barcode — at hardly any extra cost.",
            ),
        ],
        "h3": ("أشهر الطلبات", "Most popular requests"),
        "bullets": [
            ("دوق تاق (Dog Tag): الاسم، فصيلة الدم، رقم الطوارئ — للعسكريين والرياضيين والهدايا.", "Dog tags: name, blood type, emergency number — for servicemen, athletes and gifts."),
            ("تاقات الحيوانات الأليفة: اسم القط أو الكلب ورقم جوال المالك.", "Pet tags: the cat's or dog's name and the owner's mobile number."),
            ("ميداليات مفاتيح دعائية بشعار الشركة للعملاء والموظفين والمعارض.", "Promotional keychains with the company logo for clients, staff and exhibitions."),
            ("تاقات الأصول: رقم الأصل وباركود أو QR لجرد الأجهزة والمعدات والأدوات.", "Asset tags: asset number and barcode or QR for inventorying devices, equipment and tools."),
        ],
    },
    "cards": {
        "eyebrow": ("الأنواع", "Types"),
        "h2": ("اختر نوع التاق", "Choose your tag type"),
        "items": [
            {"icon": "user", "h3": ("دوق تاق", "Dog tags"), "p": ("ستانلس بحواف مدوّرة وسلسلة كرات، حفر على الوجهين.", "Rounded-edge stainless with a ball chain, engraved on both sides.")},
            {"icon": "target", "h3": ("تاقات الحيوانات", "Pet tags"), "p": ("دائري، قلب، عظمة — براص أو ستانلس بحلقة للطوق.", "Round, heart or bone — brass or stainless with a collar ring.")},
            {"icon": "store", "h3": ("ميداليات مفاتيح", "Keychains"), "p": ("بشعار الشركة أو اسم المناسبة، للهدايا والمعارض.", "With a company logo or event name, for gifts and exhibitions."), "href": "logo-engraving-products.html", "more": ("حفر الشعارات على المنتجات", "Logo engraving on products")},
            {"icon": "file", "h3": ("تاقات الأصول", "Asset tags"), "p": ("رقم أصل وباركود أو QR، بلاصق صناعي أو برشام.", "Asset number with barcode or QR, with industrial adhesive or rivets."), "href": "qr-barcode-marking.html", "more": ("حفر الباركود وQR", "Barcode and QR marking")},
            {"icon": "build", "h3": ("تاقات الأدوات", "Tool tags"), "p": ("ترقيم عدد الورش لمعرفة صاحب كل أداة ومكانها.", "Numbering workshop tools to track each tool's owner and place.")},
            {"icon": "layers", "h3": ("تاقات الحقائب", "Luggage tags"), "p": ("الاسم ورقم التواصل على تاق معدني متين.", "Name and contact number on a durable metal tag.")},
        ],
    },
    "specs": {
        "soft": True,
        "eyebrow": ("مواصفات", "Specs"),
        "h2": ("المقاسات والمواد المعتادة", "Usual sizes and materials"),
        "cols": [("النوع", "Type"), ("المقاس الشائع", "Common size"), ("المادة", "Material")],
        "rows": [
            [("دوق تاق", "Dog tag"), ("50×28 مم", "50×28 mm"), ("ستانلس", "Stainless")],
            [("تاق حيوان", "Pet tag"), ("قطر 25–32 مم", "25–32 mm diameter"), ("براص أو ستانلس", "Brass or stainless")],
            [("ميدالية مفاتيح", "Keychain"), ("قطر 35–45 مم أو بشكل الشعار", "35–45 mm or logo-shaped"), ("ستانلس أو ألمنيوم ملوّن", "Stainless or coloured aluminium")],
            [("تاق أصول", "Asset tag"), ("50×20 إلى 75×38 مم", "50×20 to 75×38 mm"), ("ألمنيوم مؤكسد أو ستانلس", "Anodised aluminium or stainless")],
        ],
        "note": (
            "يمكن قصّ الميدالية بشكل شعارك نفسه بالليزر بدلاً من الأشكال القياسية.",
            "A keychain can be laser cut in the shape of your logo instead of a standard shape.",
        ),
    },
    "gallery": {
        "eyebrow": ("نماذج", "Samples"),
        "h2": ("تاقات وميداليات محفورة", "Engraved tags and keychains"),
        "items": [
            ("assets/img/svc/tags-asset-tags.jpg", ("تاقات أصول مرقّمة مثبّتة على العدد والمعدات", "Numbered asset tags fixed on tools and equipment"), ("تاقات الأصول", "Asset tags"), 1200, 900),
            ("assets/img/svc/tags-mixed-materials.jpg", ("تاقات محفورة من الستانلس والبراص والألمنيوم الملوّن", "Engraved tags in stainless, brass and coloured aluminium"), ("مواد مختلفة", "Different materials"), 1200, 900),
            g("engraved-hand-tool", ("عدّة يدوية محفور عليها رقم بالليزر", "A hand tool laser engraved with a number"), ("حفر على العدد", "Engraving on tools")),
        ],
        "note": GALLERY_NOTE,
    },
    "process": process(),
    "related": {
        "eyebrow": ("مرتبط", "Related"),
        "h2": ("خدمات مرتبطة", "Related services"),
        "items": [
            {"icon": "user", "href": "name-badges.html", "h3": ("بادجات الأسماء", "Name badges"), "p": ("بادجات موظفين معدنية بشعار الشركة.", "Metal staff badges with your logo.")},
            {"icon": "target", "href": "qr-barcode-marking.html", "h3": ("حفر QR والباركود", "QR and barcode marking"), "p": ("أكواد قابلة للمسح على المعدن لجرد الأصول.", "Scannable codes on metal for asset tracking.")},
            {"icon": "engrave", "href": "logo-engraving-products.html", "h3": ("حفر الشعارات", "Logo engraving"), "p": ("على الترامس والأقلام والهدايا الدعائية.", "On flasks, pens and promotional gifts.")},
        ],
    },
    "faq": [
        {
            "q": ("هل تنفّذون طلبات الشركات بالكميات؟", "Do you handle company orders in quantity?"),
            "a": (
                "نعم. ميداليات بشعار الشركة وتاقات أصول مرقّمة بالمئات والآلاف، مرتّبة حسب قائمتك — ونحفر أيضاً هدايا شخصية مثل دوق تاق أو تاق لقطتك.",
                "Yes. Branded keychains and numbered asset tags in hundreds and thousands, sorted to your list — and we also engrave personal gifts like a dog tag or a tag for your cat.",
            ),
        },
        {
            "q": ("هل يمكن الحفر على الوجهين؟", "Can both sides be engraved?"),
            "a": (
                "نعم. مثلاً: الاسم على الوجه الأول، ورقم الجوال أو فصيلة الدم على الوجه الثاني.",
                "Yes. For example, the name on one side and the mobile number or blood type on the other.",
            ),
        },
        {
            "q": ("هل يقرأ الماسح باركود تاقات الأصول؟", "Will scanners read asset-tag barcodes?"),
            "a": (
                "نعم، نحفر الباركود وأكواد QR بتباين عالٍ يُقرأ بالماسحات وتطبيقات الجوال، ونختبر عيّنة قبل الكمية الكاملة.",
                "Yes, we engrave barcodes and QR codes in high contrast readable by scanners and phone apps, and test a sample before the full batch.",
            ),
        },
        {
            "q": ("هل تتوفر السلاسل والحلقات؟", "Are chains and rings available?"),
            "a": (
                "نعم: سلاسل كرات للدوق تاق، حلقات مفاتيح، وحلقات صغيرة لأطواق الحيوانات — تُرفق مع الطلب.",
                "Yes: ball chains for dog tags, key rings and small split rings for pet collars — supplied with the order.",
            ),
        },
    ],
    "form_services": [
        ("دوق تاق", "Dog tags"),
        ("تاقات حيوانات أليفة", "Pet tags"),
        ("ميداليات مفاتيح بالشعار", "Branded keychains"),
        ("تاقات أصول ومعدات", "Asset and equipment tags"),
        ("أخرى / غير متأكد", "Other / not sure"),
    ],
    "form_wa": WA,
    "quote_h2": ("أرسل النص أو الشعار", "Send your text or logo"),
    "quote_lead": (
        "اذكر نوع التاق والكمية والمادة المفضلة، والنص المطلوب على كل وجه.",
        "Tell us the tag type, quantity, preferred material and the text for each side.",
    ),
    "cta": {
        "h2": ("تاق صغير يدوم طويلاً", "A small tag that lasts"),
        "p": ("أرسل التفاصيل، وتصلك معاينة وعرض سعر في نفس يوم العمل غالباً.", "Send the details and usually get a proof and quote the same working day."),
        "wa": WA,
    },
}
