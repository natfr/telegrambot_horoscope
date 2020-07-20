from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, ReplyKeyboardMarkup


# `callback_data` -- это то, что будет присылать TG при нажатии на каждую кнопку
# , поэтому каждый идентификатор должен быть уникальным

time_horoscope_rambler = {'Вчера': 'yesterday', 'Сегодня': '', 'Завтра': 'tomorrow',
                          'Неделя': 'weekly', 'Месяц': 'monthly'}
types_horoscope = {'Общий': '', 'Любовный': 'erotic', 'Финансы': 'career'}

CALLBACK_BUTTON1_aries = "callback_button1_aries"
CALLBACK_BUTTON2_taurus = "callback_button2_taurus"
CALLBACK_BUTTON3_gemini = "callback_button3_gemini"
CALLBACK_BUTTON4_cancer = "callback_button4_cancer"
CALLBACK_BUTTON5_leo = "callback_button5_leo"
CALLBACK_BUTTON6_virgo = "callback_button6_virgo"
CALLBACK_BUTTON7_libra = "callback_button7_libra"
CALLBACK_BUTTON8_scorpio = "callback_button8_scorpio"
CALLBACK_BUTTON9_sagittarius = "callback_button9_sagittarius"
CALLBACK_BUTTON10_capricorn = "callback_button10_capricorn"
CALLBACK_BUTTON11_aquarius = "callback_button11_aquarius"
CALLBACK_BUTTON12_pisces = "callback_button12_pisces"

CALLBACK_BUTTON13_yesterday = "callback_button13_yesterday"
CALLBACK_BUTTON14_ = "callback_button14_"
CALLBACK_BUTTON15_tomorrow = "callback_button15_tomorrow"
CALLBACK_BUTTON16_weekly = "callback_button16_weekly"
CALLBACK_BUTTON17_monthly = "callback_button17_monthly"

CALLBACK_BUTTON18_ = "callback_button18_"
CALLBACK_BUTTON19_erotic = "callback_button19_erotic"
CALLBACK_BUTTON20_career = "callback_button20_career"

CALLBACK_BUTTON21_start = "callback_button21_start"
CALLBACK_BUTTON22_firststart = 'callback_button22_firststart'

TITLES_zodiac = {
    CALLBACK_BUTTON1_aries: "Овен ♈",
    CALLBACK_BUTTON2_taurus: "Телец ♉",
    CALLBACK_BUTTON3_gemini: "Близнецы ♊",
    CALLBACK_BUTTON4_cancer: "Рак ♋",
    CALLBACK_BUTTON5_leo: "Лев ♌",
    CALLBACK_BUTTON6_virgo: "Дева ♍",
    CALLBACK_BUTTON7_libra: "Весы ♎",
    CALLBACK_BUTTON8_scorpio: "Скорпион ♏",
    CALLBACK_BUTTON9_sagittarius: "Стрелец ♐",
    CALLBACK_BUTTON10_capricorn: "Козерог ♑",
    CALLBACK_BUTTON11_aquarius: "Водолей ♒",
    CALLBACK_BUTTON12_pisces: "Рыбы ♓",
}

TITLES_time = {
    CALLBACK_BUTTON13_yesterday: "Вчера ⬅",
    CALLBACK_BUTTON14_: "Сегодня",
    CALLBACK_BUTTON15_tomorrow: "Завтра ➡",
    CALLBACK_BUTTON16_weekly: "Неделя",
    CALLBACK_BUTTON17_monthly: "Месяц",
}

TITLES_type = {
    CALLBACK_BUTTON18_: "Общий 📖",
    CALLBACK_BUTTON19_erotic: "Любовный 💔",
    CALLBACK_BUTTON20_career: "Финансы 💰",
}

TITLES_start = {
    CALLBACK_BUTTON21_start: "Получить новый гороскоп",
    CALLBACK_BUTTON22_firststart: 'Получить гороскоп сейчас!'}

buttons_zodiac = (CALLBACK_BUTTON1_aries, CALLBACK_BUTTON2_taurus,
                  CALLBACK_BUTTON3_gemini, CALLBACK_BUTTON4_cancer,
                  CALLBACK_BUTTON5_leo, CALLBACK_BUTTON6_virgo,
                  CALLBACK_BUTTON7_libra, CALLBACK_BUTTON8_scorpio,
                  CALLBACK_BUTTON9_sagittarius, CALLBACK_BUTTON10_capricorn,
                  CALLBACK_BUTTON11_aquarius, CALLBACK_BUTTON12_pisces)

buttons_type = (CALLBACK_BUTTON18_, CALLBACK_BUTTON19_erotic, CALLBACK_BUTTON20_career)

buttons_time = (CALLBACK_BUTTON13_yesterday, CALLBACK_BUTTON14_, CALLBACK_BUTTON15_tomorrow,
                CALLBACK_BUTTON16_weekly, CALLBACK_BUTTON17_monthly)

buttons_start = CALLBACK_BUTTON21_start


def get_zodiac_keyboard():
    """
    Keyboard with zodiac signs
    """
    # Каждый новый список внутри keyboard - это новая горизонталньая строка
    keyboard = [
        [
            InlineKeyboardButton(TITLES_zodiac[CALLBACK_BUTTON1_aries], callback_data=CALLBACK_BUTTON1_aries),
            InlineKeyboardButton(TITLES_zodiac[CALLBACK_BUTTON2_taurus], callback_data=CALLBACK_BUTTON2_taurus),
            InlineKeyboardButton(TITLES_zodiac[CALLBACK_BUTTON3_gemini], callback_data=CALLBACK_BUTTON3_gemini),
            InlineKeyboardButton(TITLES_zodiac[CALLBACK_BUTTON4_cancer], callback_data=CALLBACK_BUTTON4_cancer),
        ],
        [
            InlineKeyboardButton(TITLES_zodiac[CALLBACK_BUTTON5_leo], callback_data=CALLBACK_BUTTON5_leo),
            InlineKeyboardButton(TITLES_zodiac[CALLBACK_BUTTON6_virgo], callback_data=CALLBACK_BUTTON6_virgo),
            InlineKeyboardButton(TITLES_zodiac[CALLBACK_BUTTON7_libra], callback_data=CALLBACK_BUTTON7_libra),
            InlineKeyboardButton(TITLES_zodiac[CALLBACK_BUTTON8_scorpio], callback_data=CALLBACK_BUTTON8_scorpio),
        ],
        [
            InlineKeyboardButton(TITLES_zodiac[CALLBACK_BUTTON9_sagittarius],
                                 callback_data=CALLBACK_BUTTON9_sagittarius),
            InlineKeyboardButton(TITLES_zodiac[CALLBACK_BUTTON10_capricorn], callback_data=CALLBACK_BUTTON10_capricorn),
            InlineKeyboardButton(TITLES_zodiac[CALLBACK_BUTTON11_aquarius], callback_data=CALLBACK_BUTTON11_aquarius),
            InlineKeyboardButton(TITLES_zodiac[CALLBACK_BUTTON12_pisces], callback_data=CALLBACK_BUTTON12_pisces),
        ],
    ]
    return InlineKeyboardMarkup(keyboard, resize_keyboard=True)


def get_time_horoscope_keyboard():
    """
    Keyboard with time buttons
    """
    keyboard = [
        [
            InlineKeyboardButton(TITLES_time[CALLBACK_BUTTON13_yesterday], callback_data=CALLBACK_BUTTON13_yesterday),
            InlineKeyboardButton(TITLES_time[CALLBACK_BUTTON14_], callback_data=CALLBACK_BUTTON14_),
            InlineKeyboardButton(TITLES_time[CALLBACK_BUTTON15_tomorrow], callback_data=CALLBACK_BUTTON15_tomorrow),
        ],
        [
            InlineKeyboardButton(TITLES_time[CALLBACK_BUTTON16_weekly], callback_data=CALLBACK_BUTTON16_weekly),
            InlineKeyboardButton(TITLES_time[CALLBACK_BUTTON17_monthly], callback_data=CALLBACK_BUTTON17_monthly),
        ]
    ]
    return InlineKeyboardMarkup(keyboard, resize_keyboard=True)


def get_type_horoscope_keyboard():
    """
    Keyboard with different types of horoscope
    """
    keyboard = [
        [
            InlineKeyboardButton(TITLES_type[CALLBACK_BUTTON18_], callback_data=CALLBACK_BUTTON18_),
            InlineKeyboardButton(TITLES_type[CALLBACK_BUTTON19_erotic], callback_data=CALLBACK_BUTTON19_erotic),
            InlineKeyboardButton(TITLES_type[CALLBACK_BUTTON20_career], callback_data=CALLBACK_BUTTON20_career),
        ]
    ]
    return InlineKeyboardMarkup(keyboard, resize_keyboard=True)


def start_again():
    """
    Keyboard with "Get a new horoscope" button.
    """
    keyboard = [
        [
            InlineKeyboardButton(TITLES_start[CALLBACK_BUTTON21_start], callback_data=CALLBACK_BUTTON21_start)
        ]
    ]
    return InlineKeyboardMarkup(keyboard, resize_keyboard=True)


def first_keybord():
    """
    Keyboard with "Get a new horoscope" button.
    """
    keyboard = [
        [
            InlineKeyboardButton(TITLES_start[CALLBACK_BUTTON22_firststart], callback_data=CALLBACK_BUTTON22_firststart)
        ]
    ]
    return InlineKeyboardMarkup(keyboard, resize_keyboard=True)


def admin_keyboard():
    """
    Keyboard for Admin's panel
    """
    return ReplyKeyboardMarkup([['Отправить сообщение' ,'Все пользователи']])