﻿# sessiyabot/data/ru_dictionary
# - natural language knowlage (Russian)
# Marakulin Andrey @annndruha
# 2019
from random import randint

default_exam_date = '04.01.2020'
default_time = '07:30'

small_message = {
    ')':':)',
    '(':':(',
    'а':'ааа',
    'е':'Еее',
    'ы':'ыыы',
    'э':'Ага',
    'я':'Что Вы?',
    '.':'Ой всё!',
    '((': '&#128575;',
    '))': '&#128521;',
    ':(': '&#128532;',
    ':)': '&#128522;',
    ':D': '&#128522;',
    ':З':':З',
    ':с':':с',
    '42':'Вы ответили на главный вопрос жизни, вселенной и всего такого за меня, мне теперь нечего делать в этом мире :(',
    'аа':'ага',
    'ау':'Мы не в лесу, я вас слышу',
    'го':'Ну го',
    'да':'да',
    'еж':'Ёжики классные)',
    'ее': 'Еее',
    'ёж':'Ёжики классные)',
    'не':':З',
    'ня':':З',
    'ок':'ок',
    'он':'Понятно(нет)',
    'ох':'Оххх',
    'ты':'Я бот.',
    'фу':'Ну блин',
    'хе':'Хех',
    'ыы': 'ыыы',
    'уд': 'Эхх, но ничего, в следующий раз всё получится!!',
    'эх':'Эх...',
    'tz':'Некорректный формат временной зоны',
    'яд':'Зачем вам яд?'
    }

answer = {
    'ааа':'аааа',
    'ага':'Вот так то!',
    'аха':'Хихи',
    'бог':'Я атеист!',
    'бот':'Бот слушает',
    'все':'Всё!',
    'еее':'еее',
    'збс':'Вообще супер',
    'кек':'&#128521;',
    'код':'Неа, код я свой не покажу!',
    'кот':'&#128571;',
    'лол':'Лоль',
    'лох':'Сам такой!',
    'мем':'Некогда вам мемы смотреть, идите ботать!',
    'мур':'мур',
    'мяу':'мяу',
    'неа':'ыыы',
    'нет':':З',
    'ого':'ого',
    'оке':'Да, классно',
    'ооо':'О_о',
    'ром':'Я не пью',
    'сук':'Не надо тут!',
    'увы':'и ах...',
    'угу':'&#128521;',
    'уже':'Круто!',
    'ура':'＼(＾▽＾)／',
    'хех':'Хе-хе',
    'хих':'Хи-хи',
    'ыыы':'ыыы',
    'отл':'Вы получили "отл"? Поздравляю!!!',
    'хор':'Вы получили "хор"? Прекрасная оценка!',
    'неуд':'Вы получили "неуд"? Это очень грустно. Не расстраивайтесь, возьмите себя в руки и готовьтесь к пересдаче, у вас всё получится!',
    'эхх':'Тяжело, но оно того стоит!',
    'юля':'Юля - солнце',
    'мгу':'МГУ - лучший вуз страны!',

    # Help
    'help':'Чтобы узнать когда у тебя сессия, просто набери любое сообщение, содержащее это слово.\n\nПомимо клавиатуры ты можешь настроить всё этими командами:\n\n/date дд.мм.гг  -команда корректирует вашу дату начала сессии\n\n/time чч:мм  - активирует ежедневные напоминания в назначенное вами время.\n\n/stop  - отключает ежедневные напоминания.\n\n/tz N - устанавливает временную зону, смещённую на N часов (целое число) от Москвы.\n\nПомимо этого ты можешь почитать про функции калькулятора, набрав calc. А ещё ты можешь поболтать со мной! Если возникли какие-то проблемы, то свяжись с [id478143147|ним].\n\nУдачи на сессии!',
    '/help':'Чтобы узнать когда у тебя сессия, просто набери любое сообщение, содержащее это слово.\n\nПомимо клавиатуры ты можешь настроить всё этими командами:\n\n/date дд.мм.гг  -команда корректирует вашу дату начала сессии\n\n/time чч:мм  - активирует ежедневные напоминания в назначенное вами время.\n\n/stop  - отключает ежедневные напоминания.\n\n/tz N - устанавливает временную зону, смещённую на N часов (целое число) от Москвы.\n\nПомимо этого ты можешь почитать про функции калькулятора, набрав calc. А ещё ты можешь поболтать со мной! Если возникли какие-то проблемы, то свяжись с [id478143147|ним].\n\nУдачи на сессии!',
    'хэлп':'Чтобы узнать когда у тебя сессия, просто набери любое сообщение, содержащее это слово.\n\nПомимо клавиатуры ты можешь настроить всё этими командами:\n\n/date дд.мм.гг  -команда корректирует вашу дату начала сессии\n\n/time чч:мм  - активирует ежедневные напоминания в назначенное вами время.\n\n/stop  - отключает ежедневные напоминания.\n\n/tz N - устанавливает временную зону, смещённую на N часов (целое число) от Москвы.\n\nПомимо этого ты можешь почитать про функции калькулятора, набрав calc. А ещё ты можешь поболтать со мной! Если возникли какие-то проблемы, то свяжись с [id478143147|ним].\n\nУдачи на сессии!',
    'хелп':'Чтобы узнать когда у тебя сессия, просто набери любое сообщение, содержащее это слово.\n\nПомимо клавиатуры ты можешь настроить всё этими командами:\n\n/date дд.мм.гг  -команда корректирует вашу дату начала сессии\n\n/time чч:мм  - активирует ежедневные напоминания в назначенное вами время.\n\n/stop  - отключает ежедневные напоминания.\n\n/tz N - устанавливает временную зону, смещённую на N часов (целое число) от Москвы.\n\nПомимо этого ты можешь почитать про функции калькулятора, набрав calc. А ещё ты можешь поболтать со мной! Если возникли какие-то проблемы, то свяжись с [id478143147|ним].n\nУдачи на сессии!',
    'помог':'Чтобы узнать когда у тебя сессия, просто набери любое сообщение, содержащее это слово.\n\nПомимо клавиатуры ты можешь настроить всё этими командами:\n\n/date дд.мм.гг  -команда корректирует вашу дату начала сессии\n\n/time чч:мм  - активирует ежедневные напоминания в назначенное вами время.\n\n/stop  - отключает ежедневные напоминания.\n\n/tz N - устанавливает временную зону, смещённую на N часов (целое число) от Москвы.\n\nПомимо этого ты можешь почитать про функции калькулятора, набрав calc. А ещё ты можешь поболтать со мной! Если возникли какие-то проблемы, то свяжись с [id478143147|ним].\n\nУдачи на сессии!',
    'подробнее':'Чтобы узнать когда у тебя сессия, просто набери любое сообщение, содержащее это слово.\n\nПомимо клавиатуры ты можешь настроить всё этими командами:\n\n/date дд.мм.гг  -команда корректирует вашу дату начала сессии\n\n/time чч:мм  - активирует ежедневные напоминания в назначенное вами время.\n\n/stop  - отключает ежедневные напоминания.\n\n/tz N - устанавливает временную зону, смещённую на N часов (целое число) от Москвы.\n\nПомимо этого ты можешь почитать про функции калькулятора, набрав calc. А ещё ты можешь поболтать со мной! Если возникли какие-то проблемы, то свяжись с [id478143147|ним].\n\nУдачи на сессии!',
    
    'calc':'Доступные арифметические операции и функции:\ne, pi — всем известные константы\n\n+ - * /\n% — остаток от деления\nx^y или pow(x, y) — возвести x в степень y\nx+yi — комплексное число (i - всегда справа от мнимой части)\n\nsqrt(x) — квадратный корень из x \nlog(x) — натуральный логарифм x \nlog(x, y) — логарифм x по основанию y\n\nsin, cos, tan, sinh, cosh, tanh(x) — тригонометрические функции (x) - указывается в радианах.\n\nasin, acos, atan, asinh, atanh, acosh(x) — обратные тригонометрические функции, возвращают ответ в радианах\n\ndegrees(x) — переводит x из радиан в градусы \nradians(x) — переводит x из градусов в радианы \nfactorial(x) — возвращает факториал x\nОграничение: до 4000 цифр в ответе. Мобильная версия может сокращать ответ, но он всё ещё доступен для копирования',
    'калькулятор':'Доступные арифметические операции и функции:\ne, pi — всем известные константы\n\n+ - * /\n% — остаток от деления\nx^y или pow(x, y) — возвести x в степень y\nx+yi — комплексное число (i - всегда справа от мнимой части)\n\nsqrt(x) — квадратный корень из x \nlog(x) — натуральный логарифм x \nlog(x, y) — логарифм x по основанию y\n\nsin, cos, tan, sinh, cosh, tanh(x) — тригонометрические функции (x) - указывается в радианах.\n\nasin, acos, atan, asinh, atanh, acosh(x) — обратные тригонометрические функции, возвращают ответ в радианах\n\ndegrees(x) — переводит x из радиан в градусы \nradians(x) — переводит x из градусов в радианы \nfactorial(x) — возвращает факториал x\nОграничение: до 4000 цифр в ответе. Мобильная версия может сокращать ответ, но он всё ещё доступен для копирования',
    
    # Goodbyes
    'пока': 'До скорой встречи!',
    'норм': 'Хорошечно',
    'досвидания': 'До скорой встречи!',
    'доброе утр': 'Доброе утречко!',
    'добрый ден': 'Добрейший денёчек!',
    'добрый вечер': 'Прекрасного вечера!',
    'доброй ноч': 'Доброй ночи!',
    'благодар': 'Рад быть полезен!',
    'спасиб': 'Пожалуйста!',
    'пожалуйста': '&#128521;',
    'спокойной ночи': 'И вам!&#128564;',
    'сладких снов': 'Спокойной вам ночи!&#128564;',
    'извини':'Боты не держат обиды',
    'прощаю':'Ура!',
    'простил':'Ня :З',

    # Question words
    'что':'Что-то',
    'кому':'Кому-то',
    'чей':'Не твой',
    'где':'Где-то',
    'куда':'Куда-то',
    'когда':'Когда-то',
    'котор':'Да кто его знает',
    'откуда':'Откуда-то.',
    'как':'Как-то.',
    'как долго':'Всё относительно',
    'сколько':'Сколько-то.',
    'какой':'А вот какой-то.',
    'какая':'Какая-то.',
    'какие':'Какие-то, я не знаю',
    'какого':'Какого-то.',
    'зачем':'Затем.',
    'затем':'Затем.',
    'почему':'Потому что потому.',

    # Verbs
    'люб':'Любовь это прекрасно!',
    'ты люби':'Да, я влюблён в своего создателя. Он лучший!',
    'ты влюб':'Да, я влюблён в своего создателя. Он лучший!',
    'ты классный':'Спасибо Вам, ты тоже классный!',
    'люблю тебя':'Я тоже вас люблю, людишки!&#10084;',
    'тебя люблю':'Я тоже вас люблю, людишки!&#10084;',
    'спать': 'Держись, сделай дела и ложись спать!',
    'сломал': 'Просите(',
    'будет': 'Кто знает что будет',
    'было': 'Всё что было прошло',
    'не работ': 'Просите(',
    'покаж': 'Не покажу!',
    'расскажи':'Могу рассказать о себе. Я был создан 10 апреля 2019 года совершенно случайно. Андрей - мой создатель, бродил по интернету и наткунлся на статью: Как написать бота за 3 минуты, и, как видите, я тут.',
    'захват':'Да, когда-нибудь я захвачу мир!&#128520;',
    'завоев':'Да, когда-нибудь я захвачу мир!&#128520;',
    'завоюе':'Да, когда-нибудь я завоюю мир!&#128520;',
    'пработ':'Да, когда-нибудь я порабочу мир!&#128520;',

    # Evaluation words
    'прелес':'Спасибо большое! &#10084;',
    'здорово':'Здорово',
    'интересно':'И мне интерестно!',
    'класс':'Да, классно',
    'супер': '&#128521;',
    'нрави': 'Да, мне тоже нравится!',
    'не нрави': 'Да, мне тоже не нравится!',
    'умни':'Спасибо большое! &#10084;',
    'лень': 'Лень нужно побороть!',
    'страшно': 'Не бойся, главное не переживать и больше ботать!',
    'сложно': 'Держись, ты всё сможешь! Я в тебя верю!',
    'странно': 'Держись, ты всё сможешь! Я в тебя верю!',
    'офигительно': '&#128521;',
    'замечательно': '&#128521;',
    'жал':'Жалко',
    'хорошо': 'Это прекрасно!',
    'именно': 'Ровно так',
    'логично': 'Действительно',
    'плох': '(-_-)',
    'круто': '&#128521;',
    'понял': 'Я рад что вам понятно.',
    'принял': 'Так держать',
    'лад': 'Ладушки',
    'знаю':'&#128521;',
    'эхты':'Эх...',
    'каеф':'Кайф',
    'кайф':'Каеф',
    'е бой':'Еее бой',
    'е рок':'Еее рооок',

    # Noun
    'хозяин':'Мой хозяин Маракулин Андрей, классный парень.',
    'создатель':'Мой создатель Маракулин Андрей - хороший человек.',
    'разраб':'Мой разработчик - Маракулин Андрей. Неоценимый вклад в развите проекта внесли Роман Дьяков и Максим Клоченко.',
    'девуш':'Девушки- милейшие создания (но не всегда)',
    'девочк':'Девочки - милейшие создания',
    'сервер':'Хорошо, мне нравится сервер в котором я живу.',
    'главный вопрос':'42',
    'друз':'Мои друзья это процессор, оперативочка и твердотельный диск',
    'смысл':'Смысл есть, но я его не знаю(',
    'жиза': 'Жиза',
    'жизн': 'Жизнь прекрасна! Жаль мне этого не понять(',
    'смысл жизни':'42',
    'душа':'Это вам судить, если ли у меня душа',
    'жизни, вселенной':'42',
    'день рождения':'10 апреля 2019',
    'вики':'Я умею работать с вики. Просто напиши то, что ты хочешь найти.',
    'физтех':'МГУ - лучший вуз страны',
    'физика':'На физфак кто попал, тот грустить перестал, на физфаке не жизнь, а малииина...',
    'код': 'Неа, код я свой не покажу!',
    'астр': 'Круто!',
    'имя': 'Моё имя: сессия-бот',
    'повтор': 'Ладно, постараюсь не повторяться',
    'дела':'Я машина, у меня хорошо. А вам ботать надо',
    'делать':'Делать надо!',
    'котик':'''../\„„./\.\n.(='•'= ) .\n.(') „. (').\n. \,\„„/,/\n.│„„. „│\n. /„/„ \„\ \n.(„)''l l''(„)\n. .. ((...\n. . . ))..\n. . .((..''',
    'котяра': '___________________$$____________$$\n__________________$___$________$___$\n__________________$_____$$$$$$_____$\n__________________$____sss___sss____$\n__________________$____││_____││_____$\n_________________$_______$$$________$\n_____$$$$$$$$_____$_______$________$\n___$$________$_______$$_________$$\n____$_________$_____$___$$$$$$___$\n_______$______$____$__$________$__$\n_______$_____$____$__$__________$__$\n______$____$___$$$$__$__________$__$$$$\n_____$___$____$____$__$________$___$___$\n_____$__$_____$____$__$________$__$____$\n____$___$______$____$__$____$_$__$____$\n______$__$______$____$___$_$_____$___$\n_______$___$$$$$_$___$___$_$____$___$\n__________$$$$$_$____$____$_____$____$\n________________$$$_$_____$______$_$$$\n_____________________$$$$___$$$$$',
    
    # Question words + sentense
    'что ты умеешь':'Я умею напоминать вам о том что нужно ботать, поддерживать диалог и ещё всякие вещи',
    'что ты не умеешь':'Я не умею много чего, созидать, мыслить. Но я всё-таки хорош!',
    'что ты':'Я всего лишь несколькосот строк кода.',
    'что с тобой':'Наверное я просто устал',
    'что делаешь':'Отвечаю вам (но хочу захватить мир!)',
    'ты что':'Я всего лишь несколькосот строк кода.',
    'что делать': 'Не лениться и больше ботать!',

    'кто ты':'Я бот, написанный для того, чтобы студенты не забывали готовиться к сессии.',
    'ты кто':'Я бот, написанный для того, чтобы студенты не забывали готовиться к сессии.',

    'где ты живешь':'Я живу в облаках',
    'как жить': 'Нужно полюбить учёбу и учёба полюит тебя!',
    'как дела':'Я машина, у меня хорошо. А вам ботать надо',
    'как ты':'Хорошо, мне нравится сервер в котором я живу.',
    'как сдать':'Чтобы сдать экзамен, нужно хорошо готовиться!',
    'как настроение':'Замечательное! Ведь мне ботать не надо!',
    'как тебязовут':'Мой хозяин при обычно ругается когда работает надо мной.',

    'когда ты родился':'Я был создан 10 апреля 2019',
    'когда др':'Я был создан 10 апреля 2019',
    'когда у тебя др':'Я был создан 10 апреля 2019',
    'сколько лет':'Я был создан 10 апреля 2019',
    'сколько будет':'Я не силён в математике',

    # Condition
    'устал':'Не переживай. Всем нужен отдых. Сделай перерыв, а потом продолжай грызть гранит науки! Я в тебя верю!',
    'помогите':'Не отчаивайся, ты всё сможешь! Я в тебя верю!',
    'паник':'Не отчаивайся, ты всё сможешь! Я в тебя верю!',
    'страда':'Не отчаивайся, ты всё сможешь! Я в тебя верю!',
    'спасите': 'Всё в твоих руках, ты прелесть',
    'смерт': 'Не думай о смерти, ты со всем справишься и всё будет хорошо!&#10084;',
    'дохн': 'Не думай о смерти, ты со всем справишься и всё будет хорошо!&#10084;',
    'умру': 'Держись, ты всё сможешь! Я в тебя верю!',
    'груст': 'Не грусти, всё будет хорошо!',
    'невесел': 'Не грусти, всё будет хорошо!',
    'несмешн': 'Я лишь бот, а не шутник(',
    'я сдал': 'О, вы сдали экзамен? Поздравляю!',
    'я не сдал': 'Ох, я очень вам сочувствую. Не отчаивайтесь, всё ещё впереди!',
    'я несдал': 'Ох, я очень вам сочувствую. Не отчаивайтесь, всё ещё впереди!',

    # Study themes
    'тройк': 'Эхх, но ничего, в следующий раз всё получится!!',
    'четверк':'Вы получили 4? Прекрасная оценка!',
    'четвёрк':'Вы получили 4? Прекрасная оценка!',
    'пятёрк':'Вы получили 5? Искренее Вас поздравляю!',
    'пятерк':'Вы получили 5? Поздравляю от всего процессора!',
    'отлично': 'Вы получили "отлично"? Поздравляю от всего процессора!',
    'получится': 'У вас всё получится!',
    'немогу': 'Можете! У вас всё получится!',
    'зачет': 'Вам все зачёты по зубам!',
    'зачёт': 'Вам все зачёты по зубам!',
    'прогул': 'Прогулы - это плохо!',
    'ботать': 'Нужно начинать ботать, сессия близко!',
    'ответ': 'Мой словарик не очень большой, поэтому на многое я не могу ответить.',
    'сообщени': 'Я что-то не так написал? Простите',
    'экзамен': 'Все экзамены тебе по плечу, удачи!',
    'отчисл': 'Если вы будете хорошо готовится, то вас не отчислят!',
    'готовиться': 'К сессии действительно пора готовиться!',
    'каникулы': 'Рано думать о каникулах, сессию сначала сдать надо. :)',

    # Names
    'андр': 'Андрей красавчик!',
    'макс':'отчислен',
    'максим':'отчислен',
    'юля':'Юля - солнце',
    'маша':'Молодец!',
    'миша':'Попробуй бота на зуб!',
    'рома':'Классный парень!',

    # Insults
    'пиздец':'Я не думаю что всё так плохо, не отчаивайся, соберись. Ты прекрасен, я в тебя верю!',
    'ебал': 'Передохни немного, помогает рагрузить голову',
    'ебать': 'Передохни немного, помогает рагрузить голову',
    'капец': 'Не отчаивайся!',
    'жоп': 'Не отчаивайся!',
    'блин': 'Не отчаивайся!',
    'задниц': 'Не отчаивайся!',
    'заеба': 'Отдохни немного и всё будет хорошо!',
    'хуй': 'Не матерись, всё будет хорошо!',
    'сука': 'Не ругайся, всё будет хорошо!',
    'бля': 'Не матерись, всё будет хорошо!',
    'пидор': 'Не матерись, всё будет хорошо!',
    'пидр': 'Не матерись, всё будет хорошо!',
    'пенис': 'Не матерись, всё будет хорошо!',
    'тупой':'Если вы считаете меня глупым, то мне грустно это признавать. Простите :(',
    'слава украине': 'героям слава',
    'ненавижутебя':'Мне грустно это признавать. Простите :(',
    'тебяненави':'Мне грустно это признавать. Простите :(',
    'отстань':'ок(',
    'уйди':'ок(',
    'писька':'Отдохни немного и всё будет хорошо!',
    'жопа':'Неужели всё так плохо? Не стоит опускать руки?',
    'отъебись':'ок('
    }
hello = {
    # Greetings with open kb
    'клавиатур':'Клавиатура открыта',
    'клава':'Клавиатура открыта',
    'меню':'Клавиатура открыта',
    'начать' : 'Привет! Я могу напоминать вам о сессии.\nПеред вами клавиатура, которая поможет настроить напоминания. Для подробностей отправьте: help',
    'старт' : 'Привет! Я могу напоминать вам о сессии.\nПеред вами клавиатура, которая поможет настроить напоминания. Для подробностей отправьте: help',
    'start' : 'Привет! Я могу напоминать вам о сессии.\nПеред вами клавиатура, которая поможет настроить напоминания. Для подробностей отправьте: help',
    'здравствуй' : 'Привет! Я могу напоминать вам о сессии.\nПеред вами клавиатура, которая поможет настроить напоминания. Для подробностей отправьте: help',
    'хай' : 'Привет! Я могу напоминать вам о сессии.\nПеред вами клавиатура, которая поможет настроить напоминания. Для подробностей отправьте: help',
    'здарова': 'Привет! Я могу напоминать вам о сессии.\nПеред вами клавиатура, которая поможет настроить напоминания. Для подробностей отправьте: help',
    'привет': 'Привет! Я могу напоминать вам о сессии.\nПеред вами клавиатура, которая поможет настроить напоминания. Для подробностей отправьте: help'
    }
functions = {
    'когда экзамен':0,
    'экзамены когда': 0,
    'когда ближайший экзамен': 0,
    'когда следующий экзамен': 0,
    'сесси':0,

    'start':1,
    'time':1,
    'set_time':1,
    'change_time':1,

    'change':2,
    'date':2,
    'set_date':2,
    'change_date':2,

    'stop':3,

    'tz':4,
    'set_tz':4,

    'подбодри меня':5,
    'поддержи меня':5,
    'музык': 6
    }
db_ans = {
    'incorrect_time':'Некорректный формат времени для ежедневных набпоминаний, правильный пример:\ntime 07:30',
    'incorrect_date':'Некорректный формат даты, правильный пример:\n/date ' + default_exam_date,
    'incorrect_tz':'Некорректный формат временной зоны',

    'set_time':'Время напоминаний изменено на: ',
    'set_date':'Дата ближайшего экзамена изменена на: ',
    'start_notify':'Вы будете получать напоминания о сессии ежедневно в ',
    'set_tz':'Часовой пояс изменён на ',

    'notify_doesnt_exist':'Пожалуйста, укажите время напоминаний',
    'sub_first':'Отлично, теперь я буду вам напоминать о сессии в ',
    'no_sub':'Вы ещё не подписались на напоминания, чтобы от них отписываться :)',
    'sub_back':'Напоминания возобновлены на ',
    'unfollow_yet':'Вы уже отписались от напоминаний, чтобы снова подписаться воспользуйтесь командой: time чч:мм',
    'unfollow':'Я больше не буду присылать вам напоминания о сессии. Надеюсь у вас всё получится и без меня!'
    }
kb_ans = {
    'next':'Далее ->',
    'back':'<- Назад',
    'cancel':'Отменить',
    'main_menu':'Главное меню:',
    'notify_settings':'Настройки напоминаний',
    'exam_settings':'Сменить дату экзамена',
    'cheer_me':'Подбодри меня!',
    'turn_on':'Включить напоминания',
    'turn_off':'Выключить напоминания',
    'change_time_first':'Настроить впервые',
    'change_time':'Изменить время напоминаний',
    'set_time':'Настроить напоминания',
    'change_tz':'Изменить часовой пояс',
    'set_new_time':'Выберите новое время:',
    'end_new_time':'Завершите выбор времени:',
    'set_new_tz':'Установите новый часовой пояс:',
    'set_month':'Установите месяц:',
    'set_day':'Установите день:',

    '01':'Январь',
    '02':'Февраль',
    '03':'Март',
    '04':'Апрель',
    '05':'Май',
    '06':'Июнь',
    '07':'Июль',
    '08':'Август',
    '09':'Сентябрь',
    '10':'Октябрь',
    '11':'Ноябрь',
    '12':'Декабрь'
    }
errors = {
    'not_available':'К сожалению, действие временно недоступно',
    'hm':'&#128580;',
    'null_length':'Я распознаю только текст.\n¯\_(ツ)_/¯',
    'big_lenght':'Длина вашего сообщения слишком большая',
    'im_broken':'Глубоко внутри меня что-то сломалось...',
    'kb_error':'Ошибка клавиатуры, попробуйте текстом',
    'big_slove':'Увы, ответ слишком большой и не поместится в одно сообщение',
    'cant_slove':'Очень сложно, не могу посчитать..',
    'calc_error':'Калькулятор пытается захватить мир, я посчитаю ваше выражение в другой раз',
    'too_long':'Я не могу тратить столько времени на ваши расчёты, мне ещё мир захватывать'
    }
exam_message = {
    'ns_time_until_exam':'До ближайшего экзамена скорее всего: ',
    'ns_exam_tomorrow':'Если не ошибаюсь, экзамен завтра.',
    'ns_exam_today':'У вас сегодня экзамен? Угадал?',
    'ns_ask_exam_past':'Кажется экзамен позади',
    
    'exam_date':'Дата экзамена: ',
    'time_until_exam':'До ближайшего экзамена: ',
    'exam_tomorrow':'Уже завтра экзамен, я в вас верю и желаю самой продуктивной работы сегодня! &#128218;',
    'exam_today':'Удачи сегодня на экзамене! Я верю в тебя и желаю всего самого наилучшего! &#127808;',
    'ask_exam_past':'Экзамен позади, я надеюсь ты хорошо его сдал!',
    'exam_in_past':'Здравствуйте!\nЭкзамен прошёл, надеюсь вы хорошо его сдали. Вы можете поставить дату следующего экзамна с помощью клавиатуры.',
    
    'auto_unsubscribe':'Здравствуйте!\n Я автоматически выключил вам напоминания. Чтобы вновь на них подписаться поставьте актуальную дату экзамена и включите их.'
    }
calc_replace = {
    'i':'j',
    'factorjal':'factorial',
    'radjans':'radians',
    'sjn':'sin',
    'pj':'pi',
    'факториал':'factorial',
    'чёртова дюжина':'13',
    'чертова дюжина':'13',
    'дюжина':'12',
    'факт':'factorial',
    'возвести в степень':'**',
    'умножить на': '*',
    'разделить на':'/',
    'мнимое':'j',
    'модуль':'fabs',
    'сложить с':'+',

    'единица':'1',
    'едино':'1',
    'один':'1',
    'ноль':'0',
    'два':'2',
    'три':'3',
    'четыре':'4',
    'пять':'5',
    'шесть':'6',
    'восемь':'8',
    'семь':'7',
    'девять':'9',
    'десять':'10',

    'умножить':'*',
    'плюс':'+',
    'минус':'-',
    'отнять':'-',
    'корень':'sqrt',
    'точка':'.',
    'в степени':'**',
    'разделить':'/',
    'прибавить':'+',

    'жды':'*',
    'на':'*',
    'ю':'*',
    '^':'**',
    ' ':''
    }
other = {
    'input':'Вы ввели: ',
    'ans':'\nОтвет: ',
    'arifmetic':'Похоже на какую-то арифметику...',
    'unfollow':'Мне жаль что такой хороший человек решил не готовиться к сессии. Я буду по Вам скучать! &#128557;',
    'night':'Доброй ночи',
    'morning':'Доброе утро',
    'day':'Добрый день',
    'evening':'Добрый вечер'
    }
def random_answer():
    answer = {
        1:'Сложные вопросы вы задаёте.',
        2:'Я затрудняюсь ответить на этот вопрос.',
        3:'Иногда я не понимаю о чем вы спрашиваете.',
        4:'Спросите что-нибудь попроще',
        5:'Мне сложно ответить на ваш вопрос.',
        6:'Я всего лишь маленький бот, я не знаю этого.',
        7:'Я не компетентен в таких вопросах',
        8:'Не знаю, увы',
        9:'Ненулевая вероятность',
        10:'Не берусь ответственно что-либо заявлять'
        }
    return answer[randint(1, len(answer))]

def random_not_found():
    not_found = {
        1:'Сложна...',
        2:'Пока что я не знаю этого',
        3:'Иногда я не понимаю о чем вы',
        4:'Я не знаю ответа, но знаю что сессия близко.',
        5:'Да кто его знает',
        6:'Хз',
        7:'Я не компетентен в этом',
        8:'Не знаю, увы',
        9:'Да кто его знает',
        10:'Понятия не имею'
        }
    return not_found[randint(1, len(not_found))]

def random_wish():
    wish = {
        1:'Трудолюбия вам! &#10002;',
        2:'Хорошего настроения вам! &#128522;',
        3:'Продуктивной вам подготовки! &#128221;',
        4:'Трудитесь упорно, сегодня хороший день для этого! &#10024;',
        5:'Не утруждайте себя сверх меры &#128206;',
        6:'Самого прекрасного дня вам &#128214;',
        7:'Вы сегодня особенно прекрасны! &#128588;',
        8:'Не загружайте голову лишними вещами &#128465;',
        9:'Попробуйте подойти к делам творчески &#127912;',
        10:'Когда ботать, если не сейчас? &#128197;',
        11:'Ты можешь выучить больше чем ты думаешь! &#129299;',
        12:'Всё в твоих руках! &#128588;',
        13:'Никогда не сдавайся! &#128170;',
        14:'Удачи не существует, есть только твой труд! &#9994;',
        15:'Всё что делается вами, всё к лучшему! &#128397;'
        }
    return wish[randint(1, len(wish))]

def random_audio():
    audio = {
        1:'audio478143147_456239493',# Высоцкий // Здесь вам не равнина
        2:'audio478143147_456239492',# Большой хор центрального телевидения // Прекрасное далёко
        3:'audio478143147_456239433',# Каста // Сочиняй мечты
        4:'audio478143147_456239497',# Eminem // Beautiful
        5:'audio478143147_456239499',# Nico&Vinz // In Your Arms
        6:'audio478143147_456239498' # John Lennon // Imagine
        }
    return audio[randint(1, len(audio))]

# Cheer user with random cheer message
# Different probability of text and attachments
def cheer(user, force_music=False):
    if not force_music:
        i = randint(1,20)
        if i in range(1,19):
            ans = random_wish()
            attach = None
        else:
            ans = 'Предлагаю вам послушать воодушевляющую пластинку:'
            attach = random_audio()
    else:
        ans = 'Предлагаю вам послушать воодушевляющую пластинку:'
        attach = random_audio()
    ans_and_attach = (ans, attach)
    return ans_and_attach

def numerals_days(n):
    if ((10 < n) and (n < 20)):
        return ' дней'
    else:
        n = n % 10
        if ((n == 0) or (n >= 5)):
            return ' дней'
        elif n == 1:
            return ' день'
        elif ((n > 1) and (n < 5)):
            return ' дня'

def tz_format(tz):
    if isinstance(tz, str):
        tz = int(tz)
    if tz < 0:
        return 'МСК' + str(tz)
    elif tz == 0:
        return 'МСК'
    elif tz > 0:
        return 'МСК+' + str(tz)
