# -*- coding: utf-8 -*-
"""أجزاء مشتركة لصفحات الحفر على المواد واللوحات والتاقات (أُضيفت 2026-10-11)
الملف يبدأ بـ _ لذلك لا يبنيه build.py كصفحة."""

ENG_PARENT = {"slug": "laser-engraving-jeddah", "name": ("الحفر والنقش بالليزر", "Laser engraving")}
TAGS_PARENT = {"slug": "industrial-labels-tags", "name": ("اللوحات والتاقات التعريفية", "Labels, plates &amp; tags")}

# مقاسات الصور الموجودة في assets/img/svc
_SIZES = {
    "engraving-four-metals-test": (1400, 764),
    "laser-engraving-metals-range": (1400, 1050),
    "engraved-brass-plate": (992, 1057),
    "engraved-part-number-plate": (992, 1057),
    "engraved-qr-equipment-id": (992, 1057),
    "engraving-contrast-range": (1312, 1199),
    "engraved-hand-tool": (992, 1057),
    "engraved-calibration-scale": (992, 1057),
    "engraved-rotor-disc": (992, 1057),
    "fiber-marking-plates-wide": (1400, 933),
    "engraving-line-detail-test": (1400, 1050),
    "engraving-power-test-grid": (1400, 1050),
    "dataplate-before-after-engraving": (1050, 1400),
}


def ill(name):
    return f"assets/img/svc/ill-{name}.jpg"


def hero_img(name, alt):
    return (ill(name), alt, 1400, 1050)


def g(name, alt, label):
    """عنصر معرض: صورة توضيحية مرسومة (ill-*) أو صورة قائمة"""
    if name.startswith("ill-"):
        return (f"assets/img/svc/{name}.jpg", alt, label, 1400, 1050)
    w, h = _SIZES[name]
    return (f"assets/img/svc/{name}.jpg", alt, label, w, h)


GALLERY_NOTE = (
    "الصور رسومات ونماذج توضيحية لإمكانيات الخدمة، وليست أعمالاً منفّذة لعملاء.",
    "Images are illustrations and visual samples of the service, not delivered client work.",
)


def process(h2=("كيف يتم طلبك؟", "How your order works")):
    return {
        "soft": True,
        "eyebrow": ("خطوات واضحة", "Clear steps"),
        "h2": h2,
        "steps": [
            {
                "h3": ("أرسل التصميم أو القائمة", "Send the design or the list"),
                "p": (
                    "ملف شعار، صورة، أو حتى قائمة نصوص في إكسل — مع المقاس والكمية ومكان الاستخدام.",
                    "A logo file, a photo, or just a list of texts in Excel — with size, quantity and where it will be used.",
                ),
            },
            {
                "h3": ("معاينة وعرض سعر", "Proof and quote"),
                "p": (
                    "نرسل لك معاينة رقمية بالشكل النهائي وسعراً واضحاً قبل أي تنفيذ.",
                    "We send a digital proof of the final look and a clear price before any production.",
                ),
            },
            {
                "h3": ("التنفيذ", "Production"),
                "p": (
                    "يبدأ التنفيذ خلال 6 ساعات من اعتماد المعاينة، مع عيّنة أولى للكميات الكبيرة.",
                    "Production starts within 6 hours of proof approval, with a first sample for large batches.",
                ),
            },
            {
                "h3": ("فحص وتسليم", "Inspection and delivery"),
                "p": (
                    "فحص 100% للنصوص والأرقام قبل التسليم، مرتّبة ومرقّمة حسب قائمتك.",
                    "100% check of every text and number before delivery, sorted and numbered to your list.",
                ),
            },
        ],
    }


def why():
    return {
        "eyebrow": ("لماذا رواد الليزر", "Why Ruwwad Laser"),
        "h2": ("طلب واحد، جهة واحدة مسؤولة", "One order, one accountable partner"),
        "items": [
            {
                "icon": "file",
                "h3": ("ترقيم من ملف إكسل", "Numbering straight from Excel"),
                "p": ("أرسل قائمتك، ونحفر كل رقم وحرف مرتّباً كما في جدولك.", "Send your list and we engrave every number and letter, sorted exactly as in your sheet."),
            },
            {
                "icon": "bolt",
                "h3": ("بدء خلال 6 ساعات", "Start within 6 hours"),
                "p": ("من اعتماد المعاينة إلى بدء التنفيذ.", "From proof approval to production start."),
            },
            {
                "icon": "layers",
                "h3": ("كل المواد تحت سقف واحد", "Every material under one roof"),
                "p": (
                    "معادن، ترافوليت، أكريليك، ABS — لا تحتاج تتنقّل بين الورش.",
                    "Metals, Traffolyte, acrylic, ABS — no need to go from workshop to workshop.",
                ),
            },
            {
                "icon": "shield",
                "h3": ("فحص 100% قبل التسليم", "100% checked before delivery"),
                "p": ("كل رقم وكل حرف يُراجع مقابل قائمتك.", "Every number and letter is checked against your list."),
            },
        ],
    }
