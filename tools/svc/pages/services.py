# -*- coding: utf-8 -*-
"""صفحة الخدمات — المركز (Hub) الذي يربط كل صفحات الخدمات المستقلة"""

SERVICES = [
    ("laser-metal-cutting", "قص المعادن بالليزر", "Laser metal cutting"),
    ("metal-bending-forming", "تشكيل وثني المعادن", "Metal bending and forming"),
    ("stainless-steel-fabrication", "تصنيع الستانلس ستيل", "Stainless steel fabrication"),
    ("metal-fabrication", "تصنيع المعادن", "Metal fabrication"),
    ("fiber-marking", "الحفر والنحت على المعادن", "Metal engraving and fibre marking"),
    ("custom-metal-solutions", "الحلول المخصصة حسب الطلب", "Custom-made solutions"),
    ("contracting-metal-projects", "مشاريع المقاولات والكميات", "Contracting and bulk projects"),
    ("metal-finishing-quality", "التشطيب وفحص الجودة", "Finishing and quality control"),
]

ITEM_LIST = """<script type="application/ld+json">
  {"@context":"https://schema.org","@type":"ItemList","name":"خدمات رواد الليزر","itemListElement":[
""" + ",\n".join(
    '    {"@type":"ListItem","position":%d,"name":"%s","url":"https://rowadlaser.com/%s.html"}'
    % (i + 1, ar, slug)
    for i, (slug, ar, en) in enumerate(SERVICES)
) + """
  ]}
  </script>"""

WEBPAGE = """<script type="application/ld+json">
  {"@context":"https://schema.org","@type":"CollectionPage","name":"خدمات قص وتشكيل وتصنيع المعادن بالليزر","url":"https://rowadlaser.com/services.html","inLanguage":"ar","isPartOf":{"@type":"WebSite","name":"رواد الليزر","url":"https://rowadlaser.com/"},"about":{"@type":"Service","name":"قص وتشكيل وتصنيع المعادن بالليزر","provider":{"@id":"https://rowadlaser.com/#business"}}}
  </script>"""

PAGE = {
    "slug": "services",
    "is_hub": True,
    "crumb": ("خدماتنا", "Services"),
    "title": (
        "خدمات قص وتشكيل وتصنيع المعادن بالليزر في جدة | رواد الليزر",
        "Laser Metal Cutting, Forming &amp; Fabrication Services in Jeddah | Ruwwad Laser",
    ),
    "desc": (
        "كل خدمات رواد الليزر في صفحة واحدة: قص المعادن بالليزر، تشكيل وثني، تصنيع ستانلس ستيل، حفر ونحت، حلول مخصصة، مشاريع كميات، وتشطيب وفحص جودة في جدة.",
        "Every Ruwwad Laser service in one place: laser metal cutting, bending and forming, stainless fabrication, engraving, custom solutions, bulk projects, finishing and QC in Jeddah.",
    ),
    "og_image": "assets/img/svc/laser-cut-metal-parts-poster.jpg",
    "service_type": ("قص وتشكيل وتصنيع المعادن بالليزر", "Laser metal cutting, forming and fabrication"),
    "schema_name": ("خدمات قص وتشكيل وتصنيع المعادن بالليزر في جدة", "Laser metal cutting, forming and fabrication services in Jeddah"),
    "schema_desc": (
        "مجموعة خدمات رواد الليزر في جدة: قص المعادن بالليزر CNC، تشكيل وثني، تصنيع الستانلس ستيل والمعادن المختلفة، الحفر والنحت بالفايبر، الحلول المخصصة، مشاريع الكميات، والتشطيب وفحص الجودة.",
        "The full Ruwwad Laser service set in Jeddah: CNC laser metal cutting, bending and forming, stainless and multi-metal fabrication, fibre engraving, custom solutions, bulk projects, and finishing with quality control.",
    ),
    "schema_offers": [(ar, en) for slug, ar, en in SERVICES],
    "schema_extra": [ITEM_LIST, WEBPAGE],
    "hero": {
        "eyebrow": ("خدماتنا · 8 خدمات مستقلة", "Our services · 8 dedicated services"),
        "h1": ("خدمات تصنيع المعادن بالليزر في جدة", "Laser metal fabrication services in Jeddah"),
        "sub": (
            "نغطّي دورة تصنيع المعدن كاملة — من القص الدقيق إلى القطعة الجاهزة للتركيب. لكل خدمة صفحة مستقلة تشرح تفاصيلها والمعادن المناسبة لها وما تحتاجه لطلب عرض سعر، فاختر ما يخصّ مشروعك.",
            "We cover the full metal fabrication cycle — from precise cutting to an installation-ready part. Each service has its own page explaining the detail, the suitable metals, and what you need for a quote. Pick the one your project needs.",
        ),
        "chips": [
            ("دقة ±0.1 مم", "±0.1 mm accuracy", "target"),
            ("أكثر من 10 أنواع معادن", "10+ metal types", "layers"),
            ("بدء التنفيذ خلال 6 ساعات", "Production starts in 6 hours", "bolt"),
            ("فحص 100% قبل التسليم", "100% inspection before delivery", "shield"),
        ],
        "img": (
            "assets/img/svc/laser-cut-metal-parts-poster.jpg",
            (
                "قطع معدنية مقصوصة بالليزر تعرض خدمات رواد الليزر في جدة",
                "Laser-cut metal parts representing Ruwwad Laser services in Jeddah",
            ),
            991,
            1400,
        ),
        "wa": "مرحباً رواد الليزر، أرغب في معرفة الخدمة المناسبة لطلبي.",
    },
    "facts": [
        (("8", "8"), ("خدمات رئيسية مستقلة", "Dedicated main services")),
        (("+10", "+10"), ("أنواع معادن نعمل عليها", "Metal types we work with")),
        (("6h", "6h"), ("لبدء التنفيذ بعد الاعتماد", "To start production")),
        (("1", "1"), ("قطعة واحدة طلب مقبول", "One piece is a valid order")),
    ],
    "intro": {
        "h2": ("كيف تختار الخدمة المناسبة لطلبك؟", "How to choose the right service for your request"),
        "paras": [
            (
                "معظم الطلبات التي تصلنا تحتاج أكثر من خدمة واحدة: لوح يُقصّ، ثم يُثنى، ثم يُلحم، ثم يُلمّع. لكن نقطة البداية تختلف من عميل لآخر — بعضهم يعرف تماماً ما يريد وبعضهم يعرف المشكلة فقط. لهذا فصلنا كل خدمة في صفحة مستقلة، حتى تقرأ ما يخصّك أنت لا كل شيء.",
                "Most requests we receive need more than one service: a sheet gets cut, then bent, then welded, then polished. But the starting point differs from customer to customer — some know exactly what they want, others only know the problem. That is why each service has its own page, so you read what concerns you rather than everything.",
            ),
            (
                "إن كان لديك ملف أو مخطط جاهز، ابدأ من صفحة قص المعادن بالليزر. وإن كان لديك مساحة أو وحدة تحتاج تصنيعاً كاملاً، ابدأ من تصنيع الستانلس أو تصنيع المعادن. وإن كان لديك فكرة أو قطعة تالفة أو طلب غير معتاد، ابدأ من الحلول المخصصة. وإن كنت مقاولاً بقائمة قطع، ابدأ من صفحة مشاريع الكميات.",
                "If you have a file or a drawing ready, start from the laser cutting page. If you have a space or a unit needing full fabrication, start from stainless or multi-metal fabrication. If you have an idea, a broken part or an unusual request, start from custom solutions. And if you are a contractor with a parts list, start from the bulk projects page.",
            ),
            (
                "وإن لم تكن متأكداً أبداً، راسلنا على واتساب بوصف بسيط لما تحتاجه — نحدّد لك الخدمة المناسبة ونجيبك بسعر ومدة، دون أن تحتاج معرفة تقنية مسبقة.",
                "And if you are not sure at all, message us on WhatsApp with a simple description of what you need — we will identify the right service and come back with a price and a timeframe, with no technical knowledge required from you.",
            ),
        ],
    },
    "cards": {
        "eyebrow": ("الخدمات الرئيسية", "Main services"),
        "h2": ("ثماني خدمات، لكل واحدة صفحتها", "Eight services, each with its own page"),
        "lead": (
            "اضغط على أي خدمة لتقرأ تفاصيلها الكاملة: المعادن المناسبة، مراحل التنفيذ، وما نحتاجه لعرض السعر.",
            "Open any service to read its full detail: suitable metals, production stages, and what we need to quote.",
        ),
        "items": [
            {
                "icon": "cut",
                "href": "laser-metal-cutting.html",
                "more": ("تفاصيل قص المعادن بالليزر", "Laser cutting details"),
                "h3": ("قص المعادن بالليزر", "Laser metal cutting"),
                "p": (
                    "قص الصفائح بدقة ±0.1 مم بحواف نظيفة وتفاصيل معقدة، على الستانلس والحديد والألمنيوم والنحاس والمجلفن.",
                    "Sheet cutting to ±0.1 mm with clean edges and intricate detail, on stainless, steel, aluminium, copper and galvanised sheet.",
                ),
            },
            {
                "icon": "bend",
                "href": "metal-bending-forming.html",
                "more": ("تفاصيل التشكيل والثني", "Bending and forming details"),
                "h3": ("تشكيل وثني المعادن", "Metal bending and forming"),
                "p": (
                    "ثني الصفائح بزوايا مضبوطة وحساب بدلات الثني قبل القص، لإنتاج صناديق وأغلفة وهياكل جاهزة للتركيب.",
                    "Bending sheet at exact angles with bend allowances calculated before cutting, producing boxes, enclosures and install-ready frames.",
                ),
            },
            {
                "icon": "cube",
                "href": "stainless-steel-fabrication.html",
                "more": ("تفاصيل تصنيع الستانلس", "Stainless fabrication details"),
                "h3": ("تصنيع الستانلس ستيل", "Stainless steel fabrication"),
                "p": (
                    "وحدات كاملة من الستانلس: طاولات وأرفف وأحواض وواجهات، بلحام مصقول وتشطيب يقاوم الصدأ والاستخدام الشاق.",
                    "Complete stainless units — tables, shelving, sinks and façade elements — with polished welds and a finish that resists rust and heavy use.",
                ),
            },
            {
                "icon": "layers",
                "href": "metal-fabrication.html",
                "more": ("تفاصيل تصنيع المعادن", "Metal fabrication details"),
                "h3": ("تصنيع المعادن المختلفة", "Multi-metal fabrication"),
                "p": (
                    "أكثر من عشرة معادن: حديد وألمنيوم ونحاس وبراص ومجلفن — ونرشّح لك المعدن الأنسب لأداء مشروعك وميزانيته.",
                    "More than ten metals — steel, aluminium, copper, brass and galvanised — with a recommendation for the metal that fits your performance and budget.",
                ),
            },
            {
                "icon": "engrave",
                "href": "fiber-marking.html",
                "more": ("تفاصيل الفايبر ماركينق", "Fibre marking details"),
                "h3": ("الحفر والنحت على المعادن", "Metal engraving and fibre marking"),
                "p": (
                    "نقش دائم لا يبهت: أسماء وشعارات وأرقام تسلسلية وأكواد QR على اللوحات واللافتات والهدايا والقطع الصناعية.",
                    "Permanent, fade-free marking: names, logos, serial numbers and QR codes on plates, signage, gifts and industrial parts.",
                ),
            },
            {
                "icon": "sliders",
                "href": "custom-metal-solutions.html",
                "more": ("تفاصيل الحلول المخصصة", "Custom solutions details"),
                "h3": ("الحلول المخصصة حسب الطلب", "Custom-made solutions"),
                "p": (
                    "قطعة واحدة أو فكرة على ورقة أو قطعة قديمة توقّف إنتاجها — نحوّلها إلى منتج معدني يعمل، بلا حد أدنى للكمية.",
                    "A single piece, an idea on paper, or a discontinued part — turned into a working metal product, with no minimum order.",
                ),
            },
            {
                "icon": "factory",
                "href": "contracting-metal-projects.html",
                "more": ("تفاصيل مشاريع الكميات", "Bulk projects details"),
                "h3": ("مشاريع المقاولات والكميات", "Contracting and bulk projects"),
                "p": (
                    "قائمة قطع بسعر لكل بند، تسليم على مراحل مربوط بجدول مشروعك، وثبات المواصفة بين الدفعة الأولى والأخيرة.",
                    "A parts list priced per item, phased delivery tied to your project schedule, and spec consistency from the first batch to the last.",
                ),
            },
            {
                "icon": "shield",
                "href": "metal-finishing-quality.html",
                "more": ("تفاصيل التشطيب والجودة", "Finishing and QC details"),
                "h3": ("التشطيب وفحص الجودة", "Finishing and quality control"),
                "p": (
                    "إزالة حواف، تلميع، تنظيف لحام، ومطابقة قياسات قبل التسليم — كمرحلة أخيرة في التصنيع أو كخدمة مستقلة.",
                    "Deburring, polishing, weld cleaning and dimensional checks before delivery — as the final fabrication stage or a standalone service.",
                ),
            },
        ],
    },
    "gallery": {
        "soft": True,
        "eyebrow": ("نماذج بصرية", "Visual samples"),
        "h2": ("أشكال من أعمال المعادن التي ننفّذها", "Forms of the metal work we produce"),
        "items": [
            (
                "assets/img/svc/laser-cutting-machine-wide.jpg",
                ("ماكينة قص المعادن بالليزر أثناء قص صفيحة معدنية", "A laser metal cutting machine cutting a sheet"),
                ("قص بالليزر", "Laser cutting"),
                1400,
                1120,
            ),
            (
                "assets/img/lp/forming-closeup.jpg",
                ("ثني صفيحة معدنية بزاوية مضبوطة على مكبس ثني", "Sheet metal bent at an exact angle on a press brake"),
                ("تشكيل وثني", "Bending"),
                1100,
                1375,
            ),
            (
                "assets/img/svc/stainless-restaurant-kitchen.jpg",
                ("تجهيزات مطبخ تجاري من الستانلس ستيل", "Commercial kitchen fittings in stainless steel"),
                ("تصنيع ستانلس", "Stainless fabrication"),
                1050,
                1400,
            ),
            (
                "assets/img/svc/industrial-laser-engraving-wide.jpg",
                ("حفر ونقش صناعي على لوحات معدنية بالفايبر ليزر", "Industrial fibre-laser engraving on metal plates"),
                ("حفر ونحت", "Engraving"),
                1400,
                933,
            ),
            (
                "assets/img/svc/custom-metal-solutions-range.jpg",
                ("مجموعة حلول معدنية مخصصة مصنّعة حسب الطلب", "A range of custom-made metal solutions"),
                ("حلول مخصصة", "Custom solutions"),
                1050,
                1400,
            ),
            (
                "assets/img/svc/metal-fabrication-workshop.jpg",
                ("ورشة تصنيع معادن مهيّأة لمشاريع الكميات", "A metal fabrication workshop set up for bulk projects"),
                ("مشاريع كميات", "Bulk projects"),
                1400,
                933,
            ),
            (
                "assets/img/svc/metal-storefront-facade.jpg",
                ("واجهة محل بشعار معدني مقصوص بالليزر", "A storefront with a laser-cut metal logo"),
                ("واجهات ولافتات", "Façades and signage"),
                1050,
                1400,
            ),
            (
                "assets/img/gallery/facade-decor.jpg",
                ("زخارف معمارية معدنية مفرّغة بالليزر", "Laser-cut architectural metal screens"),
                ("زخارف معمارية", "Architectural décor"),
                1400,
                933,
            ),
            (
                "assets/img/svc/finished-metal-parts-store.jpg",
                ("قطع معدنية جاهزة بعد التشطيب وفحص الجودة", "Finished metal parts after finishing and quality control"),
                ("تشطيب وجودة", "Finishing and QC"),
                1120,
                1400,
            ),
        ],
        "note": (
            "الصور نماذج وتصورات بصرية توضح إمكانيات الخدمات وتطبيقاتها المختلفة.",
            "Images are visual samples illustrating the services and their applications.",
        ),
    },
    "cards2": {
        "eyebrow": ("صفحات متخصصة", "Specialised pages"),
        "h2": ("صفحات أعمق لطلبات محددة", "Deeper pages for specific requests"),
        "lead": (
            "إن كان طلبك محدداً بمعدن معيّن أو تطبيق معيّن، ابدأ من صفحته المتخصصة مباشرة.",
            "If your request is specific to a metal or an application, start from its dedicated page.",
        ),
        "items": [
            {
                "icon": "cut",
                "href": "stainless-steel-laser-cutting.html",
                "more": ("قص الستانلس بالليزر", "Stainless laser cutting"),
                "h3": ("قص الستانلس ستيل بالليزر", "Stainless steel laser cutting"),
                "p": (
                    "درجات 304 و316 و430، وحافة نظيفة بلا تأكسد للأعمال الظاهرة والغذائية.",
                    "Grades 304, 316 and 430 with a clean, oxide-free edge for visible and food-related work.",
                ),
            },
            {
                "icon": "cut",
                "href": "steel-laser-cutting.html",
                "more": ("قص الحديد بالليزر", "Steel laser cutting"),
                "h3": ("قص الحديد بالليزر", "Steel laser cutting"),
                "p": (
                    "الأوفر سعراً للهياكل والقواعد والقطع الإنشائية، مع خطة حماية من الصدأ.",
                    "The best value for frames, base plates and structural parts, with a rust-protection plan.",
                ),
            },
            {
                "icon": "bolt",
                "href": "aluminum-laser-cutting.html",
                "more": ("قص الألمنيوم بالليزر", "Aluminium laser cutting"),
                "h3": ("قص الألمنيوم بالليزر", "Aluminium laser cutting"),
                "p": (
                    "ثلث وزن الحديد ولا يصدأ — للافتات والأغطية والقطع خفيفة الوزن.",
                    "A third of steel’s weight and rust-free — for signage, covers and lightweight parts.",
                ),
            },
            {
                "icon": "target",
                "href": "copper-brass-laser-cutting.html",
                "more": ("قص النحاس والبراص", "Copper and brass cutting"),
                "h3": ("قص النحاس والبراص بالليزر", "Copper and brass laser cutting"),
                "p": (
                    "معادن عاكسة ترفضها ورش كثيرة — نقصّها للديكور الفاخر والقطع الموصّلة.",
                    "Reflective metals many workshops refuse — cut here for premium décor and conductive parts.",
                ),
            },
            {
                "icon": "shield",
                "href": "galvanized-steel-laser-cutting.html",
                "more": ("قص الصفائح المجلفنة", "Galvanised sheet cutting"),
                "h3": ("قص الصفائح المجلفنة بالليزر", "Galvanised sheet laser cutting"),
                "p": (
                    "حماية زنك بميزانية معقولة — لأعمال التكييف والدكتات والأسقف.",
                    "Zinc protection at a sensible budget — for HVAC, ducting and roofing work.",
                ),
            },
            {
                "icon": "store",
                "href": "metal-facades-signage.html",
                "more": ("واجهات ولافتات معدنية", "Façades and signage"),
                "h3": ("واجهات المحلات واللافتات", "Storefronts and metal signage"),
                "p": (
                    "حروف بارزة وشعارات ولوحات بمعدن وتشطيب يتحمّلان شمس جدة ورطوبتها.",
                    "Raised letters, logos and panels in a metal and finish that survive Jeddah’s sun and humidity.",
                ),
            },
            {
                "icon": "cube",
                "href": "restaurant-kitchen-equipment.html",
                "more": ("تجهيزات المطاعم والمطابخ", "Restaurant and kitchen fittings"),
                "h3": ("تجهيزات المطاعم والمطابخ", "Restaurant and kitchen fittings"),
                "p": (
                    "طاولات وأرفف وأحواض ستانلس بمقاسات مطبخك وتفاصيل تسهّل التنظيف اليومي.",
                    "Stainless tables, shelving and sinks at your kitchen’s dimensions with details that ease daily cleaning.",
                ),
            },
            {
                "icon": "factory",
                "href": "industrial-parts-manufacturing.html",
                "more": ("القطع الصناعية وقطع الغيار", "Industrial parts and spares"),
                "h3": ("القطع الصناعية وقطع الغيار", "Industrial parts and spares"),
                "p": (
                    "قطع بديلة من رسمك أو من القطعة التالفة، بمواقع فتحات مضبوطة لتعمل من المرة الأولى.",
                    "Replacements from your drawing or the failed part, with exact hole positions so they work first time.",
                ),
            },
            {
                "icon": "build",
                "href": "architectural-metal-decor.html",
                "more": ("الزخارف المعمارية المعدنية", "Architectural metal décor"),
                "h3": ("الزخارف والمشربيات المعدنية", "Architectural screens and mashrabiya"),
                "p": (
                    "أنماط إسلامية وهندسية مفرّغة للفواصل والتظليل والأسقف، بمقاسات المشروع.",
                    "Islamic and geometric cut-out patterns for dividers, shading and ceilings at project dimensions.",
                ),
            },
        ],
    },
    "sectors": {
        "eyebrow": ("القطاعات", "Sectors"),
        "h2": ("شريك موثوق لكل قطاع", "A trusted partner for every sector"),
        "items": [
            {
                "icon": "factory",
                "h3": ("الصناعي", "Industrial"),
                "p": (
                    "قطع غيار، هياكل، ولوازم خطوط الإنتاج للمصانع والورش.",
                    "Spares, frames and production-line components for factories and workshops.",
                ),
            },
            {
                "icon": "store",
                "h3": ("التجاري", "Commercial"),
                "p": (
                    "واجهات، لافتات، ديكورات معدنية، وتجهيزات المحلات والمطاعم.",
                    "Façades, signage, decorative metal, and shop and restaurant fittings.",
                ),
            },
            {
                "icon": "build",
                "h3": ("الإنشائي", "Construction"),
                "p": (
                    "عناصر إنشائية ومعمارية للمقاولين والمشاريع العقارية.",
                    "Structural and architectural elements for contractors and property projects.",
                ),
            },
            {
                "icon": "user",
                "h3": ("الأفراد", "Individuals"),
                "p": (
                    "الطلبات الخاصة والقطعة الواحدة — لوحة، هدية، أو تصميم خاص.",
                    "Custom and one-off requests — a plate, a gift, or a special design.",
                ),
            },
        ],
    },
    "process": {
        "soft": True,
        "eyebrow": ("كيف تطلب", "How to order"),
        "h2": ("من الطلب إلى التسليم في أربع خطوات", "From request to delivery in four steps"),
        "steps": [
            {
                "h3": ("أرسل طلبك", "Send your request"),
                "p": (
                    "عبر واتساب أو النموذج: مخطط أو رسم أو صورة مع القياسات ونوع المعدن والكمية — ونساعدك إن لم يكن المخطط جاهزاً.",
                    "By WhatsApp or the form: a drawing, sketch or photo with dimensions, metal type and quantity — and we help if the drawing is not ready.",
                ),
            },
            {
                "h3": ("عرض سعر سريع", "A fast quote"),
                "p": (
                    "سعر واضح وجدول تنفيذ محدد، بدون أي التزام من جانبك — ونشير إلى أي تعديل يوفّر عليك تكلفة.",
                    "A clear price and a defined schedule with no obligation — and we flag any change that would save you money.",
                ),
            },
            {
                "h3": ("التصنيع والتنفيذ", "Production"),
                "p": (
                    "نبدأ عادةً خلال 6 ساعات من اعتماد الطلب، مع متابعة الجودة بين المراحل لا في النهاية فقط.",
                    "We usually start within 6 hours of approval, with quality checks between stages rather than only at the end.",
                ),
            },
            {
                "h3": ("الفحص والتسليم", "Inspection and delivery"),
                "p": (
                    "فحص القياسات والحواف قبل التسليم، وتسليم في الموعد المتفق عليه.",
                    "Dimensional and edge checks before delivery, handed over on the agreed date.",
                ),
            },
        ],
        "need": {
            "h3": ("ما نحتاجه منك لعرض السعر", "What we need for a quote"),
            "items": [
                (
                    "المخطط أو الرسم — أو صورة واضحة مع القياسات.",
                    "The drawing or sketch — or a clear photo with dimensions.",
                ),
                (
                    "نوع المعدن والسماكة — وإن لم تكن متأكداً نرشدك للأنسب.",
                    "Metal type and thickness — and if you are unsure, we will advise.",
                ),
                (
                    "الكمية المطلوبة — من قطعة واحدة إلى كميات المشاريع.",
                    "The quantity — from a single piece to project volumes.",
                ),
                (
                    "الموعد المطلوب — لنرتّب جدول التنفيذ على أساسه.",
                    "The date you need it — so we can plan the schedule around it.",
                ),
            ],
        },
    },
    "why": {
        "eyebrow": ("لماذا رواد الليزر", "Why Ruwwad Laser"),
        "h2": ("جهة واحدة تعتمد عليها في كل ما يتعلق بالمعادن", "One partner for everything metal"),
        "items": [
            {
                "icon": "bolt",
                "h3": ("السرعة", "Speed"),
                "p": (
                    "رد سريع على الاستفسار، عرض سعر سريع، والتزام حقيقي بالموعد.",
                    "A quick reply, a fast quote, and dates we actually keep.",
                ),
            },
            {
                "icon": "sliders",
                "h3": ("المرونة", "Flexibility"),
                "p": (
                    "نقبل الطلبات الصغيرة وغير المعتادة التي ترفضها ورش أخرى — حتى القطعة الواحدة.",
                    "We accept the small, unusual orders other workshops turn down — down to a single piece.",
                ),
            },
            {
                "icon": "target",
                "h3": ("الدقة", "Precision"),
                "p": (
                    "تنفيذ مطابق للمخطط، حواف نظيفة، وقياسات مضبوطة.",
                    "Built to the drawing — clean edges and exact dimensions.",
                ),
            },
            {
                "icon": "shield",
                "h3": ("الثقة والمتابعة", "Trust and follow-up"),
                "p": (
                    "شفافية في السعر ومتابعة شخصية لطلبك من أول رسالة حتى التسليم.",
                    "Transparent pricing and personal follow-up from the first message to delivery.",
                ),
            },
        ],
    },
    "related": {
        "eyebrow": ("صفحات محلية", "Local pages"),
        "h2": ("خدماتنا حسب المدينة", "Our services by city"),
        "lead": (
            "نخدم جدة ومنطقة مكة المكرمة، ولكل منطقة صفحة توضح الخدمات المتاحة فيها.",
            "We serve Jeddah and the Makkah region, and each area has a page outlining the services available.",
        ),
        "items": [
            {
                "icon": "pin",
                "href": "laser-jeddah.html",
                "h3": ("قص الليزر في جدة", "Laser cutting in Jeddah"),
                "p": (
                    "نطاق خدمتنا الأساسي: قص وتصنيع المعادن لعملاء جدة وأحيائها.",
                    "Our core service area: metal cutting and fabrication for customers across Jeddah.",
                ),
            },
            {
                "icon": "pin",
                "href": "laser-makkah.html",
                "h3": ("خدماتنا في مكة المكرمة", "Our services in Makkah"),
                "p": (
                    "خدمات القص والتصنيع والحفر لعملاء مكة المكرمة ومحيطها.",
                    "Cutting, fabrication and engraving services for customers in Makkah and its surroundings.",
                ),
            },
            {
                "icon": "file",
                "href": "laser-cutting-services.html",
                "h3": ("نظرة عامة على خدمات القص", "Cutting services overview"),
                "p": (
                    "صفحة عامة تجمع خدمات القص والتصنيع مع ملف الشركة التعريفي للتحميل.",
                    "A general page combining cutting and fabrication services with the downloadable company profile.",
                ),
            },
        ],
    },
    "faq": [
        {
            "q": ("ما الخدمة التي أحتاجها إن كان لدي مخطط جاهز فقط؟", "Which service do I need if I only have a drawing?"),
            "a": (
                "ابدأ من صفحة قص المعادن بالليزر. أرسل ملف DXF أو DWG أو PDF ونراجعه فنياً ونسعّره. وإن كان تصميمك يحتاج ثنياً أو لحاماً بعد القص، سنشير إلى ذلك في العرض ونضمّن المراحل كلها في سعر واحد.",
                "Start from the laser metal cutting page. Send a DXF, DWG or PDF and we will review it technically and price it. If your design needs bending or welding after cutting, we will flag that in the quote and include all stages in one price.",
            ),
        },
        {
            "q": ("هل يمكن طلب أكثر من خدمة في طلب واحد؟", "Can I order more than one service in a single request?"),
            "a": (
                "نعم، وهذا هو الأغلب. القص والثني واللحام والتشطيب تُنفَّذ في مسار واحد بعرض سعر واحد ومسؤولية واحدة، فلا تحتاج التنسيق بين موردين ولا تحمل مسؤولية الفرق بينهم.",
                "Yes, and that is the norm. Cutting, bending, welding and finishing run in one flow with one quote and one point of accountability, so you do not coordinate suppliers or carry the risk of the gaps between them.",
            ),
        },
        {
            "q": ("هل تقبلون الطلبات الصغيرة أو القطعة الواحدة؟", "Do you accept small or single-piece orders?"),
            "a": (
                "نعم، ولا يوجد حد أدنى للكمية. من أهم ما يميّزنا مرونتنا في قبول الطلبات الصغيرة وغير المعتادة التي قد ترفضها ورش أخرى — وتُعامل بنفس دقة الطلبات الكبيرة.",
                "Yes, with no minimum quantity. One of our key advantages is accepting small and unusual orders other workshops may refuse — treated with the same accuracy as large ones.",
            ),
        },
        {
            "q": ("كم تستغرق تنفيذ الطلبات؟", "How long do orders take?"),
            "a": (
                "تعتمد المدة على حجم الطلب وتعقيده وعدد المراحل، لكننا نرسل جدولاً واضحاً مع عرض السعر ونبدأ التنفيذ عادةً خلال 6 ساعات من اعتماد الطلب. ولا نعطي موعداً متفائلاً لا نستطيع الوفاء به.",
                "It depends on the order’s size, complexity and number of stages, but we send a clear schedule with the quote and usually start production within 6 hours of approval. We do not give optimistic dates we cannot keep.",
            ),
        },
        {
            "q": ("هل تخدمون خارج مدينة جدة؟", "Do you serve outside Jeddah?"),
            "a": (
                "نخدم جدة ومنطقة مكة المكرمة بشكل أساسي بما فيها مكة المكرمة، ويمكن التنسيق لمشاريع خارج المنطقة حسب حجم الطلب. راسلنا وسنوضّح لك الخيارات المتاحة بصراحة.",
                "We primarily serve Jeddah and the Makkah region, including Makkah itself, and can coordinate projects outside the region depending on order size. Message us and we will explain the options plainly.",
            ),
        },
        {
            "q": ("ما الملفات التي تقبلونها؟", "Which file formats do you accept?"),
            "a": (
                "DXF و DWG و PDF هي الأفضل للقص. ونقبل أيضاً صور PNG أو JPG عالية الدقة والرسومات اليدوية الواضحة مع القياسات، ونتولّى تحويلها إلى ملف قابل للتنفيذ قبل البدء.",
                "DXF, DWG and PDF are best for cutting. We also accept high-resolution PNG or JPG images and clear hand sketches with dimensions, and convert them into a producible file before starting.",
            ),
        },
    ],
    "form_services": [
        ("قص المعادن بالليزر", "Laser metal cutting"),
        ("تشكيل وثني المعادن", "Metal bending and forming"),
        ("تصنيع الستانلس ستيل", "Stainless steel fabrication"),
        ("تصنيع المعادن المختلفة", "Multi-metal fabrication"),
        ("الحفر والنحت بالفايبر ليزر", "Fibre laser engraving"),
        ("حلول مخصصة حسب الطلب", "Custom-made solutions"),
        ("مشاريع مقاولات وكميات", "Contracting and bulk projects"),
        ("تشطيب وفحص جودة", "Finishing and quality control"),
        ("أخرى / غير متأكد", "Other / not sure"),
    ],
    "form_wa": "مرحباً رواد الليزر، أرغب في طلب عرض سعر.",
    "quote_h2": ("أرسل تفاصيل طلبك الآن", "Send your request now"),
    "cta": {
        "h2": ("حدّثنا عن مشروعك", "Tell us about your project"),
        "p": (
            "مهما كان طلبك، لدينا الخدمة المناسبة له. احصل على عرض سعر سريع اليوم — بدون أي التزام.",
            "Whatever your request, we have the right service for it. Get a fast quote today — with no obligation.",
        ),
        "wa": "مرحباً رواد الليزر، أرغب في طلب عرض سعر.",
    },
}
