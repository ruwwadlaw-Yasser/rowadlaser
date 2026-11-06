# -*- coding: utf-8 -*-
"""اللوحات الإرشادية والتعريفية (Signage Plates) — تحت اللوحات والتاقات التعريفية"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _eng import GALLERY_NOTE, TAGS_PARENT, g, hero_img, process  # noqa: E402

WA = "مرحباً رواد الليزر، أرغب في عرض سعر للوحات إرشادية وتعريفية."

PAGE = {
    "slug": "signage-plates",
    "parent": TAGS_PARENT,
    "crumb": ("اللوحات الإرشادية", "Signage plates"),
    "title": (
        "لوحات إرشادية في جدة | لوحات أبواب ومكاتب وأقسام محفورة — رواد الليزر",
        "Signage Plates in Jeddah | Engraved Door, Office &amp; Department Signs — Ruwwad Laser",
    ),
    "desc": (
        "لوحات إرشادية وتعريفية في جدة: أرقام أبواب، لوحات مكاتب وأقسام، لوحات اتجاهات وطوابق، ولوحات دورات المياه — محفورة على ستانلس وبراص وألمنيوم وأكريليك، بالعربي والإنجليزي. للمكاتب والمستشفيات والفنادق والمدارس.",
        "Signage plates in Jeddah: door numbers, office and department plates, directional and floor signs and restroom signs — engraved on stainless, brass, aluminium and acrylic, in Arabic and English. For offices, hospitals, hotels and schools.",
    ),
    "og_image": "assets/img/svc/tags-office-door.jpg",
    "service_type": ("لوحات إرشادية وتعريفية", "Signage and wayfinding plates"),
    "schema_name": ("اللوحات الإرشادية في جدة", "Signage plates in Jeddah"),
    "schema_desc": (
        "تصنيع اللوحات الإرشادية والتعريفية الداخلية في جدة: أرقام الغرف والأبواب، أسماء المكاتب والأقسام، لوحات الطوابق والاتجاهات، لوحات دورات المياه والمصليات، محفورة على الستانلس والبراص والألمنيوم والأكريليك باللغتين العربية والإنجليزية.",
        "Manufacture of interior signage and wayfinding plates in Jeddah: room and door numbers, office and department names, floor and directional signs, restroom and prayer-room signs, engraved on stainless, brass, aluminium and acrylic in Arabic and English.",
    ),
    "schema_offers": [
        ("لوحات أرقام الأبواب والغرف", "Door and room number plates"),
        ("لوحات المكاتب والأقسام", "Office and department plates"),
        ("لوحات الاتجاهات والطوابق", "Directional and floor signs"),
        ("لوحات دورات المياه والمصليات", "Restroom and prayer-room signs"),
    ],
    "hero": {
        "eyebrow": ("لوحات إرشادية · مكاتب ومنشآت", "Signage · offices and facilities"),
        "h1": ("لوحات إرشادية وتعريفية محفورة", "Engraved signage and wayfinding plates"),
        "sub": (
            "الزائر الذي يجد طريقه بسهولة يأخذ انطباعاً احترافياً عن منشأتك. نصنع لوحات الأبواب والمكاتب والأقسام والاتجاهات بتصميم موحّد يناسب هويتك — ستانلس مصقول، براص فاخر، ألمنيوم ملوّن أو أكريليك — بالعربي والإنجليزي.",
            "A visitor who finds their way easily leaves with a professional impression of your facility. We make door, office, department and directional plates in a unified design that matches your identity — brushed stainless, premium brass, coloured aluminium or acrylic — in Arabic and English.",
        ),
        "chips": [
            ("تصميم موحّد بهويتك", "Unified with your identity", "target"),
            ("عربي + إنجليزي", "Arabic + English", "globe"),
            ("ستانلس · براص · أكريليك", "Stainless · brass · acrylic", "layers"),
            ("لمكتب أو مبنى كامل", "For an office or a whole building", "store"),
        ],
        "img": ("assets/img/svc/tags-office-door.jpg", ("لوحة ستانلس محفورة «إدارة المشاريع — مكتب 101» مثبّتة على باب", "Engraved stainless plate «Project Management — Office 101» on a door"), 1200, 900),
        "wa": WA,
    },
    "facts": [
        (("+5", "+5"), ("مواد وتشطيبات للاختيار", "Materials and finishes to choose")),
        (("2", "2"), ("لغتان على كل لوحة", "Two languages on every plate")),
        (("6", "6"), ("ساعات لبدء التنفيذ", "Hours to start production")),
        (("100%", "100%"), ("مراجعة الأسماء قبل التنفيذ", "Names checked before production")),
    ],
    "intro": {
        "h2": ("لوحات تنظّم المكان وتعكس هويتك", "Plates that organise the space and reflect your identity"),
        "paras": [
            (
                "اللوحات الإرشادية ليست مجرد أسماء على الأبواب؛ هي نظام كامل يقود الزائر من المدخل إلى المكتب المطلوب: لوحة الطابق، ثم الاتجاه، ثم اسم القسم، ثم رقم الغرفة. عندما تكون كل هذه اللوحات بنفس التصميم والمادة، يبدو المكان منظماً واحترافياً.",
                "Signage plates are not just names on doors; they form a complete system that leads a visitor from the entrance to the right office: floor sign, then direction, then department name, then room number. When all of them share the same design and material, the place looks organised and professional.",
            ),
            (
                "نحفر النصوص بالليزر فلا تُمحى بالتنظيف اليومي ولا تتقشّر كالملصقات، ونقصّ اللوحة بالشكل الذي تريده — مستطيلة، بزوايا دائرية، أو بشكل مخصص — مع خيارات تثبيت بالبراغي أو اللاصق أو الفواصل المعدنية.",
                "We laser engrave the text so it never wipes off with daily cleaning or peels like stickers, and cut the plate to the shape you want — rectangular, rounded corners or a custom shape — with screw, adhesive or metal standoff fixing.",
            ),
        ],
        "h3": ("أين تُستخدم؟", "Where are they used?"),
        "bullets": [
            ("الشركات والمكاتب: أسماء الإدارات والمدراء وغرف الاجتماعات.", "Companies and offices: department and manager names, meeting rooms."),
            ("المستشفيات والعيادات: أرقام العيادات والأقسام والاتجاهات.", "Hospitals and clinics: clinic numbers, departments and directions."),
            ("الفنادق والشقق: أرقام الغرف والطوابق والمرافق.", "Hotels and apartments: room numbers, floors and amenities."),
            ("المدارس والجامعات والمساجد: الفصول والقاعات والمصليات ودورات المياه.", "Schools, universities and mosques: classrooms, halls, prayer rooms and restrooms."),
        ],
    },
    "cards": {
        "eyebrow": ("الأنواع", "Types"),
        "h2": ("لوحات لكل ركن في المبنى", "Plates for every corner of the building"),
        "items": [
            {"icon": "store", "h3": ("لوحات الأبواب والغرف", "Door and room plates"), "p": ("رقم الغرفة واسمها، وأحياناً اسم الموظف بإطار قابل للتغيير.", "Room number and name, sometimes the occupant's name in a changeable frame.")},
            {"icon": "user", "h3": ("لوحات المكاتب والمدراء", "Office and manager plates"), "p": ("ستانلس أو براص فاخر بالاسم والمسمى الوظيفي.", "Premium stainless or brass with name and job title.")},
            {"icon": "arrow", "h3": ("لوحات الاتجاهات", "Directional signs"), "p": ("أسهم وأسماء الأقسام عند الممرات والمصاعد.", "Arrows and department names at corridors and lifts.")},
            {"icon": "layers", "h3": ("لوحات الطوابق", "Floor signs"), "p": ("رقم الطابق ودليل الأقسام فيه عند المصعد والدرج.", "Floor number and department directory by the lift and stairs.")},
            {"icon": "check", "h3": ("لوحات المرافق", "Facility signs"), "p": ("دورات المياه، المصلى، غرفة الكهرباء، المستودع.", "Restrooms, prayer room, electrical room, storage.")},
            {"icon": "file", "h3": ("لوحات المداخل", "Entrance plaques"), "p": ("لوحة اسم الشركة أو الفيلا بشعار محفور أو مقصوص بالليزر.", "Company or villa name plaque with an engraved or laser-cut logo."), "href": "metal-facades-signage.html", "more": ("الواجهات واللوحات المعدنية", "Metal facades and signage")},
        ],
    },
    "specs": {
        "soft": True,
        "eyebrow": ("المواد والتشطيبات", "Materials and finishes"),
        "h2": ("اختر الشكل الذي يناسب منشأتك", "Pick the look that suits your facility"),
        "cols": [("المادة", "Material"), ("الطابع", "Character"), ("الأنسب لـ", "Best for")],
        "rows": [
            [("ستانلس مصقول", "Brushed stainless"), ("عصري ونظيف، نقش أسود", "Modern and clean, black marking"), ("الشركات والمستشفيات", "Corporate and hospitals")],
            [("براص", "Brass"), ("فاخر وكلاسيكي", "Premium and classic"), ("مكاتب الإدارة والفلل والفنادق", "Executive offices, villas and hotels")],
            [("ألمنيوم مؤكسد ملوّن", "Coloured anodised aluminium"), ("ألوان الهوية، حفر فضي", "Brand colours, silver engraving"), ("المدارس والمكاتب الحديثة", "Schools and modern offices")],
            [("أكريليك شفاف أو ملوّن", "Clear or coloured acrylic"), ("أنيق مع فواصل معدنية", "Elegant with metal standoffs"), ("الاستقبال والعيادات", "Reception and clinics")],
            [("ABS طبقتين", "Two-layer ABS"), ("اقتصادي وعملي", "Economical and practical"), ("الكميات الكبيرة والمرافق", "Large quantities and utilities")],
        ],
    },
    "gallery": {
        "eyebrow": ("نماذج", "Samples"),
        "h2": ("أمثلة على اللوحات الإرشادية", "Signage examples"),
        "items": [
            ("assets/img/svc/tags-office-signs.jpg", ("لوحات مكاتب واستقبال ودورات مياه وقاعة اجتماعات", "Office, reception, restroom and conference room plates"), ("لوحات المكاتب", "Office plates"), 1200, 900),
            ("assets/img/svc/tags-reception.jpg", ("لوحتا استقبال من الستانلس والأكريليك الأسود", "Reception plates in stainless and black acrylic"), ("خامتان", "Two materials"), 1200, 900),
            ("assets/img/svc/tags-plastic-signs.jpg", ("لوحات إرشادية بالأبيض والأسود والفضي", "Signage plates in white, black and silver"), ("ألوان متعددة", "Several colours"), 1200, 670),
        ],
        "note": GALLERY_NOTE,
    },
    "process": process(("من قائمة الغرف إلى التركيب", "From the room list to installation")),
    "related": {
        "eyebrow": ("مكمّلات", "Complements"),
        "h2": ("منتجات مرتبطة", "Related products"),
        "items": [
            {"icon": "user", "href": "name-badges.html", "h3": ("بادجات الأسماء", "Name badges"), "p": ("بنفس هوية اللوحات لموظفيك.", "Matching your signage for your staff.")},
            {"icon": "shield", "href": "safety-signs.html", "h3": ("لوحات السلامة", "Safety signs"), "p": ("مخارج الطوارئ وطفايات الحريق ونقاط التجمّع.", "Emergency exits, extinguishers and assembly points.")},
            {"icon": "engrave", "href": "acrylic-engraving.html", "h3": ("الحفر على الأكريليك", "Acrylic engraving"), "p": ("لوحات ودروع أكريليك بحفر مثلّج أنيق.", "Acrylic plates and awards with elegant frosted engraving.")},
        ],
    },
    "faq": [
        {
            "q": ("هل يمكن تصميم اللوحات بهوية شركتنا؟", "Can the plates follow our brand identity?"),
            "a": (
                "نعم. أرسل الشعار ودليل الهوية (الألوان والخطوط) إن وجد، ونصمم نموذجاً موحّداً تُطبَّق عليه كل اللوحات، ونرسل معاينة لكل اللوحات قبل التنفيذ.",
                "Yes. Send the logo and brand guidelines (colours and fonts) if available, and we design a unified template applied to every plate, sending a proof of all plates before production.",
            ),
        },
        {
            "q": ("أسماء الموظفين تتغير — هل هناك حل؟", "Staff names change — is there a solution?"),
            "a": (
                "نعم: لوحة ثابتة محفورة برقم الغرفة واسم القسم، مع إطار أو شريحة قابلة للاستبدال لاسم الموظف. عند التغيير تطلب شريحة جديدة فقط بتكلفة بسيطة.",
                "Yes: a fixed plate engraved with the room number and department, plus a replaceable frame or insert for the occupant's name. When it changes, you only order a new insert at low cost.",
            ),
        },
        {
            "q": ("هل تنفّذون لوحات مبنى كامل؟", "Do you do signage for a whole building?"),
            "a": (
                "نعم. أرسل قائمة الغرف والطوابق (أو مخطط المبنى) ونجهّز جدولاً بكل اللوحات وأماكنها، وتُسلَّم مرقّمة ومرتّبة حسب الطابق لتسهيل التركيب.",
                "Yes. Send the room and floor list (or building plan) and we prepare a schedule of every plate and its location, delivered numbered and sorted by floor for easy installation.",
            ),
        },
        {
            "q": ("ما طرق التثبيت؟", "How are they fixed?"),
            "a": (
                "لاصق ثنائي الوجه قوي للأسطح الملساء، براغي مخفية أو ظاهرة، أو فواصل معدنية (Standoffs) تعطي اللوحة بعداً عن الجدار — الأخيرة هي الأشهر مع الأكريليك.",
                "Strong double-sided tape for smooth surfaces, hidden or visible screws, or metal standoffs that lift the plate off the wall — the latter is most popular with acrylic.",
            ),
        },
    ],
    "form_services": [
        ("لوحات أبواب وغرف", "Door and room plates"),
        ("لوحات مكاتب ومدراء", "Office and manager plates"),
        ("لوحات اتجاهات وطوابق", "Directional and floor signs"),
        ("لوحات مبنى كامل", "Whole-building signage"),
        ("أخرى / غير متأكد", "Other / not sure"),
    ],
    "form_wa": WA,
    "quote_h2": ("أرسل قائمة اللوحات أو مخطط المبنى", "Send your plate list or building plan"),
    "quote_lead": (
        "اذكر المادة المفضلة والمقاس التقريبي وعدد اللوحات، وأرفق الشعار إن وجد.",
        "Tell us the preferred material, approximate size and number of plates, and attach your logo if you have one.",
    ),
    "cta": {
        "h2": ("منشأة منظّمة من أول نظرة", "An organised facility at first glance"),
        "p": ("أرسل القائمة، وتصلك معاينة وعرض سعر في نفس يوم العمل غالباً.", "Send the list and usually get a proof and quote the same working day."),
        "wa": WA,
    },
}
