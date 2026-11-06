# -*- coding: utf-8 -*-
"""تاقات الكيابل (Cable ID Tags) — تحت اللوحات والتاقات التعريفية"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _eng import GALLERY_NOTE, TAGS_PARENT, g, hero_img, process  # noqa: E402

WA = "مرحباً رواد الليزر، أرغب في عرض سعر لتاقات كيابل محفورة."

PAGE = {
    "slug": "cable-id-tags",
    "parent": TAGS_PARENT,
    "crumb": ("تاقات الكيابل", "Cable ID tags"),
    "title": (
        "تاقات كيابل محفورة في جدة | Cable Tags ستانلس لا تُمحى — رواد الليزر",
        "Engraved Cable ID Tags in Jeddah | Stainless Cable Markers — Ruwwad Laser",
    ),
    "desc": (
        "تاقات تعريف الكيابل محفورة بالليزر في جدة: شرائح ستانلس 316 وألمنيوم بأرقام الكيابل والدوائر، تُثبّت بأربطة ستانلس. للوحات التوزيع ومحطات الطاقة الشمسية والاتصالات. ترقيم من إكسل.",
        "Laser engraved cable ID tags in Jeddah: stainless 316 and aluminium strips with cable and circuit numbers, fixed with stainless ties. For switchgear, solar plants and telecom. Numbered from Excel.",
    ),
    "og_image": "assets/img/svc/tags-cable-bundle.jpg",
    "service_type": ("تاقات تعريف الكيابل", "Cable identification tags"),
    "schema_name": ("تاقات الكيابل المحفورة في جدة", "Engraved cable ID tags in Jeddah"),
    "schema_desc": (
        "تصنيع تاقات تعريف الكيابل بالحفر بالليزر على الستانلس ستيل والألمنيوم في جدة: أرقام الكيابل والدوائر ومصدرها ووجهتها، مع أربطة ستانلس للتثبيت، لمشاريع الكهرباء والطاقة الشمسية والاتصالات والمصانع.",
        "Laser engraved cable identification tags in stainless steel and aluminium in Jeddah: cable and circuit numbers, source and destination, with stainless ties, for electrical, solar, telecom and industrial projects.",
    ),
    "schema_offers": [
        ("تاقات كيابل ستانلس 316", "Stainless 316 cable tags"),
        ("تاقات كيابل ألمنيوم", "Aluminium cable tags"),
        ("تاقات كيابل الطاقة الشمسية", "Solar cable tags"),
        ("أربطة كيابل ستانلس", "Stainless cable ties"),
    ],
    "hero": {
        "eyebrow": ("Cable Tags · كهرباء واتصالات", "Cable tags · power and telecom"),
        "h1": ("تاقات كيابل محفورة لا تُمحى", "Engraved cable tags that never wipe off"),
        "sub": (
            "في غرفة الكهرباء أو محطة الطاقة الشمسية، الكيبل غير المعرَّف يعني ساعات من البحث عند أي عطل. نحفر تاقات الكيابل على ستانلس وألمنيوم برقم الكيبل ومصدره ووجهته — تصمد للحرارة والأشعة فوق البنفسجية والزيوت طوال عمر المنشأة.",
            "In an electrical room or a solar plant, an unidentified cable means hours of searching at every fault. We engrave cable tags in stainless and aluminium with the cable number, source and destination — they withstand heat, UV and oils for the life of the facility.",
        ),
        "chips": [
            ("ستانلس 316 مقاوم للأشعة", "UV-proof stainless 316", "shield"),
            ("أربطة ستانلس مرفقة", "Stainless ties included", "check"),
            ("ترقيم من ملف إكسل", "Numbering from Excel", "file"),
            ("مقاومة حرارة عالية", "High heat resistance", "bolt"),
        ],
        "img": ("assets/img/svc/tags-cable-bundle.jpg", ("تاقات ستانلس محفور عليها أرقام الكيابل ومثبّتة بأربطة على حزمة كيابل", "Stainless tags engraved with cable numbers, tied onto a cable bundle"), 1200, 900),
        "wa": WA,
    },
    "facts": [
        (("316", "316"), ("ستانلس لا يتأثر بالشمس", "Sun-proof stainless")),
        (("0.5 mm", "0.5 mm"), ("سماكة مرنة تلتف حول الكيبل", "Flexible thickness that wraps the cable")),
        (("1000+", "1000+"), ("تاق في الطلبية بلا أخطاء نسخ", "Tags per order with no retyping errors")),
        (("100%", "100%"), ("مطابقة مع جدول الكيابل", "Matched to the cable schedule")),
    ],
    "intro": {
        "h2": ("لماذا تاقات الكيابل المعدنية بدل الملصقات؟", "Why metal cable tags instead of stickers?"),
        "paras": [
            (
                "ملصقات الكيابل البلاستيكية تتقصّف تحت شمس جدة وحرارة غرف الكهرباء، وتنفصل مع الزيت والغبار. أما التاق المعدني المحفور فلا يحتوي حبراً يبهت أصلاً — الرقم محفور في المعدن نفسه ويبقى مقروءاً بعد عشرين سنة.",
                "Plastic cable labels crack under Jeddah's sun and the heat of electrical rooms, and peel with oil and dust. An engraved metal tag has no ink to fade at all — the number is engraved into the metal itself and stays legible after twenty years.",
            ),
            (
                "ولهذا تُطلب التاقات المعدنية في مواصفات محطات التحويل، والطاقة الشمسية، ومصانع البتروكيماويات، وأنظمة الحريق — كل مكان تكون فيه معرفة الكيبل الصحيح مسألة سلامة لا مجرد تنظيم.",
                "That is why metal tags are specified for substations, solar plants, petrochemical facilities and fire systems — anywhere knowing the right cable is a matter of safety, not just order.",
            ),
        ],
        "h3": ("ماذا يُحفر على تاق الكيبل؟", "What goes on a cable tag?"),
        "bullets": [
            ("رقم الكيبل كما في جدول الكيابل (Cable Schedule).", "The cable number as in the cable schedule."),
            ("المصدر والوجهة: من لوحة MDB-01 إلى DB-2F مثلاً.", "Source and destination: from MDB-01 to DB-2F, for example."),
            ("نوع الكيبل ومقطعه أو الجهد: 4C×95 mm² أو DC 1000V.", "Cable type and size or voltage: 4C×95 mm² or DC 1000V."),
            ("للطاقة الشمسية: رقم السلسلة (String) والقطبية + / −.", "For solar: string number and polarity + / −."),
        ],
    },
    "cards": {
        "eyebrow": ("أين تُستخدم", "Where they are used"),
        "h2": ("تطبيقات تاقات الكيابل", "Cable tag applications"),
        "items": [
            {"icon": "bolt", "h3": ("لوحات التوزيع والمحولات", "Switchgear and transformers"), "p": ("تعريف كيابل الدخول والخروج في كل لوحة.", "Identifying incoming and outgoing cables at every board.")},
            {"icon": "target", "h3": ("محطات الطاقة الشمسية", "Solar plants"), "p": ("ترقيم السلاسل والقطبية على كيابل DC المعرّضة للشمس طوال اليوم.", "String and polarity numbering on DC cables exposed to the sun all day.")},
            {"icon": "globe", "h3": ("الاتصالات والألياف", "Telecom and fibre"), "p": ("تاقات صغيرة للألياف البصرية وكيابل الشبكات في غرف الخوادم.", "Small tags for fibre optics and network cables in server rooms.")},
            {"icon": "factory", "h3": ("المصانع والبتروكيماويات", "Factories and petrochemicals"), "p": ("ستانلس 316 يتحمل الأبخرة الكيميائية والزيوت.", "Stainless 316 that handles chemical fumes and oils.")},
            {"icon": "shield", "h3": ("أنظمة الحريق والإنذار", "Fire and alarm systems"), "p": ("تعريف دوائر الإنذار والمضخات لسرعة الاستجابة.", "Identifying alarm circuits and pumps for faster response.")},
            {"icon": "build", "h3": ("الأنفاق والممرات الأرضية", "Tunnels and trenches"), "p": ("تاقات على مسافات منتظمة لتتبّع الكيبل على طول مساره.", "Tags at regular intervals to trace a cable along its route.")},
        ],
    },
    "specs": {
        "soft": True,
        "eyebrow": ("مواصفات", "Specs"),
        "h2": ("الأشكال والمقاسات المعتادة", "Usual shapes and sizes"),
        "cols": [("النوع", "Type"), ("المقاس الشائع", "Common size"), ("طريقة التثبيت", "Fixing")],
        "rows": [
            [("شريحة مستطيلة بفتحتين", "Strip with two slots"), ("60×20 مم إلى 100×25 مم", "60×20 mm to 100×25 mm"), ("رباط ستانلس يمر عبر الفتحتين", "Stainless tie through both slots")],
            [("شريحة مرنة ملفوفة", "Flexible wrap-around"), ("سماكة 0.3 – 0.5 مم", "0.3 – 0.5 mm thick"), ("تلتف حول الكيبل مباشرة", "Wraps directly around the cable")],
            [("قرص دائري", "Round disc"), ("قطر 25 – 38 مم", "25 – 38 mm diameter"), ("رباط أو سلك ستانلس", "Stainless tie or wire")],
            [("تاق مع حروف منفصلة", "Tag with separate characters"), ("حسب طول النص", "By text length"), ("للكيابل الكثيرة المتشابهة", "For many similar cables")],
        ],
        "note": (
            "نحدد ارتفاع الحروف حسب مسافة القراءة: 4 مم للوحات القريبة، و6–8 مم للكيابل في الممرات والأنفاق.",
            "We set character height by reading distance: 4 mm for close boards, 6–8 mm for cables in trenches and tunnels.",
        ),
    },
    "gallery": {
        "eyebrow": ("نماذج", "Samples"),
        "h2": ("تاقات الكيابل عن قرب", "Cable tags up close"),
        "items": [
            ("assets/img/svc/tags-cable-sequence.jpg", ("15 تاق كيبل ستانلس مرقّمة بالتسلسل من CABLE-001 إلى CABLE-015", "15 stainless cable tags numbered in sequence from CABLE-001 to CABLE-015"), ("ترقيم متسلسل", "Sequential numbering"), 1200, 900),
            ("assets/img/svc/tags-cable-coil.jpg", ("تاقات مرقّمة مربوطة على لفّة كيبل", "Numbered tags tied on a cable coil"), ("على لفّة الكيبل", "On the cable coil"), 1200, 655),
            ("assets/img/svc/tags-cable-single.jpg", ("تاق كيبل ستانلس محفور عليه نوع الكيبل والجهد", "Stainless cable tag engraved with cable type and voltage"), ("بيانات الكيبل", "Cable data"), 1200, 655),
        ],
        "note": GALLERY_NOTE,
    },
    "process": process(("من جدول الكيابل إلى التاقات", "From the cable schedule to the tags")),
    "related": {
        "eyebrow": ("للمشروع نفسه", "For the same project"),
        "h2": ("منتجات تعريف مكمّلة", "Complementary identification"),
        "items": [
            {"icon": "engrave", "href": "traffolyte-engraving.html", "h3": ("لوحات ترافوليت", "Traffolyte labels"), "p": ("تسميات لوحات التوزيع والقواطع داخل غرفة الكهرباء.", "Board and breaker labels inside the electrical room.")},
            {"icon": "sliders", "href": "valve-tags.html", "h3": ("تاقات المحابس", "Valve tags"), "p": ("نفس المنطق لأعمال الميكانيكا والسباكة.", "The same logic for mechanical and plumbing works.")},
            {"icon": "shield", "href": "safety-signs.html", "h3": ("لوحات السلامة", "Safety signs"), "p": ("خطر كهرباء، ممنوع الدخول، ومعدات الوقاية.", "High voltage, no entry and PPE signs.")},
        ],
    },
    "faq": [
        {
            "q": ("هل تتحمل التاقات حرارة غرف الكهرباء وشمس الصيف؟", "Do the tags survive electrical room heat and summer sun?"),
            "a": (
                "نعم. الستانلس 316 والألمنيوم لا يتأثران بالأشعة فوق البنفسجية ولا بحرارة الصيف، والحفر لا يحتوي حبراً يبهت. التاق يعيش عمر الكيبل نفسه.",
                "Yes. Stainless 316 and aluminium are unaffected by UV and summer heat, and the engraving contains no ink to fade. The tag lives as long as the cable.",
            ),
        },
        {
            "q": ("هل توفرون أربطة الكيابل الستانلس؟", "Do you supply stainless cable ties?"),
            "a": (
                "نعم، نوفّر أربطة ستانلس بأطوال مناسبة لأقطار الكيابل في مشروعك، أو نجهّز التاقات بفتحات تناسب الأربطة التي لديك.",
                "Yes, we supply stainless ties in lengths suited to your cable diameters, or prepare the tags with slots that fit the ties you already have.",
            ),
        },
        {
            "q": ("لدي آلاف الكيابل — كيف نتجنّب الأخطاء؟", "I have thousands of cables — how do we avoid mistakes?"),
            "a": (
                "نستورد جدول الكيابل مباشرة من ملف إكسل فلا يُعاد كتابة أي رقم يدوياً، ثم نراجع الناتج 100% ونسلّم التاقات مرتّبة ومغلّفة حسب اللوحة أو المنطقة.",
                "We import the cable schedule straight from Excel so no number is retyped by hand, check the result 100%, and deliver the tags sorted and bagged by board or area.",
            ),
        },
        {
            "q": ("هل يمكن حفر التاق باللغة العربية؟", "Can the tag be engraved in Arabic?"),
            "a": (
                "نعم، رغم أن أرقام الكيابل تُكتب عادة بالإنجليزية لتطابق المخططات. يمكن إضافة وصف عربي مثل «مضخة الحريق» تحت الرقم.",
                "Yes, although cable numbers are usually in English to match the drawings. An Arabic description such as “fire pump” can be added under the number.",
            ),
        },
    ],
    "form_services": [
        ("تاقات كيابل ستانلس", "Stainless cable tags"),
        ("تاقات كيابل ألمنيوم", "Aluminium cable tags"),
        ("تاقات طاقة شمسية", "Solar cable tags"),
        ("أربطة ستانلس", "Stainless ties"),
        ("أخرى / غير متأكد", "Other / not sure"),
    ],
    "form_wa": WA,
    "quote_h2": ("أرسل جدول الكيابل", "Send your cable schedule"),
    "quote_lead": (
        "اذكر العدد التقريبي ونوع البيئة (داخلي، خارجي، شمسي)، وأرفق القائمة إن وجدت.",
        "Tell us the approximate count and environment (indoor, outdoor, solar), and attach the list if you have it.",
    ),
    "cta": {
        "h2": ("كل كيبل معروف المسار", "Every cable traceable"),
        "p": ("أرسل الجدول، وتصلك معاينة وعرض سعر في نفس يوم العمل غالباً.", "Send the schedule and usually get a proof and quote the same working day."),
        "wa": WA,
    },
}
