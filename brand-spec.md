# WHEEL ZONE TYRE TRADING — brand-spec

Единственные источники фактов: дамп Google Maps + снятый вживую tirez.ae (Playwright, 07.10.2026).
Всё, чего здесь нет — не идёт в вёрстку.

---

## 1. Факты из дампа Google Maps

| Поле | Значение | Статус |
|---|---|---|
| Название EN | `WHEEL ZONE TYRE TRADING (4X_WHEELS)` | ✅ факт |
| Название AR | `ویل زون لتجارة الاطارات` | ✅ факт |
| Категория | Магазин шин / Tyre shop | ✅ факт |
| Адрес | `36TH STREET - Ras Al Khor - Ras Al Khor Industrial Area 2 - Dubai` | ✅ факт |
| Телефон | `04 576 2199` (tel:+97145762199) | ✅ факт |
| Plus code | `59J9+C8 Дубай` | ✅ факт |
| Рейтинг | 4,4 · 40 отзывов на Google | ✅ факт — **только текстом, НЕ в JSON-LD** |
| Часы | известно ТОЛЬКО «закроется в 23:00» | ⚠️ неполно |
| Загруженность | среда, сейчас низкая | ℹ️ не для сайта |
| Фото | есть в профиле, свежие (10 дней) | ⚠️ у меня нет файлов |

### Чего в дампе НЕТ — не выдумывать
- Полное недельное расписание (только время закрытия)
- Сайт в профиле Maps не указан (`Добавить сайт` — пусто) → tirez.ae к профилю не привязан
- WhatsApp-номер
- Email
- Прайс, бренды шин/дисков, размеры
- Ссылка на профиль Maps (нужна для кнопки «отзывы»)

---

## 2. За что хвалят в отзывах — это и есть заголовки секций

Три видимых отзыва, дословно:

**Vahid** (Local Guide, 330 отзывов) — «newly opened **tire and rim repair** shop… staff were friendly, professional… took the time to **explain the issues with my wheels**… **fair prices**»

**Mohammad Alalawi** — «best prices, top-quality tyres… you get a **warranty on both the tyres and the work**… **selection of rims? Crazy good — whatever style you're thinking of, they've got it**»

**Hamid Entezam** (Local Guide) — «bought a set of tyres… the way their **staff welcomes you and guide you**… price very good, quality very well, best service»

### Выводы, на которых строится сайт
1. **ДИСКИ — главный товар, не шины.** Два из трёх отзывов про диски и выбор дисков. Конкурент Tire Zone в том же районе имеет 1 733 отзыва на шинах — бодаться там бессмысленно.
2. **Ремонт дисков** — подтверждённая отзывом услуга. Это главный отрыв от конкурентов.
3. **Гарантия на товар И на работу** — подтверждено отзывом, это сильный блок.
4. **Объясняют, что не так с колесом** — ядро тона: консультация, а не впаривание.
5. Магазин **новый** (отзывам ~год) — поэтому 40 отзывов, а не 1 700. Молодость не скрывать.

---

## 3. Что реально сняли с tirez.ae

Сайт на конструкторе Zyro/Hostinger. Снято вживую через Playwright.

### Палитра старого сайта
`rgb(29,30,32)` текст · `rgb(13,20,26)` фон-тёмный · `rgb(244,249,252)` светлый фон.
Акцента нет вообще — сайт бесцветный.

### Шрифты старого сайта
`DM Sans` (body), `PT Serif`, `Roboto`. Случайный набор конструктора, не бренд.

### ⚠️ Жёсткий вывод: переносить с сайта практически нечего

| Что | Состояние |
|---|---|
| **Логотип** | ✅ **единственный настоящий ассет.** 1260×491 PNG, синий `#057CBC` + чёрная шина + гаечные ключи, тяжёлый слэб-вордмарк |
| Каталог `/products` | ❌ **пусто.** Страница буквально отдаёт «No publicly visible products» |
| `/rims`, `/tyres`, `/services`, `/contacts` | ❌ **не существуют.** SPA отдаёт одну и ту же главную на все роуты |
| Контакты на сайте | ❌ **заглушки конструктора:** `support@wheelzone.com`, `+1234567890` |
| Отзывы на сайте | ❌ **фальшивые:** «John Doe, New York», «Jane Smith, Los Angeles» |
| Фото | ⚠️ 11 стоковых Unsplash, ни одного фото их магазина |
| Тексты | ⚠️ рыба конструктора: «we specialize in high-quality tyres…» |

**Фактически мы делаем сайт с нуля.** «Обновить существующий» нечего — существующий это демо-шаблон с чужими контактами.

---

## 4. Ассеты в проекте

Перенесено с tirez.ae, сконвертировано в WebP, 1600px по ширине.

| Файл | Что | Куда |
|---|---|---|
| `img/logo.webp` / `logo.png` (630×245) | **логотип бренда** | шапка, футер, favicon, og |
| `img/hero-side.webp` (1600×898) | ч/б борт белой машины, тёмный литой диск, чисто | **кандидат в hero** |
| `img/rim-dark.webp` (1600×2400) | диск в тёмном контровом свете | **кандидат в hero**, тёмная сетка |
| `img/rim-chrome.webp` (1600×2124) | крупный многоспицевый хром на сером авто | карточка каталога |
| `img/rim-caliper.webp` (1600×2416) | серебро + красный суппорт | карточка каталога |
| `img/rim-bronze.webp` (1600×2400) | бронза/золото на чёрном авто | карточка каталога |
| `img/rim-wire.webp` (1600×2848) | крупный спицованный хром | карточка каталога |
| `img/rim-redline.webp` (1600×2133) | чёрный диск с красной полосой, премиум-авто | крупная плитка bento |
| `img/tyre-asphalt.webp` (1600×1200) | шина + диск на асфальте | блок шин |
| `img/workshop-hands.webp` (1600×1066) | руки в перчатках с шиной в цеху | **блок «ремонт дисков» / услуги** |
| `img/showroom.webp` (1600×1066) | торговый зал шин, жёлтая стена | блок «витрина», приглушить |

**Выброшено:** `photo-1700722209617` — на фото вывеска чужого магазина «EXPRESS TYRE SHOP» с логотипами MRF/Michelin/Apollo/CEAT/JK. Ставить на сайт клиента рекламу другого шиномонтажа нельзя.

**Чего в ассетах нет:** ни одного фото их цеха, витрины, стеллажа с дисками, вывески, команды. Ни одного «до/после» ремонта диска. Ни одного товара.

---

## 5. Бренд

| Токен | Значение | Откуда |
|---|---|---|
| Основной синий | `#057CBC` | 38 364 пикселя логотипа — доминирующий цвет |
| Тёмный синий | `#0560A3` | тень вордмарка в логотипе |
| Чёрный шины | `#0A1504` | тело шины в эмблеме |
| Форма вордмарка | тяжёлый slab/serif, разрядка, подчёркивание | логотип |

---

## 5a. Применимости дисков (WhatsApp 26.10.2026, правка клиента 28.10.2026)

Формат строки клиента: `диаметр · PCD · CB`. **Это боевые данные, они на сайте.**

| Авто | Диаметры | PCD | CB |
|---|---|---|---|
| Jeep Wrangler | 17 | 5×127 | 71 |
| Jetour T2 | 17, 20 | 5×108 | 60 |
| Toyota Land Cruiser 100 | 16 | 5×150 | 110 ✳ |
| Toyota Land Cruiser 200 | 17, 18 | 5×150 | 110 |
| Toyota Land Cruiser 300 | 17 | 6×139.7 | 95 |
| Nissan Patrol Y61 | 16, 17 | 6×139.7 | 110 |
| Nissan Patrol Y62 | 17, 18, 20 | 6×139.7 | **78** ✳ |
| Nissan Patrol Y63 | 17 | 6×139.7 | **78** ✳ |

✳ — исправлено/добавлено клиентом 28.10.2026.

Лежит в `catalog.json` → `vehicles` + `rims`, **8 машин, 12 позиций**. На сайте подбор
«по автомобилю»: марка → модель → только подходящие диски + плашка PCD / CB / диаметры.

### ✅ Расхождение закрыто — проверка себя оправдала

26.10 клиент прислал по Y62 `CB110`. Я не стал класть на сайт и сверил: у Y62 штатное
центральное отверстие **78,1 мм**, 110,1 — это предыдущий Y61. Источники:
[dynamicwheelco.com.au](https://dynamicwheelco.com.au/vehicle/nissan/patrol-y62/),
[avtoreference.com](https://avtoreference.com/en/auto/nissan/patrol/2019/).

28.10 клиент подтвердил правку своей рукой: `Nissan Y62 17 6x139 Cb110` → **`Cb78`**,
дословно «Yes sorry bro». Заодно прислал **новую машину Y63** (тоже CB78) и подтвердил,
что у LC100 именно `CB110` — в первом сообщении было «cb1100», это опечатка.

**Вывод на будущее: присланные клиентом числа сверять до публикации, а не после.**
Ошибка сидела бы на боевом сайте, человек купил бы диск и не надел его на ступицу.

### ⚠️ Не разобрано
- В переписке два **голосовых по 0:15** — я их не слышал, присланы только скриншотом.
  Если там есть цифры (ширина, вылет, цены) — нужен текст или пересылка аудио.
- Клиент сам пишет «Let me know brother if anything missing» — он готов дослать, надо просить.

### Чего в применимостях НЕТ
- **Ширина (J) и вылет (ET)** — без них подбор неполный. На карточках стоит «уточняется».
- Размеры шин под эти же машины.
- Цены и наличие по каждой позиции.
- Свои фото — на карточках иллюстративные, и это написано прямо в секции.

---

## 6. Что дослать (RU — для Александра)

**Блокеры, без них сайт не наполнить:**
1. **Прайс или хотя бы вилки** — иначе каталог и калькулятор без цифр. Цены не выдумываю.
2. **Ширина (J) и вылет (ET)** по каждой применимости из таблицы 5a.
3. **Остальные машины** — прислали 7, наверняка есть ещё.
4. ⚠️ **Подтвердить CB у Patrol Y62** — см. красный блок выше.
5. **Бренды шин**, если каталог шин тоже должен стать реальным.
3. **Полное расписание** на неделю — знаю только «закрывается в 23:00».
4. **WhatsApp-номер** — тот же `04 576 2199` или мобильный? Это главная кнопка на сайте.
5. **Ссылка на их профиль Google Maps** — для кнопки «4.4 на Google».
6. **Фото магазина:** витрина дисков, стеллаж, цех, вывеска, 2–3 «до/после» ремонта диска. Сейчас на сайте будет 100% стока.
7. **Логотип в SVG или PNG без фона** — есть только PNG 1260×491 с белой подложкой.
8. Домен: остаёмся на `tirez.ae` или берём новый?

**Чего НЕ будет на сайте (и это правильно):**
— фальшивые отзывы John Doe / Jane Smith · `+1234567890` · `support@wheelzone.com` · «500+ клиентов» · aggregateRating в JSON-LD.

---

## 7. Questions for the client (EN — под копипаст)

> Hi! I'm rebuilding the Wheel Zone website from scratch — the current one still has the template's demo contacts and demo reviews on it, so it can't be used as it is. To fill it with your real business I need the following:
>
> **Your fitment list — it is live**
> Thank you for the correction on the Y62 and for the Y63. All eight cars are on the site now: pick the make, pick the model, and only the wheels that bolt on are shown. Wrangler, Jetour T2, LC100, LC200, LC300, Patrol Y61, Y62 and Y63.
>
> 1. For each of those I still need the **rim width (J) and the offset (ET)**. Those are the last two numbers missing from every card — without them a customer cannot be sure the wheel will clear the brake and sit flush, and right now the site honestly says "to confirm".
> 2. You sent two voice notes that did not reach me, only the screenshots did. If there were any numbers in them, could you type them out?
> 3. Which other cars can you cover? Eight is a strong start, and every model you add is another customer landing on exactly the right page.
>
> **Stock & pricing**
> 4. Price list, or at least a price range per fitment — for example "17" 6x139.7 from AED X". Without numbers the site can only say "price on request".
> 5. Which tyre brands do you actually keep in stock, and what tyre sizes go with each of the cars above (for example 275/60R20 for the Y62)?
> 6. What do you charge for fitting, balancing, alignment, puncture repair, nitrogen and rim repair?
>
> **Services**
> 5. Your customers specifically mention rim repair in the reviews. What exactly do you repair — buckled rims, cracks, curb rash, refinishing/powder coating? How long does it take?
> 6. What does the warranty cover — the tyres, the workmanship, or both? For how long?
>
> **Contacts & hours**
> 7. Full opening hours for every day of the week, including Friday and Sunday. Google only shows me the closing time (23:00).
> 8. Is `04 576 2199` also your WhatsApp, or is there a separate mobile number? WhatsApp will be the main button on the site.
> 9. Business email for the contact form.
> 10. Please send me the link to your Google Maps profile.
>
> **Photos — this is the important one**
> 11. I need real photos of your shop: the rim display, the storage racks, the workshop, the shopfront sign, your team at work. 10–15 photos taken on a phone are perfectly fine.
> 12. Two or three before/after shots of a rim repair would be the single strongest thing on the whole website.
> 13. Do you have the logo as an SVG or a transparent PNG?
>
> **Language**
> 14. Do you want the site in English and Arabic? Most of your neighbours in Ras Al Khor search in Arabic, so I'd recommend both.
