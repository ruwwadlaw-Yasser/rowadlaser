# -*- coding: utf-8 -*-
"""تاقات الأصول والمعدات وميداليات الشركات (asset tags, equipment tags, keychains) — تحت اللوحات والتاقات"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _eng import GALLERY_NOTE, TAGS_PARENT, g, hero_img, process  # noqa: E402

WA = "مرحباً رواد الليزر، أرغب في عرض سعر لتاقات أو ميداليات معدنية محفورة."

PAGE = {
    "slug": "engraved-tags",
    "parent": TAGS_PARENT,
    "crumb": ("تاقات الأصول والميداليات المعدنية", "Asset tags and metal keychains"),
    "title": (
        "تاقات أصول ومعدات وميداليات شركات محفورة في جدة | Asset Tags بالكميات — رواد الليزر",
        "Engraved Asset Tags, Equipment Tags &amp; Branded Keychains in Jeddah | In Quantity — Ruwwad Laser",
    ),
    "desc": (
        "تاقات معدنية محفورة بالليزر للشركات في جدة: تاقات أصول ومعدات بباركود وQR، تاقات ترقيم العدد والأدوات، وميداليات مفاتيح دعائية بشعار الشركة — ستانلس وبراص وألمنيوم، بالكميات ومرقّمة من ملف إكسل.",
        "Laser engraved metal tags for companies in Jeddah: asset and equipment tags with barcodes and QR, tool numbering tags, and promotional keychains with your logo — stainless, brass and aluminium, in quantity and numbered from Excel.",
    ),
    "og_image": "assets/img/svc/tags-asset-tags.jpg",
    "service_type": ("تاقات أصول ومعدات وميداليات شركات محفورة", "Engraved asset tags, equipment tags and branded keychains"),
    "schema_name": ("تاقات الأصول والميداليات المعدنية المحفورة في جدة", "Engraved asset tags and metal keychains in Jeddah"),
    "schema_desc": (
        "حفر التاقات المعدنية بالليزر للشركات في جدة: تاقات الأصول والمعدات بالباركود وQR، تاقات ترقيم العدد والأدوات، وميداليات المفاتيح الدعائية بشعار الشركة — على الستانلس والبراص والألمنيوم، بالكميات.",
        "Laser engraving of metal tags for companies in Jeddah: asset and equipment tags with barcodes and QR, tool numbering tags, and promotional keychains with the company logo — on stainless, brass and aluminium, in quantity.",
    ),
    "schema_offers": [
        ("تاقات أصول ومعدات", "Asset and equipment tags"),
        ("تاقات ترقيم العدد والأدوات", "Tool numbering tags"),
        ("ميداليات مفاتيح بالشعار", "Branded keychains"),
        ("تاقات معدنية مرقّمة بالكميات", "Numbered metal tags in quantity"),
    ],
    "hero": {
        "eyebrow": ("أصول · معدات · ميداليات", "Assets · equipment · keychains"),
        "h1": ("تاقات أصول وميداليات شركات محفورة", "Engraved asset tags and company keychains"),
        "sub": (
            "تاق أصول لكل جهاز في شركتك، رقم لكل أداة في ورشتك، أو ميدالية بشعارك لعملائك وموظفيك. نحفرها بالليزر على ستانلس وبراص وألمنيوم بالكميات — كل تاق برقمه أو باركوده من ملف إكسل.",
            "An asset tag for every device in your company, a number for every tool in your workshop, or a keychain with your logo for clients and staff. We laser engrave them on stainless, brass and aluminium in quantity — each tag with its own number or barcode from Excel.",
        ),
        "chips": [
            ("بالكميات للشركات", "In quantity for companies", "check"),
            ("ترقيم من ملف إكسل", "Numbering from Excel", "file"),
            ("ستانلس · براص · ألمنيوم", "Stainless · brass · aluminium", "layers"),
            ("باركود وQR", "Barcodes and QR", "target"),
        ],
        "img": ("assets/img/svc/tags-asset-tags.jpg", ("تاقات أصول مرقّمة مثبّتة على العدد والمعدات", "Numbered asset tags fixed on tools and equipment"), 1200, 900),
        "wa": WA,
    },
    "facts": [
        (("100%", "100%"), ("فحص كل رقم وحرف قبل التسليم", "Every number and letter checked")),
        (("QR", "QR"), ("وباركود لجرد الأصول", "And barcodes for asset tracking")),
        (("2", "2"), ("الحفر على الوجهين", "Engraving on both sides")),
        (("6", "6"), ("ساعات لبدء التنفيذ", "Hours to start production")),
    ],
    "intro": {
        "h2": ("رقم لكل أصل، شعار لا يُمحى", "A number for every asset, a logo that lasts"),
        "paras": [
            (
                "التاق المعدني المحفور يحمل معلومة مهمة في مساحة صغيرة: رقم أصل، باركود جرد، رقم أداة، أو شعار علامتك التجارية. وبما أن الحفر بالليزر جزء من المعدن نفسه، فالمعلومة لا تُمحى بالاحتكاك أو الحرارة أو التنظيف.",
                "An engraved metal tag carries important information in a small space: an asset number, an inventory barcode, a tool number or your brand logo. Since laser engraving is part of the metal itself, it doesn't rub off from friction, heat or cleaning.",
            ),
            (
                "ولأن الحفر يتم من ملف رقمي، يحمل كل تاق في الدفعة نصاً مختلفاً — رقم كل جهاز، اسم كل قسم، أو باركود متسلسل — مرتّباً حسب قائمة الجرد عندك.",
                "And because engraving runs from a digital file, every tag in the batch carries different text — each device's number, each department's name or a sequential barcode — sorted to your inventory list.",
            ),
        ],
        "h3": ("أشهر طلبات الشركات", "Most popular company orders"),
        "bullets": [
            ("تاقات الأصول: رقم الأصل وباركود أو QR لجرد الأجهزة والأثاث والمعدات.", "Asset tags: asset number and barcode or QR for inventorying devices, furniture and equipment."),
            ("تاقات المعدات والمكائن: رقم المعدة وبيانات الصيانة على ستانلس يتحمّل بيئة العمل.", "Equipment and machine tags: equipment number and maintenance data on stainless that survives the workplace."),
            ("ترقيم العدد والأدوات: رقم لكل أداة لمعرفة صاحبها ومكانها في الورشة.", "Tool numbering: a number for every tool to track its owner and place in the workshop."),
            ("ميداليات مفاتيح دعائية بشعار الشركة للعملاء والموظفين والمعارض.", "Promotional keychains with the company logo for clients, staff and exhibitions."),
        ],
    },
    "cards": {
        "eyebrow": ("الأنواع", "Types"),
        "h2": ("اختر نوع التاق", "Choose your tag type"),
        "items": [
            {"icon": "file", "h3": ("تاقات الأصول", "Asset tags"), "p": ("رقم أصل وباركود أو QR، بلاصق صناعي أو برشام.", "Asset number with barcode or QR, with industrial adhesive or rivets."), "href": "qr-barcode-marking.html", "more": ("حفر الباركود وQR", "Barcode and QR marking")},
            {"icon": "factory", "h3": ("تاقات المعدات", "Equipment tags"), "p": ("رقم المعدة وبيانات الصيانة على ستانلس متين.", "Equipment number and maintenance data on durable stainless."), "href": "metal-nameplates-serial-numbers.html", "more": ("لوحات البيانات", "Data plates")},
            {"icon": "build", "h3": ("تاقات الأدوات", "Tool tags"), "p": ("ترقيم عدد الورش لمعرفة صاحب كل أداة ومكانها.", "Numbering workshop tools to track each tool's owner and place.")},
            {"icon": "store", "h3": ("ميداليات بالشعار", "Logo keychains"), "p": ("بشعار الشركة أو اسم المناسبة، للعملاء والمعارض.", "With a company logo or event name, for clients and exhibitions."), "href": "logo-engraving-products.html", "more": ("حفر الشعارات", "Logo engraving")},
        ],
    },
    "specs": {
        "soft": True,
        "eyebrow": ("مواصفات", "Specs"),
        "h2": ("المقاسات والمواد المعتادة", "Usual sizes and materials"),
        "cols": [("النوع", "Type"), ("المقاس الشائع", "Common size"), ("المادة", "Material")],
        "rows": [
            [("تاق أصول", "Asset tag"), ("50×20 إلى 75×38 مم", "50×20 to 75×38 mm"), ("ألمنيوم مؤكسد أو ستانلس", "Anodised aluminium or stainless")],
            [("تاق معدة", "Equipment tag"), ("75×38 إلى 100×50 مم", "75×38 to 100×50 mm"), ("ستانلس 304/316", "Stainless 304/316")],
            [("تاق أداة", "Tool tag"), ("30×12 إلى 50×20 مم", "30×12 to 50×20 mm"), ("ستانلس أو ألمنيوم", "Stainless or aluminium")],
            [("ميدالية مفاتيح", "Keychain"), ("قطر 35–45 مم أو بشكل الشعار", "35–45 mm or logo-shaped"), ("ستانلس أو ألمنيوم ملوّن", "Stainless or coloured aluminium")],
        ],
        "note": (
            "يمكن قصّ الميدالية بشكل شعارك نفسه بالليزر بدلاً من الأشكال القياسية.",
            "A keychain can be laser cut in the shape of your logo instead of a standard shape.",
        ),
    },
    "gallery": {
        "eyebrow": ("نماذج", "Samples"),
        "h2": ("تاقات أصول وميداليات محفورة", "Engraved asset tags and keychains"),
        "items": [
            ("assets/img/svc/tags-dog-pet-tags.jpg", ("تاق أصول وميدالية مفاتيح بشعار شركة وتاقات معدنية محفورة", "Asset tag, logo keychain and engraved metal tags"), ("ميداليات وتاقات", "Keychains and tags"), 1200, 900),
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
                "نعم. ميداليات بشعار الشركة وتاقات أصول مرقّمة بالمئات والآلاف، مرتّبة حسب قائمتك، مع ترقيم أو باركود مختلف لكل قطعة.",
                "Yes. Branded keychains and numbered asset tags in hundreds and thousands, sorted to your list with a different number or barcode on every piece.",
            ),
        },
        {
            "q": ("هل يمكن الحفر على الوجهين؟", "Can both sides be engraved?"),
            "a": (
                "نعم. مثلاً: شعار الشركة على الوجه الأول، ورقم الأصل أو الباركود على الوجه الثاني.",
                "Yes. For example, the company logo on one side and the asset number or barcode on the other.",
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
                "نعم: سلاسل كرات، حلقات مفاتيح، أربطة وبراشيم للتثبيت على المعدات — تُرفق مع الطلب.",
                "Yes: ball chains, key rings, ties and rivets for fixing to equipment — supplied with the order.",
            ),
        },
    ],
    "form_services": [
        ("تاقات أصول ومعدات", "Asset and equipment tags"),
        ("ترقيم العدد والأدوات", "Tool numbering tags"),
        ("ميداليات مفاتيح بالشعار", "Branded keychains"),
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
