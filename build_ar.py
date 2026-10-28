# -*- coding: utf-8 -*-
"""Собирает /ar/index.html из index.html: перевод + RTL.
Запуск: python3 build_ar.py   (из папки wheel-zone)"""
import os, re, io

SRC = "index.html"
OUT = os.path.join("ar", "index.html")

html = io.open(SRC, encoding="utf-8").read()

# ---------- 1. голова ----------
html = html.replace('<html lang="en">', '<html lang="ar" dir="rtl">')
html = html.replace(
  'family=Archivo:wdth,wght@75..125,400..900&family=JetBrains+Mono:wght@400;700',
  'family=Archivo:wdth,wght@75..125,400..900&family=Cairo:wght@400;600;700;900&family=JetBrains+Mono:wght@400;700')
html = html.replace('<link rel="canonical" href="https://tirez.ae/">',
                    '<link rel="canonical" href="https://tirez.ae/ar/">')
html = html.replace('href="img/', 'href="../img/').replace('src="img/', 'src="../img/')
html = html.replace('srcset="img/', 'srcset="../img/')
assert 'srcset="../img/logo-mark' in html, "знак в шапке не перепривязан"

# ---------- 1a. словарь терминов каталога: подставляется в L() ----------
TERMS = {
  # подписи в карточке диска
  "width": "العرض", "et": "الإزاحة", "cb": "فتحة المركز",
  "rim": "جنط", "same rim": "نفس الجنط", "overall": "القطر الكلي",
  "Fits": "يناسب", "to confirm": "يُحدَّد لاحقاً",
  # подбор по автомобилю
  "Find by vehicle": "ابحث حسب السيارة",
  "Pick your car and we show only the rims that bolt on.":
    "اختر سيارتك وسنعرض لك الجنوط التي تركّب عليها فقط.",
  "Make": "الماركة", "Model": "الموديل", "Reset": "إعادة تعيين",
  "Any make": "كل الماركات", "Any model": "كل الموديلات", "All": "الكل",
  "Bolt pattern": "نمط الصواميل", "Centre bore": "فتحة المركز",
  "Diameters we list": "المقاسات المتوفرة لدينا",
  "Nothing listed for that combination yet. Call ":
    "لا يوجد في القائمة ما يطابق هذا الاختيار بعد. اتصل على ",
  " — the list on this page is only what we have confirmed so far.":
    " — القائمة هنا تضم ما تأكّد لدينا حتى الآن فقط.",
  # шаблоны целиком — в арабском существительное перед определением
  "{d}&Prime; rim, {pcd}, fits {fits}": "جنط مقاس {d}&Prime;، {pcd}، يناسب {fits}",
  "{d}&Prime; rim, {pcd}, CB {cb} — {fits}":
    "جنط مقاس {d}&Prime;، {pcd}، فتحة المركز {cb} — {fits}",
  # тип шины
  "Passenger": "ركاب", "SUV": "دفع رباعي", "Performance": "أداء عالٍ", "4x4": "طرق وعرة",
  # единицы и кнопки
  "load": "الحمل", "mm": "ملم", "kg": "كجم", "km/h": "كم/س",
  "AED": "درهم", "Price on request": "السعر عند الطلب", "Ask us": "اسألنا",
  # услуги
  "Tyre fitting": "تركيب الإطارات", "Wheel balancing": "ترصيص العجلات",
  "Wheel alignment": "ضبط زوايا العجلات", "Puncture repair": "تصليح البنشر",
  "Nitrogen inflation": "تعبئة نيتروجين", "New valves": "صمامات جديدة",
  "Old tyre disposal": "التخلص من الإطارات القديمة", "Rim repair": "إصلاح الجنوط",
}
import json as _json
_terms_js = "var TERMS = " + _json.dumps(TERMS, ensure_ascii=False) + ";"
assert "var TERMS = window.WZ_TERMS || {};" in html, "крючок L() пропал из index.html"
html = html.replace("var TERMS = window.WZ_TERMS || {};", _terms_js)
html = html.replace('content="https://tirez.ae/img/', 'content="https://tirez.ae/img/')
html = html.replace('fetch("catalog.json?v=1")', 'fetch("../catalog.json?v=1")')
html = html.replace("""+r.img+'?v=1" alt=""", """+"../"+r.img+'?v=1" alt=""")
assert '"../"+r.img' in html, "путь к картинкам каталога не переписан"
html = html.replace('href="ar/"', 'href="../"')
html = html.replace('"url":"https://tirez.ae/"', '"url":"https://tirez.ae/ar/"')

# ---------- 2. RTL + Cairo, поверх общих токенов ----------
RTL_CSS = u"""
/* ===== AR / RTL ===== */
body,h1,h2,h3,.btn,.lead,p,li,dd,dt,label,select,option{font-family:"Cairo","Archivo",sans-serif}
h1,h2,h3{font-variation-settings:normal;letter-spacing:0;line-height:1.18}
.label{font-family:"Cairo",sans-serif;letter-spacing:0;font-weight:700}
.mono,.ticker b,.card-spec,.dec dd,.alts li,.summary,.trow .sz,.trow .mi,.info dd.mono,
.qty output,.proof .n,.gate input,.cols3 .mono,.list li .mono,.empty,.price,.ph-slot{
  font-family:"JetBrains Mono",ui-monospace,monospace;direction:ltr}
.card-spec,.dec,.alts li,.info > div{text-align:start}
.quote{border-left:0;border-right:2px solid var(--accent);padding:4px 20px 4px 0}
.notice{border-left:1px solid var(--line);border-right:2px solid var(--accent)}
.light .notice{border-left-color:#C9D3DD;border-right-color:var(--accent)}
.nav a::after{transform-origin:right}
.hero-photo img{object-position:38% 50%}
.hero-photo::after{background:linear-gradient(270deg,var(--ink) 0%,rgba(11,14,18,.95) 42%,rgba(11,14,18,.72) 100%),
  linear-gradient(0deg,var(--ink) 0%,rgba(11,14,18,.35) 34%,transparent 62%)}
.hero-wheel{right:auto;left:-8vw}
/* .gate внутри direction:ltr — там flex-end это право.
   .gate-out и .hero-cta наследуют rtl, и у них flex-end это ЛЕВО: подпись и кнопки
   уезжали на светлую половину фото и переставали читаться. Нужен flex-start. */
.gate{direction:ltr;justify-content:flex-end}
.gate-out,.hero-cta{justify-content:flex-start}
.gate-f .label{direction:rtl}
.skip:focus{left:auto;right:var(--pad)}
.alts li em,.trow .mi{direction:rtl}
.alts li span:first-child,.trow .sz{direction:ltr}
.ftr .ar{direction:rtl}
.dec dt{font-family:"Cairo",sans-serif}
"""
html = html.replace("</style>", RTL_CSS + "\n</style>")

# ---------- 3. перевод. Длинные строки первыми ----------
T = [
 # --- варианты в select: должны сработать РАНЬШЕ пунктов меню,
 #     иначе ">Tyres<" из навигации съедает ">Tyres</option>" ---
 ('>Tyres</option>', '>إطارات</option>'), ('>Rims</option>', '>جنوط</option>'),
 ('>Rims + tyres</option>', '>جنوط + إطارات</option>'), ('>Rim repair</option>', '>إصلاح جنط</option>'),
 ('value="Rims + tyres"', 'value="جنوط + إطارات"'), ('value="Rim repair"', 'value="إصلاح جنط"'),
 ('value="Tyres"', 'value="إطارات"'), ('value="Rims"', 'value="جنوط"'),

 # --- head ---
 ("Wheel Zone Tyre Trading &mdash; Rims, Tyres &amp; Rim Repair in Ras Al Khor, Dubai",
  "ويل زون لتجارة الاطارات — جنوط وإطارات وإصلاح جنوط في راس الخور، دبي"),
 ("Wheel Zone Tyre Trading — Rims, Tyres &amp; Rim Repair in Ras Al Khor, Dubai",
  "ويل زون لتجارة الاطارات — جنوط وإطارات وإصلاح جنوط في راس الخور، دبي"),
 ("Wheel Zone Tyre Trading (4X_WHEELS) — rims, tyres and rim repair on 36th Street, Ras Al Khor Industrial Area 2, Dubai. Rated 4.4 on Google. Call 04 576 2199.",
  "ويل زون لتجارة الاطارات (4X_WHEELS) — جنوط وإطارات وإصلاح جنوط في شارع 36، منطقة راس الخور الصناعية 2، دبي. تقييم 4.4 على جوجل. اتصل 04 576 2199."),
 ("Wheel Zone Tyre Trading &mdash; Rims, Tyres &amp; Rim Repair, Dubai",
  "ويل زون لتجارة الاطارات — جنوط وإطارات وإصلاح جنوط، دبي"),
 ("Wheel Zone Tyre Trading — Rims, Tyres &amp; Rim Repair, Dubai",
  "ويل زون لتجارة الاطارات — جنوط وإطارات وإصلاح جنوط، دبي"),
 ("Rims, tyres and rim repair on 36th Street, Ras Al Khor Industrial Area 2, Dubai. Rated 4.4 on Google.",
  "جنوط وإطارات وإصلاح جنوط في شارع 36، منطقة راس الخور الصناعية 2، دبي. تقييم 4.4 على جوجل."),
 ("Wheel Zone Tyre Trading logo", "شعار ويل زون لتجارة الاطارات"),
 ("Wheel Zone Tyre Trading &mdash; home", "ويل زون لتجارة الاطارات — الرئيسية"),
 ("Wheel Zone Tyre Trading — home", "ويل زون لتجارة الاطارات — الرئيسية"),

 # --- nav / CTA ---
 (">Rims<", ">الجنوط<"), (">Rim repair<", ">إصلاح الجنوط<"), (">Tyres<", ">الإطارات<"),
 (">Calculator<", ">الحاسبة<"), (">Visit us<", ">زورونا<"), (">العربية<", ">English<"),
 ("Call 04 576 2199", "اتصل 04 576 2199"),
 ('aria-label="Menu"', 'aria-label="القائمة"'),

 # --- hero ---
 ("Ras Al Khor Industrial Area 2 · Dubai", "منطقة راس الخور الصناعية 2 · دبي"),
 ("4.4 ★ · 40 reviews on Google", "4.4 ★ · 40 تقييماً على جوجل"),
 ("Tell us your size. The rest is our job.", "قل لنا المقاس. والباقي علينا."),
 ("Rims, tyres and rim repair on 36th Street. Type the numbers off your tyre wall and the catalogue below filters itself.",
  "جنوط وإطارات وإصلاح جنوط في شارع 36. اكتب الأرقام المدوّنة على جدار إطارك، وسيُرشَّح الكتالوج أدناه من تلقاء نفسه."),
 ('aria-label="Enter your tyre size"', 'aria-label="أدخل مقاس إطارك"'),
 (">Width<", ">العرض<"), (">Profile<", ">النسبة<"), (">Rim<", ">قطر الجنط<"),
 ("It is printed on the side of your tyre — for example 225/45 R18.",
  "المقاس مطبوع على جانب الإطار — مثال 225/45 R18."),
 ("See matching rims", "اعرض الجنوط المطابقة"),
 ("Open the size calculator", "افتح حاسبة المقاسات"),

 # --- proof ---
 ("Specifications and proof", "المواصفات والأرقام"),
 ("Rating on Google, collected by Google from real customers.",
  "التقييم على جوجل، جمعته جوجل من عملاء حقيقيين."),
 ("Reviews on the Google profile. We opened recently — every one of them is earned.",
  "تقييماً على صفحتنا في جوجل. افتتحنا حديثاً — وكل تقييم منها مُستحق."),
 ("We close at 23:00. Caught a kerb on the way home from work? You still have time.",
  "نغلق الساعة 23:00. اصطدم جنطك بالرصيف في طريق العودة من العمل؟ لا يزال لديك وقت."),

 # --- rims ---
 ("01 — The wall", "01 — الجدار"),
 ("Rims that fit your&nbsp;car", "جنوط تناسب سيارتك"),
 ("Our customers say it better than we could:", "عملاؤنا قالوها أفضل منا:"),
 ("“the selection of rims? Crazy good.”", "«تشكيلة الجنوط؟ رهيبة.»"),
 ("Tell us the car and we will tell you what bolts on.",
  "قل لنا نوع السيارة ونقول لك ما الذي يركّب عليها."),
 ('aria-label="Filter rims by diameter"', 'aria-label="ترشيح الجنوط حسب القطر"'),
 ("<b>These fitments are confirmed. Prices and photos are not yet.</b> Diameter, bolt pattern and centre bore below come straight from the shop. Rim width, offset and price are still being compiled, and the photographs are illustrative — call",
  "<b>بيانات التركيب هذه مؤكّدة. أما الأسعار والصور فلا.</b> القطر ونمط الصواميل وفتحة المركز أدناه واردة من المحل مباشرة. أما عرض الجنط والإزاحة والسعر فما زالت قيد التجميع، والصور توضيحية — اتصل على"),
 ("for the exact wheel and the number.", "لمعرفة الجنط المحدد والسعر."),
 # Подписи в подборе по автомобилю: их рендерит JS через L(), поэтому
 # здесь только статические метки полей
 ('<span class="label">Find by vehicle</span>', '<span class="label">ابحث حسب السيارة</span>'),
 ("Pick your car and we show only the rims that bolt on.",
  "اختر سيارتك وسنعرض لك الجنوط التي تركّب عليها فقط."),
 (">Make<", ">الماركة<"), (">Model<", ">الموديل<"), (">Reset<", ">إعادة تعيين<"),
 (">Any make<", ">كل الماركات<"), (">Any model<", ">كل الموديلات<"),
 (">Bolt pattern<", ">نمط الصواميل<"), (">Centre bore<", ">فتحة المركز<"),
 (">Diameters we list<", ">المقاسات المتوفرة لدينا<"),

 # --- repair ---
 ("02 — What the neighbours don&rsquo;t do", "02 — ما لا يفعله الجيران"),
 ("We repair the rim.<br>We don&rsquo;t just sell you a&nbsp;new&nbsp;one.",
  "نُصلح الجنط.<br>لا نبيعك جنطاً جديداً وحسب."),
 ("You drive in and we look at the wheel with you.", "تدخل بسيارتك، وننظر إلى العجلة معك."),
 ("We tell you what is actually wrong with it before anything is quoted.",
  "نخبرك بما فيها فعلاً من عيب قبل أن نذكر أي سعر."),
 ("Repair it, or fit a replacement from the wall — your call, not ours.",
  "نُصلحها، أو نركّب بديلاً من الجدار — القرار لك، لا لنا."),
 ("Find us in Ras Al Khor", "اعثر علينا في راس الخور"),
 ("A technician in gloves handling a wheel in the workshop",
  "فني يرتدي قفازات يتعامل مع عجلة داخل الورشة"),
 ("[photo: rim before repair]", "[صورة: الجنط قبل الإصلاح]"),
 ("[photo: the same rim after]", "[صورة: الجنط نفسه بعد الإصلاح]"),
 ("awaiting the shop&rsquo;s own photo", "بانتظار صورة من المحل"),

 # --- tyres ---
 ("03 — Rubber", "03 — المطاط"),
 ("Tyres, by the number on&nbsp;your&nbsp;wall", "إطارات، حسب الرقم المكتوب على جدارها"),
 ("Fitting, balancing, puncture repair and disposal of the old set — all of it happens here, in one visit.",
  "التركيب والترصيص وتصليح البنشر والتخلص من الطقم القديم — كل ذلك هنا، في زيارة واحدة."),
 ('aria-label="Filter tyres"', 'aria-label="ترشيح الإطارات"'),
 # Подписи чипов должны совпадать со словарём TERMS, иначе фильтр и карточка
 # называют одно и то же разными словами
 (">Passenger<", ">ركاب<"), (">SUV<", ">دفع رباعي<"), (">Performance<", ">أداء عالٍ<"),
 (">4&times;4<", ">طرق وعرة<"),
 ("<b>Prices are being loaded.</b> Brands and prices come straight from the shop&rsquo;s stock list. Until then every size here is quoted on request — call",
  "<b>الأسعار قيد التحميل.</b> الماركات والأسعار تأتي مباشرة من قائمة مخزون المحل. حتى ذلك الحين، كل مقاس هنا بسعر عند الطلب — اتصل على"),
 ("and you will get the number in a minute.", "وستحصل على الرقم خلال دقيقة."),

 # --- warranty ---
 ("04 — After you drive out", "04 — بعد أن تغادر"),
 ("A warranty on the part", "ضمان على القطعة"),
 (">and</em> on the work", ">و</em> على العمل"),
 ("On the product", "على المنتج"),
 ("Whatever you buy here is covered. Ask us for the exact terms on the item you are looking at — we would rather tell you than print a vague promise.",
  "كل ما تشتريه من هنا مشمول. اسألنا عن الشروط الدقيقة للقطعة التي تنظر إليها — نفضّل أن نخبرك بدل أن نطبع وعداً غامضاً."),
 ("On the workmanship", "على جودة العمل"),
 ("If something we fitted is not right, you bring it back and we deal with it. That is the half most shops leave out.",
  "إذا لم يكن ما ركّبناه سليماً، أعِده إلينا ونتكفّل به. هذا هو النصف الذي تتجاهله معظم المحلات."),
 ("On the explanation", "على الشرح"),
 ("You will be told what is wrong with the wheel and why, before any work starts. No surprises on the invoice.",
  "سنخبرك بما في العجلة من عيب ولماذا، قبل بدء أي عمل. لا مفاجآت في الفاتورة."),

 # --- calculator ---
 ("05 — The numbers", "05 — الأرقام"),
 ("Read your size, then build the&nbsp;request", "اقرأ مقاسك، ثم جهّز طلبك"),
 ("Left side is pure arithmetic and works right now. Right side turns your choice into a message we can price in one reply.",
  "الجهة الأولى حساب رياضي بحت ويعمل الآن. والثانية تحوّل اختيارك إلى رسالة نردّ عليها بالسعر مباشرة."),
 ("What your tyre size means", "ماذا يعني مقاس إطارك"),
 ("Type it as it is written on the sidewall. We decode it and work out which other sizes will fit the same wheel.",
  "اكتبه كما هو مدوّن على جدار الإطار. نفكّ رموزه ونحسب المقاسات الأخرى التي تناسب الجنط نفسه."),
 (">Tyre size<", ">مقاس الإطار<"),
 (">Section width<", ">عرض المقطع<"), (">Aspect ratio<", ">نسبة الارتفاع<"),
 (">Rim diameter<", ">قطر الجنط<"), (">Overall diameter<", ">القطر الكلي<"),
 (">Load index<", ">مؤشر الحمل<"), (">Speed rating<", ">مؤشر السرعة<"),
 ("Sizes that fit the same wheel (&plusmn;3%)", "مقاسات تناسب الجنط نفسه (‎±3%‎)"),
 ("Enter a size above and the alternatives appear here.", "أدخل مقاساً أعلاه وستظهر البدائل هنا."),
 ("Build your request", "جهّز طلبك"),
 ("Pick what you need. We put it into one message, you send it, we come back with a price.",
  "اختر ما تحتاجه. نضعه في رسالة واحدة، ترسلها، ونعود إليك بالسعر."),
 ("What are you after", "ما الذي تبحث عنه"),
 ("Size (we fill it from the box above)", "المقاس (نملؤه من الحقل أعلاه)"),
 ("How many", "الكمية"),
 ('aria-label="One fewer"', 'aria-label="واحد أقل"'),
 ('aria-label="One more"', 'aria-label="واحد أكثر"'),
 ("Add the work", "أضف الخدمات"),
 ("Send on WhatsApp", "أرسل عبر واتساب"),
 ("Copy the request", "انسخ الطلب"),
 ("Call instead", "أو اتصل بنا"),

 # --- reviews ---
 ("06 — Out loud", "06 — بصوت عالٍ"),
 ("Three people, in their own&nbsp;words", "ثلاثة أشخاص، بكلماتهم هم"),
 ("Copied from our Google profile without a single edit. We have 40 of them and a 4.4 average — we would rather show you the real three than invent thirty.",
  "منقولة من صفحتنا على جوجل دون تعديل حرف واحد. لدينا 40 تقييماً بمعدل 4.4 — ونفضّل أن نعرض عليك ثلاثة حقيقية بدل أن نختلق ثلاثين."),
 ('aria-label="5 out of 5"', 'aria-label="5 من 5"'),
 ("Local Guide · 330 reviews · a year ago", "مرشد محلي · 330 تقييماً · قبل سنة"),
 ("8 reviews · a year ago", "8 تقييمات · قبل سنة"),
 ("Local Guide · 59 reviews · a year ago", "مرشد محلي · 59 تقييماً · قبل سنة"),

 # --- visit ---
 ("07 — Come in", "07 — تفضّل بالزيارة"),
 ("36th Street, Ras Al&nbsp;Khor", "شارع 36، راس الخور"),
 ("Industrial Area 2. Plus code", "المنطقة الصناعية 2. رمز Plus"),
 ("drops you at the door.", "يوصلك إلى الباب مباشرة."),
 (">Address<", ">العنوان<"), (">Phone<", ">الهاتف<"), (">Plus code<", ">رمز Plus<"),
 (">Closing time<", ">وقت الإغلاق<"), (">Google<", ">جوجل<"), (">Arabic name<", ">الاسم بالعربية<"),
 ("4.4 ★ from 40 reviews", "4.4 ★ من 40 تقييماً"),
 ("Wheel Zone Tyre Trading on the map", "ويل زون لتجارة الاطارات على الخريطة"),

 # --- footer / bar ---
 ("Get in touch", "تواصل معنا"),
 ("النسخة العربية", "English version"),
 ("Rating and reviews are shown as collected by Google.",
  "التقييم والمراجعات معروضة كما جمعتها جوجل."),
 ('aria-label="Quick contact"', 'aria-label="تواصل سريع"'),
 (">Call us<", ">اتصل بنا<"), (">Get a price<", ">اطلب السعر<"),

 # --- строки внутри JS ---
 # цена, единицы, «Ask us», стили дисков и услуги идут через L() и словарь TERMS выше.
 # Дословных замен для них больше нет: они били по JS-литералам и ломались от любой правки кода.
 ("No sizes under that filter yet.", "لا توجد مقاسات ضمن هذا الترشيح بعد."),
 ("Catalogue could not be loaded. Call ", "تعذّر تحميل الكتالوج. اتصل على "),
 (" and we will talk it through.", " وسنتحدث في الأمر."),
 ("Width is usually between 135 and 355.", "العرض عادةً بين 135 و 355."),
 ("Rim diameter is usually between 13 and 24.", "قطر الجنط عادةً بين 13 و 24."),
 ("Catalogue filtered to ", "رُشِّح الكتالوج على "),
 ("Catalogue filtered.", "رُشِّح الكتالوج."),
 ("Nothing within ±3% — call us, we will work it out on the spot.",
  "لا يوجد ضمن ‎±3%‎ — اتصل بنا ونحلّها على الفور."),
 # Имена оставляем латиницей: это подписи профилей Google, а сами отзывы приведены
 # дословно по-английски. Переводить чужие имена — выдумывать.
 ("Vahid · Local Guide, 330 reviews · Google", "Vahid · مرشد محلي، 330 تقييماً · جوجل"),
 ("Mohammad Alalawi · Google", "Mohammad Alalawi · جوجل"),
 ('"FULL SET"', '"طقم كامل"'),
 ('"just the one"', '"قطعة واحدة"'),
 ('qty + " pieces"', 'qty + " قطع"'),
 ('"Copied"', '"تم النسخ"'),
 ('L.push("Hello Wheel Zone, I would like a price.");', 'L.push("مرحباً ويل زون، أرغب بمعرفة السعر.");'),
 ('L.push("Item: " + qItem.value);', 'L.push("المطلوب: " + qItem.value);'),
 ('L.push("Size: " + qSize.value.trim());', 'L.push("المقاس: " + qSize.value.trim());'),
 ('" (full set)"', '" (طقم كامل)"'),
 ('L.push("Quantity: " + qty', 'L.push("الكمية: " + qty'),
 ('L.push("Work needed: " + picked.join(", "));', 'L.push("الخدمات المطلوبة: " + picked.join("، "));'),
 ('L.push("Sent from tirez.ae");', 'L.push("أُرسلت من tirez.ae");'),
]

for a, b in T:
    html = html.replace(a, b)

# чекбоксы услуг в JS ищем по английскому value — чиним
html = html.replace("'#svcBox input[value=\"", "'#svcBox input[value=\"")

if not os.path.isdir("ar"):
    os.mkdir("ar")
io.open(OUT, "w", encoding="utf-8").write(html)

# контроль: не осталось ли длинных английских фраз в видимом тексте
leftovers = re.findall(r'>([A-Z][a-z]{2,}[^<>{}]{14,})<', html)
print("written:", OUT, len(html), "bytes")
print("possible untranslated:", leftovers[:12] if leftovers else "none")
