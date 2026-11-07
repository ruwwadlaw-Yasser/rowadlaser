# -*- coding: utf-8 -*-
"""باقة تعريف مشاريع MEP — باقة كاملة للمقاولين (أُضيفت 2026-11-07) — تحت اللوحات والتاقات"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _eng import GALLERY_NOTE, TAGS_PARENT, process  # noqa: E402

WA = "مرحباً رواد الليزر، أرغب في عرض سعر لباقة تعريف مشروع MEP (تاقات ولوحات)."

PAGE = {
    "slug": "mep-identification-package",
    "parent": TAGS_PARENT,
    "crumb": ("باقة تعريف مشاريع MEP", "MEP identification package"),
    "title": (
        "باقة تعريف مشاريع MEP في جدة | تاقات محابس وكيابل ولوحات سلامة للمقاولين — رواد الليزر",
        "MEP Identification Package in Jeddah | Valve, Cable &amp; Safety Labels for Contractors — Ruwwad Laser",
    ),
    "desc": (
        "باقة تعريف كاملة لمشاريع الميكانيكا والكهرباء والسباكة (MEP) في جدة: تاقات محابس، تاقات كيابل، تسميات لوحات الكهرباء، تاقات لوتو، لوحات سلامة ومسارات — من جدول واحد ومورد واحد، محفورة بالليزر ومرتّبة حسب الطابق والنظام.",
        "A complete identification package for MEP projects in Jeddah: valve tags, cable tags, electrical panel labels, LOTO tags, safety signs and route markers — from one schedule and one supplier, laser engraved and sorted by floor and system.",
    ),
    "og_image": "assets/img/svc/tags-valves-pipeline.jpg",
    "service_type": ("باقة تعريف مشاريع MEP", "MEP identification package"),
    "schema_name": ("باقة تعريف مشاريع MEP في جدة", "MEP identification package in Jeddah"),
    "schema_desc": (
        "تصنيع وتوريد باقة التعريف الكاملة لمشاريع الميكانيكا والكهرباء والسباكة والحريق في جدة: تاقات المحابس، تاقات الكيابل، تسميات اللوحات الكهربائية، تاقات العزل والإغلاق LOTO، لوحات السلامة، ولوحات مسارات الأنابيب والكيابل — محفورة بالليزر من جداول المشروع ومسلّمة مرتّبة حسب الطابق والنظام.",
        "Manufacture and supply of the complete identification package for mechanical, electrical, plumbing and fire projects in Jeddah: valve tags, cable tags, electrical panel labels, LOTO tags, safety signs and pipe and cable route markers — laser engraved from the project schedules and delivered sorted by floor and system.",
    ),
    "schema_offers": [
        ("تاقات المحابس", "Valve tags"),
        ("تاقات الكيابل", "Cable ID tags"),
        ("تسميات اللوحات الكهربائية", "Electrical panel labels"),
        ("تاقات لوتو ولوحات السلامة", "LOTO tags and safety signs"),
        ("لوحات مسارات الأنابيب والكيابل", "Pipe and cable route markers"),
    ],
    "hero": {
        "eyebrow": ("للمقاولين · MEP", "For contractors · MEP"),
        "h1": ("باقة تعريف مشاريع MEP", "MEP project identification package"),
        "sub": (
            "قبل تسليم المشروع يطلب الاستشاري تعريف كل محبس وكيبل ولوحة. بدل أن تجمعها من أكثر من ورشة، أرسل لنا جداول المشروع ونسلّمك الباقة كاملة: تاقات المحابس والكيابل، تسميات اللوحات، تاقات لوتو ولوحات السلامة — مرقّمة من ملفك ومرتّبة حسب الطابق والنظام.",
            "Before handover the consultant requires every valve, cable and panel to be identified. Instead of collecting them from several workshops, send us the project schedules and we deliver the whole package: valve and cable tags, panel labels, LOTO tags and safety signs — numbered from your file and sorted by floor and system.",
        ),
        "chips": [
            ("جدول واحد، مورد واحد", "One schedule, one supplier", "file"),
            ("مرتّبة حسب الطابق والنظام", "Sorted by floor and system", "layers"),
            ("عيّنة للاعتماد قبل الكمية", "Sample for approval first", "check"),
            ("تسليم على مراحل", "Phased delivery", "clock"),
        ],
        "img": ("assets/img/svc/tags-valves-pipeline.jpg", ("تاقات محابس مرقّمة معلّقة على خط أنابيب في مشروع MEP", "Numbered valve tags on a pipeline in an MEP project"), 1200, 900),
        "wa": WA,
    },
    "facts": [
        (("6+", "6+"), ("أنواع تعريف في باقة واحدة", "Identification types in one package")),
        (("100%", "100%"), ("مطابقة الأرقام مع جداولك", "Numbers matched to your schedules")),
        (("6", "6"), ("ساعات لبدء التنفيذ بعد الاعتماد", "Hours to start after approval")),
        (("1", "1"), ("جهة مسؤولة عن الباقة كلها", "Accountable supplier for it all")),
    ],
    "intro": {
        "h2": ("لماذا باقة واحدة بدل طلبات متفرقة؟", "Why one package instead of scattered orders?"),
        "paras": [
            (
                "تعريف أعمال MEP يأتي عادةً في آخر المشروع وتحت ضغط موعد التسليم: تاقات المحابس من ورشة، ولوحات السلامة من مطبعة، وتسميات اللوحات الكهربائية من مورد ثالث. والنتيجة أرقام لا تطابق الجداول، وألوان مختلفة بين الأنظمة، ومتابعة مع أكثر من جهة.",
                "MEP identification usually comes at the end of the project, under handover pressure: valve tags from one workshop, safety signs from a printer, panel labels from a third supplier. The result is numbers that don't match the schedules, colours that differ between systems, and follow-up with several parties.",
            ),
            (
                "في الباقة نستلم جداول المشروع مرة واحدة — جدول المحابس، جدول الكيابل، قائمة اللوحات — ونحفر كل قطعة برقمها من الملف، ونفحص الأرقام مقابل الجدول، ثم نسلّمها مغلّفة حسب الطابق أو النظام مع نسخة من الجدول لتسهيل التركيب والاستلام.",
                "With the package we receive the project schedules once — valve schedule, cable schedule, panel list — engrave every piece with its number from the file, check the numbers against the schedule, and deliver them bagged by floor or system with a copy of the schedule to make installation and inspection easy.",
            ),
        ],
        "h3": ("ما الذي تحتاجه منك الباقة؟", "What the package needs from you"),
        "bullets": [
            ("جداول المشروع (Excel أو PDF): المحابس، الكيابل، اللوحات الكهربائية.", "The project schedules (Excel or PDF): valves, cables, electrical panels."),
            ("بند التعريف (Identification) من مواصفات المشروع إن وُجد — المادة والمقاس والألوان وارتفاع الحروف.", "The identification clause from the project specification if available — material, size, colours and character height."),
            ("موعد التسليم المطلوب، وهل يُفضّل التسليم على مراحل حسب تقدّم الأعمال.", "The required delivery date, and whether phased delivery by work progress is preferred."),
        ],
    },
    "cards": {
        "eyebrow": ("مكوّنات الباقة", "What the package includes"),
        "h2": ("كل ما يحتاجه تعريف المشروع", "Everything project identification needs"),
        "items": [
            {"icon": "target", "h3": ("تاقات المحابس", "Valve tags"), "p": ("ستانلس أو براص أو ألمنيوم ملوّن حسب الخدمة، برقم المحبس ونوع الخط.", "Stainless, brass or service-coloured aluminium, with valve number and line service."), "href": "valve-tags.html", "more": ("تاقات المحابس", "Valve tags")},
            {"icon": "bolt", "h3": ("تاقات الكيابل", "Cable ID tags"), "p": ("شرائح ستانلس برقم الكيبل والدائرة، مع أربطة التثبيت.", "Stainless strips with cable and circuit numbers, with fixing ties."), "href": "cable-id-tags.html", "more": ("تاقات الكيابل", "Cable tags")},
            {"icon": "file", "h3": ("تسميات اللوحات الكهربائية", "Electrical panel labels"), "p": ("ترافوليت أو ألمنيوم ملوّن: اسم اللوحة، المفاتيح، ودوائر التوزيع.", "Traffolyte or coloured aluminium: panel name, switches and distribution circuits."), "href": "traffolyte-engraving.html", "more": ("لوحات الترافوليت", "Traffolyte labels")},
            {"icon": "shield", "h3": ("تاقات لوتو LOTO", "LOTO tags"), "p": ("بطاقات العزل والإغلاق لفرق الصيانة والتشغيل.", "Lockout/tagout tags for maintenance and operations teams."), "href": "loto-safety-tags.html", "more": ("تاقات لوتو", "LOTO tags")},
            {"icon": "check", "h3": ("لوحات السلامة", "Safety signs"), "p": ("لوحات التحذير والإلزام والطوارئ لغرف الكهرباء والمضخات.", "Warning, mandatory and emergency signs for electrical and pump rooms."), "href": "safety-signs.html", "more": ("لوحات السلامة", "Safety signs")},
            {"icon": "arrow", "h3": ("لوحات المسارات", "Route markers"), "p": ("علامات مسارات الأنابيب والكيابل المدفونة.", "Markers for buried pipe and cable routes."), "href": "route-marker-plates.html", "more": ("لوحات المسارات", "Route markers")},
        ],
    },
    "specs": {
        "soft": True,
        "eyebrow": ("ملخص الباقة", "Package summary"),
        "h2": ("المواد المعتادة لكل بند", "Usual materials per item"),
        "cols": [("البند", "Item"), ("المادة الشائعة", "Common material"), ("المصدر في المشروع", "Source in the project")],
        "rows": [
            [("تاقات المحابس", "Valve tags"), ("ستانلس 316، براص، ألمنيوم ملوّن", "Stainless 316, brass, coloured aluminium"), ("جدول المحابس", "Valve schedule")],
            [("تاقات الكيابل", "Cable tags"), ("ستانلس 304/316", "Stainless 304/316"), ("جدول الكيابل", "Cable schedule")],
            [("تسميات اللوحات", "Panel labels"), ("ترافوليت أو ألمنيوم مؤكسد", "Traffolyte or anodised aluminium"), ("قائمة اللوحات والدوائر", "Panel and circuit list")],
            [("لوتو ولوحات السلامة", "LOTO and safety signs"), ("ألمنيوم أو PVC حسب مكان التركيب", "Aluminium or PVC depending on location"), ("مواصفات السلامة للمشروع", "Project safety specification")],
            [("لوحات المسارات", "Route markers"), ("براص أو ستانلس", "Brass or stainless"), ("مخططات المسارات", "Route drawings")],
        ],
        "note": (
            "نرسل عيّنة من كل بند لاعتمادها من الاستشاري قبل تشغيل الكمية كاملة.",
            "We send a sample of each item for the consultant's approval before running the full quantity.",
        ),
    },
    "gallery": {
        "eyebrow": ("نماذج", "Samples"),
        "h2": ("من مكوّنات الباقة", "From the package"),
        "items": [
            ("assets/img/svc/tags-cable-bundle.jpg", ("تاقات ستانلس مرقّمة على حزمة كيابل", "Numbered stainless tags on a cable bundle"), ("تاقات الكيابل", "Cable tags"), 1200, 900),
            ("assets/img/svc/tags-panel-labels.jpg", ("تسميات ملوّنة للوحات الكهرباء: المفتاح الرئيسي ولوحة التوزيع ولوحة التحكم", "Coloured electrical panel labels: main switch, distribution board, control panel"), ("تسميات اللوحات", "Panel labels"), 1200, 900),
            ("assets/img/svc/tags-route-markers.jpg", ("علامات مسارات براص وستانلس للمياه والغاز والكهرباء", "Brass and stainless route markers for water, gas and electric lines"), ("لوحات المسارات", "Route markers"), 1200, 900),
        ],
        "note": GALLERY_NOTE,
    },
    "process": process(("من جداول المشروع إلى التسليم", "From the project schedules to delivery")),
    "related": {
        "eyebrow": ("للمقاولين", "For contractors"),
        "h2": ("خدمات أخرى لنفس المشروع", "More for the same project"),
        "items": [
            {"icon": "build", "href": "contracting-metal-projects.html", "h3": ("مشاريع المقاولات المعدنية", "Contracting metal projects"), "p": ("قص وتشكيل وتصنيع القطع المعدنية للمشروع بالكميات.", "Cutting, forming and fabricating the project's metal parts in quantity.")},
            {"icon": "file", "href": "metal-nameplates-serial-numbers.html", "h3": ("لوحات بيانات المعدات", "Equipment data plates"), "p": ("لوحات بيانات وأرقام تسلسلية للمضخات والمعدات.", "Data plates and serial numbers for pumps and equipment.")},
            {"icon": "store", "href": "signage-plates.html", "h3": ("اللوحات الإرشادية", "Signage plates"), "p": ("لوحات الأبواب والغرف والطوابق لنفس المبنى.", "Door, room and floor plates for the same building.")},
        ],
    },
    "faq": [
        {
            "q": ("هل يمكن طلب جزء من الباقة فقط؟", "Can I order only part of the package?"),
            "a": (
                "نعم. الباقة مرنة: يمكن أن تبدأ بتاقات المحابس والكيابل مثلاً ثم تضيف تسميات اللوحات ولوحات السلامة لاحقاً بنفس الترقيم والهوية.",
                "Yes. The package is flexible: you can start with valve and cable tags, for example, and add panel labels and safety signs later with the same numbering and look.",
            ),
        },
        {
            "q": ("هل تلتزمون بمواصفات الاستشاري؟", "Do you follow the consultant's specification?"),
            "a": (
                "أرسل لنا بند التعريف من مواصفات المشروع، ونلتزم بالمادة والمقاس والألوان وارتفاع الحروف المطلوبة، ونرسل عيّنة من كل بند لاعتمادها قبل تشغيل الكمية.",
                "Send us the identification clause of the project specification and we follow the required material, size, colours and character height, sending a sample of each item for approval before the full run.",
            ),
        },
        {
            "q": ("كيف تُسلَّم الباقة؟", "How is the package delivered?"),
            "a": (
                "مغلّفة ومرتّبة حسب الطابق أو النظام كما تطلب، مع نسخة من الجدول ووسائل التثبيت. وللمشاريع الكبيرة يمكن التسليم على مراحل حسب تقدّم الأعمال.",
                "Bagged and sorted by floor or system as you prefer, with a copy of the schedule and the fixings. For large projects, delivery can be phased to match work progress.",
            ),
        },
        {
            "q": ("كم تستغرق الباقة؟", "How long does the package take?"),
            "a": (
                "يبدأ التنفيذ خلال 6 ساعات من اعتماد العيّنات وعرض السعر، والمدة الكاملة تعتمد على عدد القطع والبنود — نحدّدها لك كتابياً مع عرض السعر.",
                "Production starts within 6 hours of approving the samples and the quote; the full duration depends on the number of pieces and items — we state it in writing with the quote.",
            ),
        },
    ],
    "form_services": [
        ("باقة تعريف MEP كاملة", "Full MEP identification package"),
        ("تاقات محابس وكيابل", "Valve and cable tags"),
        ("تسميات لوحات كهربائية", "Electrical panel labels"),
        ("لوحات سلامة ولوتو", "Safety signs and LOTO"),
        ("أخرى / غير متأكد", "Other / not sure"),
    ],
    "form_wa": WA,
    "quote_h2": ("أرسل جداول المشروع", "Send the project schedules"),
    "quote_lead": (
        "أرفق جدول المحابس أو الكيابل أو قائمة اللوحات، واذكر موعد التسليم المطلوب.",
        "Attach the valve or cable schedule or the panel list, and mention the required delivery date.",
    ),
    "cta": {
        "h2": ("تعريف المشروع كله — من جهة واحدة", "The whole project's identification — from one supplier"),
        "p": ("أرسل الجداول، وتصلك العيّنات وعرض السعر بسرعة.", "Send the schedules and get samples and a quote quickly."),
        "wa": WA,
    },
}
