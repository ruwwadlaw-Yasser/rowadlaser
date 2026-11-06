# -*- coding: utf-8 -*-
"""بادجات الأسماء (Name Badges) — تحت اللوحات والتاقات التعريفية"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _eng import GALLERY_NOTE, TAGS_PARENT, g, hero_img, process  # noqa: E402

WA = "مرحباً رواد الليزر، أرغب في عرض سعر لبادجات أسماء محفورة."

PAGE = {
    "slug": "name-badges",
    "parent": TAGS_PARENT,
    "crumb": ("بادجات الأسماء", "Name badges"),
    "title": (
        "بادجات أسماء في جدة | بادج اسم معدني ومغناطيسي للموظفين — رواد الليزر",
        "Name Badges in Jeddah | Engraved Metal &amp; Magnetic Staff Badges — Ruwwad Laser",
    ),
    "desc": (
        "بادجات أسماء للموظفين في جدة: بادج اسم ستانلس، ذهبي، أسود، أو بألوان هويتك — محفور بالليزر بالاسم والمسمى والشعار، بمغناطيس أو دبوس. للمطاعم والفنادق والمستشفيات والشركات. بدء التنفيذ خلال 6 ساعات.",
        "Staff name badges in Jeddah: stainless, gold, black or brand-coloured badges laser engraved with name, title and logo, with magnet or pin. For restaurants, hotels, hospitals and companies. Production starts within 6 hours.",
    ),
    "og_image": "assets/img/svc/ill-name-badges.jpg",
    "service_type": ("بادجات أسماء محفورة", "Engraved name badges"),
    "schema_name": ("بادجات الأسماء المحفورة في جدة", "Engraved name badges in Jeddah"),
    "schema_desc": (
        "تصنيع بادجات أسماء الموظفين بالحفر بالليزر في جدة: بادجات معدنية من الستانلس والبراص والألمنيوم الملون، وبادجات أكريليك، بالاسم والمسمى الوظيفي وشعار الشركة، مع تثبيت مغناطيسي أو بدبوس، للمطاعم والفنادق والمستشفيات والشركات.",
        "Manufacture of laser engraved staff name badges in Jeddah: metal badges in stainless, brass and coloured aluminium, plus acrylic badges, with name, job title and company logo, magnet or pin fixing, for restaurants, hotels, hospitals and companies.",
    ),
    "schema_offers": [
        ("بادج اسم ستانلس", "Stainless name badge"),
        ("بادج اسم ذهبي", "Gold name badge"),
        ("بادج اسم مغناطيسي", "Magnetic name badge"),
        ("بادجات بشعار الشركة", "Branded name badges"),
    ],
    "hero": {
        "eyebrow": ("بادجات · موظفين", "Badges · staff"),
        "h1": ("بادجات أسماء محفورة بشعار شركتك", "Name badges engraved with your logo"),
        "sub": (
            "بادج الاسم أول ما يراه العميل عند التعامل مع موظفك. نصنعه معدنياً أنيقاً — ستانلس، ذهبي، أسود، أو بألوان هويتك — محفوراً بالاسم والمسمى والشعار، بمغناطيس لا يثقب الملابس أو بدبوس تقليدي.",
            "The name badge is the first thing a customer sees when dealing with your staff. We make it as an elegant metal badge — stainless, gold, black or your brand colours — engraved with name, title and logo, with a magnet that doesn't pierce clothing or a classic pin.",
        ),
        "chips": [
            ("مغناطيس أو دبوس", "Magnet or pin", "check"),
            ("ألوان الهوية", "Brand colours", "target"),
            ("أسماء من ملف إكسل", "Names from Excel", "file"),
            ("تصميم محفوظ للموظفين الجدد", "Design kept for new staff", "user"),
        ],
        "img": hero_img(
            "name-badges",
            ("بادجات أسماء بألوان فضي وذهبي وأسود وأزرق وأبيض مع شعار", "Name badges in silver, gold, black, blue and white with a logo"),
        ),
        "wa": WA,
    },
    "facts": [
        (("70×25 mm", "70×25 mm"), ("المقاس الأشهر للبادج", "The most popular badge size")),
        (("+6", "+6"), ("ألوان وتشطيبات", "Colours and finishes")),
        (("6", "6"), ("ساعات لبدء التنفيذ", "Hours to start production")),
        (("100%", "100%"), ("مراجعة الأسماء قبل الحفر", "Names checked before engraving")),
    ],
    "intro": {
        "h2": ("لماذا البادج المحفور أفضل من المطبوع؟", "Why an engraved badge beats a printed one"),
        "paras": [
            (
                "البادج المطبوع يبهت ويُخدش مع الاستخدام اليومي واللمس والغسيل، خصوصاً في المطاعم والمستشفيات. البادج المحفور بالليزر يحتفظ بالاسم والشعار واضحين طوال فترة عمل الموظف، ويعطي انطباعاً أرقى بكثير.",
                "Printed badges fade and scratch with daily wear, touching and washing, especially in restaurants and hospitals. A laser engraved badge keeps the name and logo crisp for the employee's whole tenure and looks far more premium.",
            ),
            (
                "ولأن الحفر يُنفّذ رقمياً من ملف، يمكن أن يحمل كل بادج اسماً مختلفاً بنفس التكلفة تقريباً — أرسل قائمة الموظفين في إكسل، ونحفر كل اسم ومسمّاه بالعربي أو الإنجليزي أو كليهما.",
                "And because engraving runs digitally from a file, every badge can carry a different name at nearly the same cost — send the staff list in Excel and we engrave each name and title in Arabic, English or both.",
            ),
        ],
        "h3": ("من يطلب بادجات الأسماء؟", "Who orders name badges?"),
        "bullets": [
            ("المطاعم والمقاهي: بادج مغناطيسي لا يتلف الزي ويتحمل البخار والغسيل.", "Restaurants and cafés: a magnetic badge that spares uniforms and handles steam and washing."),
            ("الفنادق والمعارض: بادج ذهبي أو أسود فاخر بالاسم واللغات التي يتحدثها الموظف.", "Hotels and showrooms: premium gold or black badges with the name and languages spoken."),
            ("المستشفيات والعيادات: الاسم والتخصص بوضوح عالٍ وسهولة التعقيم.", "Hospitals and clinics: name and speciality in high clarity, easy to disinfect."),
            ("الشركات والبنوك ومراكز خدمة العملاء: بادجات موحّدة بهوية الشركة.", "Companies, banks and service centres: unified badges in the company identity."),
        ],
    },
    "cards": {
        "eyebrow": ("الخيارات", "Options"),
        "h2": ("اختر شكل البادج", "Choose your badge style"),
        "items": [
            {"icon": "shield", "h3": ("ستانلس فضي", "Silver stainless"), "p": ("نقش أسود عالي التباين على ستانلس مصقول — كلاسيكي وعملي.", "High-contrast black marking on brushed stainless — classic and practical."), "href": "engraving-stainless-steel.html", "more": ("الحفر على الستانلس", "Stainless engraving")},
            {"icon": "target", "h3": ("ذهبي", "Gold"), "p": ("براص أو ألمنيوم ذهبي بحفر داكن — للفنادق والمعارض الفاخرة.", "Brass or gold aluminium with dark engraving — for hotels and premium showrooms."), "href": "brass-engraving.html", "more": ("الحفر على البراص", "Brass engraving")},
            {"icon": "layers", "h3": ("ألوان الهوية", "Brand colours"), "p": ("ألمنيوم مؤكسد بالأسود أو الأزرق أو الأحمر، والحفر يظهر فضياً.", "Anodised aluminium in black, blue or red, with silver engraving."), "href": "aluminum-engraving.html", "more": ("الحفر على الألمنيوم", "Aluminium engraving")},
            {"icon": "cube", "h3": ("أكريليك وABS", "Acrylic and ABS"), "p": ("خيار اقتصادي وخفيف بطبقتين لونيتين.", "A light, economical two-colour option.")},
            {"icon": "check", "h3": ("مغناطيس قوي", "Strong magnet"), "p": ("لا يثقب الملابس، مناسب للأزياء الرسمية والقمصان.", "Doesn't pierce fabric, suited to uniforms and shirts.")},
            {"icon": "user", "h3": ("دبوس أو كليب", "Pin or clip"), "p": ("الخيار التقليدي الاقتصادي للكميات الكبيرة.", "The classic economical option for large quantities.")},
        ],
    },
    "specs": {
        "soft": True,
        "eyebrow": ("مواصفات", "Specs"),
        "h2": ("المقاسات والتفاصيل المعتادة", "Usual sizes and details"),
        "cols": [("البند", "Item"), ("الخيار الشائع", "Common option"), ("ملاحظة", "Note")],
        "rows": [
            [("المقاس", "Size"), ("70×25، 75×30، 80×35 مم", "70×25, 75×30, 80×35 mm"), ("نرشّح الأكبر للأسماء الطويلة", "Larger for long names")],
            [("الشكل", "Shape"), ("مستطيل بزوايا دائرية، بيضاوي، مخصص", "Rounded rectangle, oval, custom"), ("نقصّ أي شكل بالليزر", "We laser cut any shape")],
            [("المحتوى", "Content"), ("الشعار، الاسم، المسمى", "Logo, name, title"), ("يمكن إضافة اللغات أو رقم الموظف", "Languages or staff ID can be added")],
            [("التثبيت", "Fixing"), ("مغناطيس، دبوس، كليب", "Magnet, pin, clip"), ("المغناطيس الأكثر طلباً", "Magnets are most requested")],
        ],
    },
    "gallery": {
        "eyebrow": ("نماذج", "Samples"),
        "h2": ("بادجات بألوان وتشطيبات مختلفة", "Badges in different colours and finishes"),
        "items": [
            g("ill-name-badges", ("بادجات أسماء معدنية بألوان مختلفة", "Metal name badges in various colours"), ("بادجات الأسماء", "Name badges")),
            g("engraving-four-metals-test", ("اختبار حفر على أربعة معادن: ستانلس وألمنيوم وبراص ونحاس", "Engraving test on four metals: stainless, aluminium, brass and copper"), ("المعادن المتاحة", "Available metals")),
            ("assets/img/svc/tags-office-signs.jpg", ("لوحات إرشادية للمكاتب بنفس الهوية", "Office signage plates in the same identity"), ("لوحات مطابقة", "Matching plates"), 1200, 900),
        ],
        "note": GALLERY_NOTE,
    },
    "process": process(("من قائمة الموظفين إلى البادجات", "From the staff list to the badges")),
    "related": {
        "eyebrow": ("مكمّلات", "Complements"),
        "h2": ("منتجات مرتبطة", "Related products"),
        "items": [
            {"icon": "store", "href": "signage-plates.html", "h3": ("اللوحات الإرشادية", "Signage plates"), "p": ("لوحات أبواب ومكاتب بنفس هوية البادجات.", "Door and office plates matching the badges.")},
            {"icon": "engrave", "href": "engraved-tags.html", "h3": ("التاقات والميداليات", "Tags and keychains"), "p": ("ميداليات وتاقات معدنية بشعار الشركة.", "Metal keychains and tags with the company logo.")},
            {"icon": "user", "href": "logo-engraving-products.html", "h3": ("حفر الشعارات على المنتجات", "Logo engraving on products"), "p": ("هدايا الموظفين والعملاء بشعارك.", "Staff and client gifts with your logo.")},
        ],
    },
    "faq": [
        {
            "q": ("ماذا لو انضم موظف جديد بعد الطلب الأول؟", "What if someone joins after the first order?"),
            "a": (
                "نحتفظ بتصميم بادجات شركتك بعد أول طلب، فعند انضمام موظف جديد ترسل اسمه ومسمّاه فقط ونجهّز بادجاً مطابقاً تماماً للبقية.",
                "We keep your company's badge design after the first order, so when someone joins you just send their name and title and we make a badge identical to the rest.",
            ),
        },
        {
            "q": ("هل المغناطيس قوي بما يكفي؟", "Is the magnet strong enough?"),
            "a": (
                "نستخدم مغناطيساً بقطعتين يثبت على القمصان والأزياء الرسمية العادية بثبات. للأقمشة السميكة جداً نرشّح الدبوس أو الكليب.",
                "We use a two-part magnet that holds firmly on normal shirts and uniforms. For very thick fabrics we recommend a pin or clip.",
            ),
        },
        {
            "q": ("هل يمكن كتابة الاسم بالعربي والإنجليزي؟", "Can the name be in Arabic and English?"),
            "a": (
                "نعم، وهو الأشهر في جدة: الاسم بالعربي في سطر وبالإنجليزي في سطر، مع الشعار. ونرسل معاينة لكل الأسماء للتأكد من الإملاء قبل الحفر.",
                "Yes, and it's the most popular in Jeddah: the name in Arabic on one line and English on another, with the logo. We send a proof of all names to verify spelling before engraving.",
            ),
        },
        {
            "q": ("هل يتحمل البادج الغسيل والبخار في المطابخ؟", "Does the badge survive washing and kitchen steam?"),
            "a": (
                "البادج المعدني المحفور لا يحتوي طباعة تتأثر بالماء أو البخار، ويُمسح بقطعة مبللة. نرشّح الستانلس للمطابخ لأنه الأسهل تنظيفاً.",
                "An engraved metal badge has no print to be affected by water or steam and wipes clean with a damp cloth. We recommend stainless for kitchens as it is the easiest to clean.",
            ),
        },
    ],
    "form_services": [
        ("بادج ستانلس فضي", "Silver stainless badge"),
        ("بادج ذهبي", "Gold badge"),
        ("بادج بألوان الهوية", "Brand-coloured badge"),
        ("بادج أكريليك / ABS", "Acrylic / ABS badge"),
        ("أخرى / غير متأكد", "Other / not sure"),
    ],
    "form_wa": WA,
    "quote_h2": ("أرسل الشعار وقائمة الأسماء", "Send your logo and name list"),
    "quote_lead": (
        "اذكر عدد البادجات واللون المفضل وطريقة التثبيت (مغناطيس أو دبوس).",
        "Tell us the number of badges, preferred colour and fixing (magnet or pin).",
    ),
    "cta": {
        "h2": ("فريقك يستحق بادجاً أنيقاً", "Your team deserves a smart badge"),
        "p": ("أرسل الشعار والأسماء، وتصلك معاينة وعرض سعر في نفس يوم العمل غالباً.", "Send the logo and names and usually get a proof and quote the same working day."),
        "wa": WA,
    },
}
