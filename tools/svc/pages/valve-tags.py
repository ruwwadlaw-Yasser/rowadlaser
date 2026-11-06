# -*- coding: utf-8 -*-
"""تاقات المحابس (Valve Tags) — تحت اللوحات والتاقات التعريفية"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _eng import GALLERY_NOTE, TAGS_PARENT, g, hero_img, process  # noqa: E402

WA = "مرحباً رواد الليزر، أرغب في عرض سعر لتاقات محابس (Valve Tags) محفورة."

PAGE = {
    "slug": "valve-tags",
    "parent": TAGS_PARENT,
    "crumb": ("تاقات المحابس", "Valve tags"),
    "title": (
        "تاقات محابس محفورة في جدة | Valve Tags ستانلس وبراص وألمنيوم — رواد الليزر",
        "Engraved Valve Tags in Jeddah | Stainless, Brass &amp; Aluminium — Ruwwad Laser",
    ),
    "desc": (
        "تاقات محابس (Valve Tags) محفورة بالليزر في جدة: أقراص ستانلس 316 وبراص وألمنيوم ملوّن بترقيم المحابس ونوع الخط، مع سلاسل أو حلقات تثبيت. ترقيم من ملف إكسل ولمشاريع MEP كاملة.",
        "Laser engraved valve tags in Jeddah: stainless 316, brass and coloured aluminium discs with valve numbers and line service, supplied with chains or rings. Numbered from Excel, for complete MEP projects.",
    ),
    "og_image": "assets/img/svc/tags-valves-pipeline.jpg",
    "service_type": ("تاقات محابس محفورة", "Engraved valve tags"),
    "schema_name": ("تاقات المحابس المحفورة في جدة", "Engraved valve tags in Jeddah"),
    "schema_desc": (
        "تصنيع تاقات المحابس (Valve Tags) بالحفر بالليزر في جدة: أقراص دائرية أو مستطيلة من الستانلس ستيل والبراص والألمنيوم المؤكسد الملون، محفور عليها رقم المحبس ونوع الخط والحالة الطبيعية، لمشاريع المياه والتكييف والحريق والغاز والبخار.",
        "Manufacture of laser engraved valve tags in Jeddah: round or rectangular discs in stainless steel, brass and coloured anodised aluminium, engraved with valve number, line service and normal position, for water, HVAC, fire, gas and steam systems.",
    ),
    "schema_offers": [
        ("تاقات محابس ستانلس 316", "Stainless 316 valve tags"),
        ("تاقات محابس براص", "Brass valve tags"),
        ("تاقات محابس ألمنيوم ملوّن", "Coloured aluminium valve tags"),
        ("جدول المحابس (Valve Chart)", "Valve chart / schedule"),
    ],
    "hero": {
        "eyebrow": ("Valve Tags · MEP", "Valve tags · MEP"),
        "h1": ("تاقات محابس محفورة بالليزر", "Laser engraved valve tags"),
        "sub": (
            "كل محبس في المبنى أو المصنع يحتاج رقماً يطابق المخطط. نحفر تاقات المحابس على أقراص ستانلس وبراص وألمنيوم ملوّن — رقم المحبس، نوع الخط، وحالته — فيعرف فريق الصيانة أي محبس يغلق في ثوانٍ، حتى بعد سنوات.",
            "Every valve in a building or plant needs a number that matches the drawing. We engrave valve tags on stainless, brass and coloured aluminium discs — valve number, line service and position — so maintenance knows which valve to close in seconds, even years later.",
        ),
        "chips": [
            ("ستانلس · براص · ألمنيوم", "Stainless · brass · aluminium", "layers"),
            ("ألوان حسب نوع الخط", "Colours by line service", "target"),
            ("ترقيم من ملف إكسل", "Numbering from Excel", "file"),
            ("سلاسل وحلقات تثبيت", "Chains and rings supplied", "check"),
        ],
        "img": ("assets/img/svc/tags-valves-pipeline.jpg", ("تاقات محابس من الستانلس والبراص والألمنيوم الملوّن معلّقة على خط أنابيب", "Stainless, brass and coloured aluminium valve tags hanging on a pipeline"), 1200, 900),
        "wa": WA,
    },
    "facts": [
        (("38–50 mm", "38–50 mm"), ("أشهر أقطار الأقراص", "Most common disc diameters")),
        (("316", "316"), ("الستانلس المرشّح للخارج والساحل", "Recommended stainless for outdoor/coastal")),
        (("6", "6"), ("ساعات لبدء التنفيذ", "Hours to start production")),
        (("100%", "100%"), ("مطابقة الأرقام مع جدولك", "Numbers matched to your schedule")),
    ],
    "intro": {
        "h2": ("ما هي تاقات المحابس ولماذا تُطلب عند التسليم؟", "What valve tags are and why handover requires them"),
        "paras": [
            (
                "تاق المحبس قرص معدني صغير يُعلَّق على ذراع أو جسم المحبس بسلسلة أو حلقة، ويحمل رقماً فريداً يطابق رقم المحبس في المخطط وجدول المحابس (Valve Chart). عند حدوث تسريب أو صيانة، يرجع الفني للجدول ويغلق المحبس الصحيح فوراً بدلاً من التجربة.",
                "A valve tag is a small metal disc hung on the valve handle or body with a chain or ring, carrying a unique number that matches the valve on the drawing and the valve chart. In a leak or during maintenance, the technician checks the chart and closes the right valve immediately instead of guessing.",
            ),
            (
                "لذلك يطلب الاستشاري تاقات المحابس ضمن متطلبات تسليم أعمال الميكانيكا والسباكة والحريق والتكييف. ولأن التاقات تبقى سنوات قرب الماء والبخار والحرارة، فإن الحفر على المعدن هو الخيار العملي الوحيد — الملصقات والطباعة لا تصمد.",
                "That is why consultants require valve tags in the handover of mechanical, plumbing, fire and HVAC works. And since tags spend years near water, steam and heat, engraving on metal is the only practical option — stickers and print do not last.",
            ),
        ],
        "h3": ("ماذا يُكتب على تاق المحبس عادةً؟", "What is usually engraved on a valve tag?"),
        "bullets": [
            ("رقم المحبس الفريد، مثل V-101 أو HV-2001 — بأكبر خط ممكن.", "The unique valve number, e.g. V-101 or HV-2001 — as large as possible."),
            ("نوع الخط أو الخدمة: مياه مبردة، مياه حريق، غاز، بخار، صرف.", "Line service: chilled water, fire water, gas, steam, drainage."),
            ("الحالة الطبيعية للمحبس: مفتوح دائماً NO أو مغلق دائماً NC.", "Normal position: normally open (NO) or normally closed (NC)."),
            ("اختيارياً: الطابق أو المنطقة، وشعار المالك أو المقاول.", "Optionally: floor or zone, and the owner's or contractor's logo."),
        ],
    },
    "cards": {
        "eyebrow": ("الأنواع", "Types"),
        "h2": ("خيارات تاقات المحابس", "Valve tag options"),
        "items": [
            {
                "icon": "shield",
                "h3": ("ستانلس ستيل 316", "Stainless steel 316"),
                "p": ("الأقوى للخارج والمناطق الساحلية والمحطات — نقش أسود أو حفر غائر لا يصدأ.", "The toughest for outdoor, coastal and plant use — black marking or recessed, rust-free."),
            },
            {
                "icon": "target",
                "h3": ("براص (نحاس أصفر)", "Brass"),
                "p": ("الشكل الكلاسيكي لتاقات المحابس، بحفر غائر يمكن تعبئته بلون أسود.", "The classic valve tag look, recessed engraving that can be filled black."),
                "href": "brass-engraving.html",
                "more": ("الحفر على البراص", "Brass engraving"),
            },
            {
                "icon": "layers",
                "h3": ("ألمنيوم مؤكسد ملوّن", "Coloured anodised aluminium"),
                "p": ("لون لكل خدمة: أحمر للحريق، أزرق للمياه، أصفر للغاز — خفيف واقتصادي.", "A colour per service: red for fire, blue for water, yellow for gas — light and economical."),
                "href": "aluminum-engraving.html",
                "more": ("الحفر على الألمنيوم", "Aluminium engraving"),
            },
            {
                "icon": "cube",
                "h3": ("بلاستيك طبقات", "Laminated plastic"),
                "p": ("للمحابس الداخلية في البيئات الكيميائية حيث يُفضّل البلاستيك على المعدن.", "For indoor valves in chemical environments where plastic is preferred to metal."),
                "href": "traffolyte-engraving.html",
                "more": ("لوحات الترافوليت", "Traffolyte labels"),
            },
            {
                "icon": "file",
                "h3": ("جدول المحابس", "Valve chart"),
                "p": ("لوحة إطار تجمع أرقام كل المحابس ومواقعها، تُعلَّق في غرفة المضخات.", "A framed chart listing every valve and location, hung in the pump room."),
            },
            {
                "icon": "sliders",
                "h3": ("مقاسات وأشكال مخصصة", "Custom sizes and shapes"),
                "p": ("دائري، مستطيل، سداسي — بثقب واحد أو ثقبين حسب طريقة التعليق.", "Round, rectangular, hexagonal — one or two holes depending on fixing."),
            },
        ],
    },
    "specs": {
        "soft": True,
        "eyebrow": ("مواصفات شائعة", "Common specs"),
        "h2": ("المقاسات والألوان المعتادة", "Usual sizes and colours"),
        "cols": [("البند", "Item"), ("الخيار الشائع", "Common option"), ("ملاحظة", "Note")],
        "rows": [
            [("القطر", "Diameter"), ("38 مم، 50 مم، 65 مم", "38 mm, 50 mm, 65 mm"), ("50 مم الأكثر طلباً للمباني", "50 mm is most requested for buildings")],
            [("السماكة", "Thickness"), ("0.8 – 1.5 مم", "0.8 – 1.5 mm"), ("1 مم توازن بين الصلابة والوزن", "1 mm balances rigidity and weight")],
            [("الثقب", "Hole"), ("4 – 6 مم أعلى القرص", "4 – 6 mm at the top"), ("ثقبان للتثبيت المزدوج عند الطلب", "Two holes for double fixing on request")],
            [("التثبيت", "Fixing"), ("سلسلة كرات، حلقة S، رباط ستانلس", "Ball chain, S-hook, stainless tie"), ("نوفّرها مع الطلب", "Supplied with the order")],
            [("ألوان الخدمات", "Service colours"), ("أحمر حريق، أزرق مياه، أخضر، أصفر غاز", "Red fire, blue water, green, yellow gas"), ("نطابق نظام الألوان في مواصفات مشروعك", "We match the colour code in your spec")],
        ],
        "note": (
            "أرسل جدول المحابس من المخطط (Excel أو PDF)، ونجهّز التاقات مرتّبة ومغلّفة حسب الطابق أو النظام لتسهيل التركيب.",
            "Send the valve schedule from the drawings (Excel or PDF) and we deliver the tags sorted and bagged by floor or system for easy installation.",
        ),
    },
    "gallery": {
        "eyebrow": ("نماذج", "Samples"),
        "h2": ("تاقات المحابس والتعريف المعدني", "Valve tags and metal identification"),
        "items": [
            ("assets/img/svc/tags-valve-colours.jpg", ("تاقات محابس ألمنيوم ملوّنة حسب نوع الخط: حريق ومياه مبرّدة وغاز", "Coloured aluminium valve tags by line service: fire, chilled water and gas"), ("ألوان حسب الخط", "Colour by service"), 1200, 900),
            ("assets/img/svc/tags-valve-closeup.jpg", ("لقطة قريبة لتاق محبس ستانلس محفور CHW-102", "Close-up of an engraved stainless valve tag CHW-102"), ("عمق ووضوح الحفر", "Engraving depth and clarity"), 1200, 900),
            ("assets/img/svc/tags-valves-row.jpg", ("صف محابس عليها تاقات مرقّمة بألوان مختلفة", "A row of valves with numbered colour tags"), ("على المحابس", "On the valves"), 1200, 655),
        ],
        "note": GALLERY_NOTE,
    },
    "process": process(("من جدول المحابس إلى التاقات", "From the valve schedule to the tags")),
    "related": {
        "eyebrow": ("للمشروع نفسه", "For the same project"),
        "h2": ("ما يُطلب عادةً مع تاقات المحابس", "Usually ordered with valve tags"),
        "items": [
            {
                "icon": "bolt",
                "href": "cable-id-tags.html",
                "h3": ("تاقات الكيابل", "Cable ID tags"),
                "p": ("تعريف الكيابل الكهربائية ودوائرها في نفس التسليم.", "Electrical cable and circuit identification in the same handover."),
            },
            {
                "icon": "arrow",
                "href": "route-marker-plates.html",
                "h3": ("لوحات المسارات", "Route markers"),
                "p": ("علامات أرضية لمسارات المياه والغاز المدفونة.", "Ground markers for buried water and gas routes."),
            },
            {
                "icon": "target",
                "href": "loto-safety-tags.html",
                "h3": ("تاقات لوتو LOTO", "LOTO tags"),
                "p": ("بطاقات العزل والإغلاق أثناء صيانة المحابس والمضخات.", "Lockout tags during valve and pump maintenance."),
            },
        ],
    },
    "faq": [
        {
            "q": ("ما الفرق بين تاق المحبس الستانلس والبراص؟", "What is the difference between stainless and brass valve tags?"),
            "a": (
                "الستانلس 316 أقوى في البيئات الخارجية والمالحة ولا يحتاج أي صيانة. البراص يعطي الشكل التقليدي الدافئ ويقاوم الرطوبة جيداً لكنه يغمق مع الوقت (طبقة باتينا طبيعية لا تؤثر على قراءة الحفر). في جدة نرشّح الستانلس 316 للخارج والبراص أو الألمنيوم للداخل.",
                "Stainless 316 is stronger outdoors and in salty air and needs no maintenance. Brass gives the warm traditional look and handles humidity well, but darkens over time (a natural patina that does not affect legibility). In Jeddah we recommend 316 for outdoors and brass or aluminium indoors.",
            ),
        },
        {
            "q": ("هل يمكن أن يحمل كل تاق رقماً مختلفاً؟", "Can every tag carry a different number?"),
            "a": (
                "نعم، هذا هو الطبيعي. نستورد قائمتك من ملف إكسل ويُحفر كل تاق برقمه تلقائياً، ثم نراجع الأرقام 100% مقابل القائمة قبل التسليم.",
                "Yes, that is the norm. We import your list from Excel, each tag is engraved with its number automatically, and we check 100% of numbers against the list before delivery.",
            ),
        },
        {
            "q": ("هل تفي التاقات بمتطلبات الاستشاري؟", "Will the tags meet the consultant's requirements?"),
            "a": (
                "أرسل لنا بند المواصفات الخاص بالتعريف (Identification) من مستندات المشروع، ونلتزم بالمادة والمقاس والألوان وارتفاع الحروف المذكورة فيه، ونرسل عيّنة للاعتماد قبل التصنيع الكامل.",
                "Send us the identification clause from the project specification and we follow its material, size, colours and character height, sending a sample for approval before full production.",
            ),
        },
        {
            "q": ("هل تثبّتون التاقات في الموقع؟", "Do you install the tags on site?"),
            "a": (
                "نحن نصنّع ونسلّم التاقات جاهزة مع وسائل التثبيت، مرتّبة حسب الطابق أو النظام، ومعها نسخة من الجدول. التركيب نفسه يتم عادة بواسطة فريق المقاول في الموقع.",
                "We manufacture and deliver the tags ready with fixings, sorted by floor or system, along with a copy of the schedule. Installation itself is usually done by the contractor's team on site.",
            ),
        },
    ],
    "form_services": [
        ("تاقات محابس ستانلس", "Stainless valve tags"),
        ("تاقات محابس براص", "Brass valve tags"),
        ("تاقات محابس ألمنيوم ملوّن", "Coloured aluminium valve tags"),
        ("جدول محابس (Valve Chart)", "Valve chart"),
        ("أخرى / غير متأكد", "Other / not sure"),
    ],
    "form_wa": WA,
    "quote_h2": ("أرسل جدول المحابس", "Send your valve schedule"),
    "quote_lead": (
        "اذكر عدد التاقات والمادة المفضلة والقطر، وأرفق قائمة الأرقام إن وجدت.",
        "Tell us the number of tags, preferred material and diameter, and attach the number list if you have it.",
    ),
    "cta": {
        "h2": ("كل محبس برقمه — من أول يوم", "Every valve numbered — from day one"),
        "p": ("أرسل الجدول، وتصلك معاينة وعرض سعر في نفس يوم العمل غالباً.", "Send the schedule and usually get a proof and quote the same working day."),
        "wa": WA,
    },
}
