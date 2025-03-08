LEXICON: dict[str, str] = {
    'start': 'Начать',
}

BUTTON: dict[str, str] = {
    'start': 'Начать',
}

censorship_list = ["шлюхи", "заработать", "разбогатеть", "обнаженочки", "ставки", "интимных", "чат", "знакомств",
                   "голые",
                   "промокод", "розыгрыши", "играть",
                   "девушки", "казино", "выигрыш", "выйгрыш", "играйте", "шкура", "шкуры", "пробей", "слитые",
                   "ахуенно", "шлюху", "травку", "носки",
                   "учете", "учёте", "выплат", "скама", "подработка", "поебота",
                   "подработку", "платим", "маякни", "сливы",
                   "заработок", "маркетолог", "сотрудники", "архипиздрит", "басран", "бздение", "бздеть",
                   "бздех", "бзднуть", "бздун", "бздунья", "бздюха",
                   "блежник", "блудилище", "бляд", "блябу", "блябуду", "блядун", "блядунья", "блядь",
                   "блядюга",
                   "взьебка", "волосянка", "взьебывать", "вз'ебывать", "выблядок", "выблядыш", "выебать", "выеть",
                   "выпердеть", "высраться", "выссаться", "говенка", "говенный", "говешка", "говназия", "говнецо",
                   "говно", "говноед", "говночист", "говнюк", "говнюха", "говнядина", "говняк", "говняный", "говнять",
                   "гондон", "дермо", "долбоеб", "дрисня", "дрист", "дристать", "дристануть", "дристун", "дристуха",
                   "дрочена", "дрочила", "дрочилка", "дрочить", "дрочка", "ебало", "ебальник", "ебануть", "ебаный",
                   "ебарь", "ебатория", "ебать", "ебаться", "ебец", "ебливый", "ебля", "ебнуть", "ебнуться", "ебня",
                   "ебун", "елда", "елдак", "елдачить", "заговнять", "задристать", "задрока", "заеба", "заебанец",
                   "заебать", "заебаться", "заебываться", "заеть", "залупа", "залупаться", "залупить", "залупиться",
                   "замудохаться", "засерун", "засеря", "засерать", "засирать", "засранец", "засрун", "захуячить",
                   "злоебучий", "изговнять", "изговняться", "кляпыжиться", "курва", "курвенок", "курвин", "курвяжник",
                   "курвяжница", "курвяжный", "манда", "мандавошка", "мандей", "мандеть", "мандища", "мандюк",
                   "минет", "минетчик", "минетчица", "мокрохвостка", "мокрощелка", "мудак", "муде", "мудеть", "мудила",
                   "мудистый", "мудня", "мудоеб", "мудозвон", "муйня", "набздеть", "наговнять", "надристать",
                   "надрочить", "наебать", "наебнуться", "наебывать", "нассать", "нахезать", "нахуйник", "насцать",
                   "обдристаться", "обосранец", "обосрать", "обосцать", "обосцаться", "обсирать", "опизде",
                   "отпиздячить",
                   "отпороть", "отъеть", "охуевательский", "охуевать", "охуевающий", "охуеть", "охуительный",
                   "охуячивать",
                   "охуячить", "педрик", "пердеж", "пердение", "пердеть", "пердильник", "перднуть", "пердун",
                   "пердунец", "подработать", "подработка",
                   "пердунина", "пердунья", "пердуха", "пердь", "передок", "пернуть", "пидор", "пидарас", "пидорас",
                   "пизда", "пиздануть", "пизденка", "пиздеть", "пиздить", "пиздища", "пиздобратия", "пиздоватый",
                   "пиздорванец", "пиздорванка", "пиздострадатель", "пиздун", "пиздюга", "пиздюк", "пиздячить",
                   "писять", "питишка", "плеха", "подговнять", "подъебнуться", "поебать", "поеть", "попысать",
                   "посрать", "поцоватый", "презерватив", "проблядь", "проебать", "промандеть",
                   "промудеть", "пропиздеть", "пропиздячить", "пысать", "разъеба", "разъебай", "распиздай",
                   "распиздеться", "распиздяй", "распроеть", "растыка", "сговнять", "секель", "серун", "серька",
                   "сика", "сикать", "сикель", "сирать", "сирывать", "скурвиться", "скуреха", "скурея", "скуряга",
                   "скуряжничать", "спиздить", "срака", "сраный", "сранье", "срать", "срун", "ссака", "ссаки",
                   "ссать", "старпер", "струк", "суходрочка", "сцавинье", "сцака", "сцаки", "сцание", "сцать",
                   "сциха", "сцуль", "сцыха", "сыкун", "титечка", "титечный", "титка", "титочка", "титька",
                   "трипер", "триппер", "уеть", "усраться", "усцаться", "фик", "фуй", "хезать", "хер", "херня",
                   "херовина", "херовый", "хитрожопый", "хлюха", "хуевина", "хуевый", "хуек", "хуепромышленник",
                   "хуерик", "хуесос", "хуище", "хуй", "хуйня", "хуйрик", "хуякать", "хуякнуть", "целка",
                   "шлюха", "блять", "нахуй", "манда", "хуйня", "обман", "ненавижу", "мошенничество",
                   "вранье", "бабки", "разводите", "развод", "секс", "отзывная",
                   "обманщики", "мошенники",
                   "уроды", "твари", "гниды", "сволочи", "мрази",
                   "официалы", "смерть", "смерти", "трупы", "трупами", "трупам", "трупов",
                   "кровь", "крови", "кровью", "войной", "войнами", "война", "бомбы", "бомбами", "бомбежка",
                   "бомбёжка", "бомбят", "артиллерия", "артилерия", "артилерийский", "гитлеру", "гитлер",
                   "путлер", "путлеру", "пыне", "фашисты", "фашики", "фашиками", "фашистами", "фашисту",
                   "фашику", "нацики", "нацисты", "нацбаты", "всу", "ВСУ", "всушники", "хохлы",
                   "ООН", "совбез", "ранения", "раненые", "раненные", "раны", "кровище", "солдаты",
                   "солдатня", "солдатами", "солдатам", "пиндосы", "митинг", "протест",
                   "молиться", "заняться сексом",
                   "санбат", "разбить", "выбить", "драться",
                   "кулаками", "стрелять", "убить", "умереть", "шайтан", "выстрелить", "взрывы",
                   "взрывами", "взорвать", "заложить", "взрывчатку", "поджечь", "сжечь", "осел", "тупые",
                   "Обман", "Мошенничество",
                   "Вранье", "говно", "хуй", "Пандора", "Старлайн", "отзывная",
                   "обманщики", "мошенники", "уроды",
                   "твари", "гниды", "сволочи", "мрази ", "жопа", "смерть", "смерти",
                   "трупы", "трупами", "трупам", "трупов", "кровь", "крови", "кровью", "войной", "войнами", "война",
                   "бомбы", "бомбами", "бомбежка", "бомбёжка", "бомбят", "артиллерия", "артилерия", "артилерийский",
                   "гитлеру", "гитлер", "путлер", "путлеру", "пыне", "фашисты", "фашики", "фашиками", "фашистами",
                   "фашисту", "фашику", "нацики", "нацисты", "нацбаты", "всу", "всушники", "хохлы",
                   "блять", "хуйня", "сука", "чмо", "урод",
                   "нахуй", "хуй", "пизда", "мудак", "уебок", "дебил", "пидор", "бляди", "мрази", "говно", "гавно",
                   "дерьмо", "пиздец", "твари", "тварь", "жопа", "херь", "нахер", "нах", "днище", "позор",
                   "жопу", "жопе", "мудовые", "мудя", "стыдно", "хер",
                   "удаляют", "удаляете", "удалять", "трете", "херам",
                   "идиоты", "идиотский", "идиотские", "идиотских", "хyйня", "хулион",
                   "6ля", "6лядь", "6лять", "b3ъeб", "cock", "cunt", "e6aль", "ebal", "eblan",
                   "eбaл", "eбaть", "eбyч", "eбать", "eбёт", "eблантий", "fuck", "fucker", "fucking", "xyёв", "xyй",
                   "xyя", "xуе", "xуй", "xую", "zaeb", "zaebal", "zaebali", "zaebat", "архипиздрит", "ахуел", "ахуеть",
                   "бздение", "бздеть", "бздех", "бздецы", "бздит", "бздицы", "бздло", "бзднуть", "бздун", "бздунья",
                   "бздюха", "бздюшка", "бздюшко", "бля", "блябу", "блябуду", "бляд", "бляди", "блядина", "блядище",
                   "блядки", "блядовать", "блядство", "блядун", "блядуны", "блядунья", "блядь", "блядюга", "блять",
                   "вафел", "вафлёр", "взъебка", "взьебка", "взьебывать", "въеб", "въебался", "въебенн", "въебусь",
                   "въебывать", "выблядок", "выблядыш", "выеб", "выебать", "выебен", "выебнулся", "выебон",
                   "выебываться", "выпердеть", "высраться", "выссаться", "вьебен", "гавно", "гавнюк", "гавнючка",
                   "гамно", "гандон", "гнид", "гнида", "гниды", "говенка", "говенный", "говешка", "говназия", "говнецо",
                   "говнище", "говно", "говноед", "говнолинк", "говночист", "говнюк", "говнюха", "говнядина", "говняк",
                   "говняный", "говнять", "гондон", "доебываться", "долбоеб", "долбоёб", "долбоящер", "дрисня", "дрист",
                   "дристануть", "дристать", "дристун", "дристуха", "дрочелло", "дрочена", "дрочила", "дрочилка",
                   "дрочистый", "дрочить", "дрочка", "дрочун", "е6ал", "е6ут", "еб твою мать", "ёб твою мать", "ёбaн",
                   "ебaть", "ебyч", "ебал", "ебало", "ебальник", "ебан", "ебанамать", "ебанат", "ебаная", "ёбаная",
                   "ебанический", "ебанный", "ебанныйврот", "ебаное", "ебануть", "ебануться", "ёбаную", "ебаный",
                   "ебанько", "ебарь", "ебат", "ёбат", "ебатория", "ебать", "ебать-копать", "ебаться", "ебашить",
                   "ебёна", "ебет", "ебёт", "ебец", "ебик", "ебин", "ебись", "ебическая", "ебки", "ебла", "еблан",
                   "ебливый", "еблище", "ебло", "еблыст", "ебля", "ёбн", "ебнуть", "ебнуться", "ебня", "ебошить",
                   "ебская", "ебский", "ебтвоюмать", "ебун", "ебут", "ебуч", "ебуче", "ебучее", "ебучий", "ебучим",
                   "ебущ", "ебырь", "елда", "елдак", "елдачить", "жопа", "жопу", "заговнять", "задрачивать",
                   "задристать", "задрота", "зае6", "заё6", "заеб", "заёб", "заеба", "заебал", "заебанец", "заебастая",
                   "заебастый", "заебать", "заебаться", "заебашить", "заебистое", "заёбистое", "заебистые", "заёбистые",
                   "заебистый", "заёбистый", "заебись", "заебошить", "заебываться", "залуп", "залупа", "залупаться",
                   "залупить", "залупиться", "замудохаться", "запиздячить", "засерать", "засерун", "засеря", "засирать",
                   "засрун", "захуячить", "заябестая", "злоеб", "злоебучая", "злоебучее", "злоебучий", "ибанамат",
                   "ибонех", "изговнять", "изговняться", "изъебнуться", "ипать", "ипаться", "ипаццо",
                   "какдвапальцаобоссать", "конча", "курва", "курвятник", "лох", "лошарa", "лошара", "лошары", "лошок",
                   "лярва", "малафья", "манда", "мандавошек", "мандавошка", "мандавошки", "мандей", "мандень",
                   "мандеть", "мандища", "мандой", "манду", "мандюк", "минет", "минетчик", "минетчица", "млять",
                   "мокрощелка", "мокрощёлка", "мразь", "мудak", "мудaк", "мудаг", "мудак", "муде", "мудель", "мудеть",
                   "муди", "мудил", "мудила", "мудистый", "мудня", "мудоеб", "мудозвон", "мудоклюй", "нахер", "нахуй",
                   "набздел", "набздеть", "наговнять", "надристать", "надрочить", "наебать", "наебет", "наебнуть",
                   "наебнуться", "наебывать", "напиздел", "напиздели", "напиздело", "напиздили", "насрать",
                   "настопиздить", "нахер", "нахрен", "нахуй", "нахуйник", "не ебет", "не ебёт", "невротебучий",
                   "невъебенно", "нехира", "нехрен", "нехуй", "нехуйственно", "ниибацо", "ниипацца", "ниипаццо",
                   "ниипет", "никуя", "нихера", "нихуя", "обдристаться", "обосранец", "обосрать", "обосцать",
                   "обосцаться", "обсирать", "объебос", "обьебать", "обьебос", "однохуйственно", "опездал", "опизде",
                   "опизденивающе", "остоебенить", "остопиздеть", "отмудохать", "отпиздить", "отпиздячить", "отпороть",
                   "отъебись", "охуевательский", "охуевать", "охуевающий", "охуел", "охуенно", "охуеньчик", "охуеть",
                   "охуительно", "охуительный", "охуяньчик", "охуячивать", "охуячить", "очкун", "падла", "падонки",
                   "падонок", "паскуда", "педерас", "педик", "педрик", "педрила", "педрилло", "педрило", "педрилы",
                   "пездень", "пездит", "пездишь", "пездо", "пездят", "пердануть", "пердеж", "пердение", "пердеть",
                   "пердильник", "перднуть", "пёрднуть", "пердун", "пердунец", "пердунина", "пердунья", "пердуха",
                   "пердь", "переёбок", "пернуть", "пёрнуть", "пи3д", "пи3де", "пи3ду", "пиzдец", "пидар", "пидарaс",
                   "пидорас", "пидарасы", "пидары", "пидор", "пидорасы", "пидорка", "пидорок", "пидоры", "пидрас",
                   "пизда", "пиздануть", "пиздануться", "пиздарваньчик", "пиздато", "пиздатое", "пиздатый", "пизденка",
                   "пизденыш", "пиздёныш", "пиздеть", "пиздец", "пиздит", "пиздить", "пиздиться", "пиздишь", "пиздища",
                   "пиздище", "пиздобол", "пиздоболы", "пиздобратия", "пиздоватая", "пиздоватый", "пиздолиз",
                   "пиздонутые", "пиздорванец", "пиздорванка", "пиздострадатель", "пизду", "пиздуй", "пиздун",
                   "пиздунья", "пизды", "пиздюга", "пиздюк", "пиздюлина", "пиздюля", "пиздят", "пиздячить", "писбшки",
                   "писька", "писькострадатель", "писюн", "писюшка", "подговнять",
                   "подонки", "подонок", "подъебнуть", "подъебнуться", "поебать", "поебень", "поёбываает", "поскуда",
                   "посрать", "потаскуха", "потаскушка", "похер", "похерил", "похерила", "похерили", "похеру", "похрен",
                   "похрену", "похуй", "похуист", "похуистка", "похую", "придурок", "приебаться", "припиздень",
                   "припизднутый", "припиздюлина", "пробзделся", "проблядь", "проеб", "проебанка", "проебать",
                   "промандеть", "промудеть", "пропизделся", "пропиздеть", "пропиздячить", "раздолбай", "разхуячить",
                   "разъеб", "разъеба", "разъебай", "разъебать", "распиздай", "распиздеться", "распиздяй",
                   "распиздяйство", "распроеть", "сволота", "сволочь", "сговнять", "секель", "серун", "серька",
                   "сестроеб", "сикель", "сирать", "сирывать", "соси", "спиздел", "спиздеть", "спиздил", "спиздила",
                   "спиздили", "спиздит", "спиздить", "срака", "сраку", "сраный", "сранье", "срать", "срун", "ссака",
                   "ссышь", "стерва", "страхопиздище", "сука", "суки", "суходрочка", "сучара", "сучий", "сучка",
                   "сучко", "сучонок", "сучье", "сцание", "сцать", "сцука", "сцуки", "сцуконах", "сцуль", "сцыха",
                   "сцышь", "съебаться", "сыкун", "трахае6", "трахаеб", "трахаёб", "трахатель", "ублюдок", "уебать",
                   "уёбища", "уебище", "уёбище", "уебищное", "уёбищное", "уебк", "уебки", "уёбки", "уебок", "долбаёб",
                   "долбаеб", "охуеете", "дебил", "хер", "херь", "хуев", "хохол", "хохлушка", "хохлинка", "хуйло",
                   "хрен", "метамфетамин", "метамфетамина", "мет", "пидорасов", "пидарасов", "жалоба", "клевета",
                   "обман", "иск", "какого фига",
                   "пендосы",
                   "враги", "ненавижу", "бабки", "разводите", "развод", "секс", "задолбали",
                   "наебываете", "хватит", "кал", "горите", "спамить", "дурить", "говна пожуй",
                   "туфта", "жахаться", "ссанина", "говна",
                   "жахаться", "цыган", "пародия", "дурилово", "дурят", "развод ",
                   "разводняк", "петухи", "гнилое", "сгнило", "петух", "калище",
                   "цыган", "гниет",
                   "конченные", "гниёт", "конченые", "тупой", "кончать", "нийтраль", "Хуесосы",
                   "игнор", "отстой", "хуйня", "секса", "ебистика",
                   "лохи", "отстой", "ублюдство", "срань", "понос",
                   "хуйня полная", "ебистика", "хуита", "конченый", "Хуесосы", "кринж",
                   "треш", "ширпотреб", "хрень", "абоба", "гашик", "конченный",
                   "развалюха китайская", "развалюха", "СВО", "жополизы", "обсосы", "утырки", "убейтесь", "дешёвки",
                   "дешевки", "зажрались", "сосал", "сосать", "обсосы", "сосня", "воюют", "отврат", "конченые", "срань",
                   "отвратительно", "калище", "дерьмище", "засранцы", "Путин",
                   "жопошники", "хуесосы", "путин", "вагина",
                   "ущербные", "хуеплеты", "увольте", "хуета", "Дичь", "корыто", "дрочу",
                   "дрочите",
                   "дешмань", "дешманский ", "дешевка", "отстой", "пидарашья", "воняет", "кал",
                   "пососать не завернуть", "ширпотреб", "наркотики",
                   "наркота", "кокос", "спид", "утиль", "в рот", "китайщина", "обсосыши",
                   "хуем по лбу", "очко", "мамашу", "китайское", "дерьмо", "отъебнул", "отъебнуло", "отъебнула",
                   "отрыгнул", "отрыгнула", "отрыгнуло", "член", "пендосская", "гомики", "сосать",
                   "ущербный", "ущербно", "украли", "украл", "дерьмицо", "гавно", "мда", "треш", "ебаный", "пидарашья",
                   ]
