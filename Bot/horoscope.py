from Bot.settings import HEADERS
from bs4 import BeautifulSoup
import requests


def get_url(zodiac, type, time):
    """
    The function allows to get the URL with a horoscope based on user's request
    """
    zodiac_signs_rambler = {'Овен': 'aries', 'Телец': 'taurus', 'Близнецы': 'gemini',
                            'Рак': 'cancer', 'Лев': 'leo', 'Дева': 'virgo',
                            'Весы': 'libra', 'Скорпион': 'scorpio', 'Стрелец': 'sagittarius',
                            'Козерог': 'capricorn', 'Водолей': 'aquarius', 'Рыбы': 'pisces'}
    time_horoscope_rambler = {'Вчера': '/yesterday', 'Сегодня': '', 'Завтра': '/tomorrow',
                              'Неделя': '/weekly', 'Месяц': '/monthly'}
    types_horoscope_rumbler = {'Общий': '', 'Любовный': '/erotic', 'Финансы': '/career'}
    url = 'https://horoscopes.rambler.ru/' + str(zodiac_signs_rambler[zodiac]) + str(
        types_horoscope_rumbler[type]) + str(time_horoscope_rambler[time])
    return url


def get_html(url, params=None):
    """
    The function allows to get the URL's data
    """
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    """
    The function collects a horoscope for user
    """
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='_1dQ3')

    target_horoscope = []
    for item in items:
        target_horoscope.append(item.find('span').get_text())
    return target_horoscope[0]


def parse(url):
    """
    The function returns the result of "get_html" and "get_content" functions
    """
    html = get_html(url)
    if html.status_code == 200:
        return get_content(html.text)
    else:
        return 'Error'


if __name__ == "__main__":
    parse(get_url('Рыбы', 'Финансы', 'Сегодня'))