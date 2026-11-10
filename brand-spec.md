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
| Рейтинг | **4,6 · 63 отзыва** на Google (снято с живой карточки 10.11.2026; на 07.10 было 4,4 · 40) | ✅ факт — **только текстом, НЕ в JSON-LD** |
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
| `img/rim-01…08.webp` (~490×560) | отдельные диски, нарезаны со стены | карточки каталога |
| `img/rim-tall-a/-b.webp` (489×1200 / 489×1075) | вертикальные полосы стойки, два диска | высокие плитки bento |
| `img/rim-big.webp` (637×636) | серебристый 12-лучевой, фас | крупная плитка bento |
| `img/rim-hero.webp` (534×533) | тот же диск фасом | вращающееся колесо в шапке |
| `img/tyre-asphalt.webp` (1600×1200) | шина + диск на асфальте | блок шин |
| `img/workshop-hands.webp` (1600×1066) | руки в перчатках с шиной в цеху | **блок «ремонт дисков» / услуги** |
| `img/showroom.webp` (1600×1066) | торговый зал шин, жёлтая стена | блок «витрина», приглушить |

**Выброшены все шесть первых `rim-*` (05.11.2026).** На них были суперкары, а на `rim-redline` читалась **эмблема Lamborghini** — диск от Уруса под подписью «подходит Nissan Patrol Y62» противоречил собственным данным карточки. Это та же ошибка, что и с чужой вывеской ниже, только внутри каталога.

**Чем заменены.** Все двенадцать картинок нарезаны из ОДНОГО кадра — тёмная стена дисков, [Pexels #36202185](https://www.pexels.com/photo/36202185/), лицензия Pexels: коммерческое использование без атрибуции, изменения разрешены. Критерии отбора: ни одной машины в кадре, ни одной читаемой эмблемы автопроизводителя, ни одного цветного акцента (бронзовые и золотые диски с этого же кадра не взяты, красные суппорты тоже). Побочно вес упал с ≈2,1 МБ до ≈245 КБ.

⚠️ Два соседних кадра рассмотрены и отклонены: Pexels #5661682 — жёлтые стеллажи и читаемые колпаки Toyota, VW, Ford; Pexels #5661690 — передний диск обрезан рамкой, целиком не вынимается.

**Выброшено раньше:** `photo-1700722209617` — на фото вывеска чужого магазина «EXPRESS TYRE SHOP» с логотипами MRF/Michelin/Apollo/CEAT/JK. Ставить на сайт клиента рекламу другого шиномонтажа нельзя.

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

## 5a. Применимости дисков — боевые данные клиента

Полный список 15.10.2026 + дополнение 26.10 + правка 28.10. **14 машин, 21 позиция, всё на сайте.**

| Авто | Диаметры | PCD | CB |
|---|---|---|---|
| Dodge Ram | 17, 18 | 5×139.7 | 77 |
| Ford F-150 | 17, 18, 20 | 6×135 | 87 |
| GMC ⚠️ модель не названа | 17, 18, 20 | 6×139.7 | 78 |
| Jeep Wrangler | 17 | 5×127 | 71 |
| Jetour T2 | 17, 20 | 5×108 | 60 |
| Lexus LX 570 ⚠️ прислано как «Ls570» | 17, 18, 20 | 5×150 | 110 |
| Nissan Patrol Y61 | 16, 17 | 6×139.7 | 110 |
| Nissan Patrol Y62 ✳ | 17, 18, 20 | 6×139.7 | **78** |
| Nissan Patrol Y63 ✳ | 17, 18, 20 | 6×139.7 | **78** |
| Nissan Xterra | 16 | 6×114.3 | 66 |
| Suzuki Jimny | 15, 16 | 5×139.7 | 108 |
| Toyota Land Cruiser 100 ✳ | 16 | 5×150 | 110 |
| Toyota Land Cruiser 200 | 17, 18 | 5×150 | 110 |
| Toyota Land Cruiser 300 | 17 | 6×139.7 | 95 |

✳ — клиент поправил сам 28.10.

Проверка целостности проходит: битых ссылок нет, машин без дисков нет,
**у каждой машины ровно одно центральное отверстие на все диаметры** — физически верно,
ЦО это свойство ступицы, а не диаметра.

### ✅ Расхождение закрыто — проверка себя оправдала

26.10 клиент прислал по Y62 `CB110`. Я не стал публиковать и сверил: у Y62 штатное ЦО
**78,1 мм**, 110,1 — это предыдущий Y61. Источники:
[dynamicwheelco.com.au](https://dynamicwheelco.com.au/vehicle/nissan/patrol-y62/),
[avtoreference.com](https://avtoreference.com/en/auto/nissan/patrol/2019/).

28.10 клиент поправил себя своей рукой: `Y62 17 6x139 Cb110` → **`Cb78`**, дословно
«Yes sorry bro». Заодно дал Y63 (тоже CB78) и подтвердил, что у LC100 именно `CB110` —
«cb1100» было опечаткой.

**Правило: числа клиента сверять ДО публикации, а не после.**

### ⚠️ Две вещи ждут подтверждения

**1. «Ls570» — такой машины не существует.** Lexus LS это 5×120 / CB60.1, а присланные
5×150 / CB110 — это ровно **LX 570**. Проверено:
[wheel-sizes.com](https://wheel-sizes.com/hubbore/lexus/lx-570/),
[studpattern.com](https://studpattern.com/lexus-lx570-2008/).
На сайте стоит **LX 570**, как и `cb1100` → `CB110` раньше. Нужно подтверждение.

**2. «Gmc» прислан без модели.** 6×139.7 / CB78 — это платформа GM 1500 (Sierra, Yukon),
но Canyon там уже 6×120, поэтому «все GMC» написать нельзя. В подборе модель стоит как
**«— модель уточняется»**, в тексте заявки остаётся просто «GMC».

### ⚠️ Не разобрано
- Два **голосовых по 0:15** — присланы скриншотом, я их не слышал. Если там цифры — нужен текст.
- Клиент сам пишет «Let me know brother if anything missing» — готов досылать.

### Чего в применимостях НЕТ
- **Ширина (J) и вылет (ET)** — на карточках стоит «уточняется». Последняя дыра.
- Размеры шин под эти машины.
- Цены и наличие.
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
5. ~~Ссылка на их профиль Google Maps~~ — **НАЙДЕНА 10.11.2026**, вопрос закрыт: CID `0x51e638f879101ecd` → `5901467001549758157`, канонический вид https://maps.google.com/?cid=5901467001549758157 . Выведена ссылкой в блоке «Come in».
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
> Thank you for the correction on the Y62 and for the Y63. All fourteen cars are on the site now: pick the make, pick the model, and only the wheels that bolt on are shown. Ram, F-150, GMC, Wrangler, Jetour T2, LX 570, Patrol Y61/Y62/Y63, Xterra, Jimny, LC100, LC200 and LC300.
>
> 1. Two of the lines need a quick confirmation. You wrote **"Ls570"** — Lexus never made an LS570, and 5x150 with a 110 mm bore is exactly the **LX 570**, so that is what the site says. Correct? And **"Gmc"** came without a model: 6x139.7 / CB78 is the Sierra and Yukon platform, but the Canyon is 6x120, so which GMC models do you mean?
> 2. For every car I still need the **rim width (J) and the offset (ET)**. Those are the last two numbers missing from every card — without them a customer cannot be sure the wheel will clear the brake and sit flush, and right now the site honestly says "to confirm".
> 3. You sent two voice notes that did not reach me, only the screenshots did. If there were any numbers in them, could you type them out?
> 4. Which other cars can you cover? Fourteen is a strong start, and every model you add is another customer landing on exactly the right page.
>
> **Stock & pricing**
> 5. Price list, or at least a price range per fitment — for example "17" 6x139.7 from AED X". Without numbers the site can only say "price on request".
> 6. Which tyre brands do you actually keep in stock, and what tyre sizes go with each of the cars above (for example 275/60R20 for the Y62)?
> 7. What do you charge for fitting, balancing, alignment, puncture repair, nitrogen and rim repair?
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
