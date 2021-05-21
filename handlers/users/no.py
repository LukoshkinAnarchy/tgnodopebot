import requests
from bs4 import BeautifulSoup


def get_answer(name):
    name = name.lower()
    search_parameters = {
        '': f'{name}'
    }
    url = 'https://antonymonline.ru/%D0%97/'

    response = requests.get(url, params=search_parameters)
    x = response.url
    new_url = x.replace("?=", "")

    html_text = requests.get(new_url).text
    soup = BeautifulSoup(html_text, 'html.parser')

    y = soup.find_all("span")
    a = str(y[4])

    d = a.replace("<span>", "")
    g = d.replace("</span>", "")
    if g != 'Страницы сайта антонимов:':
        return g
    elif g != 'Страница сайта антонимов:':
        url = f'https://xn----7sbfc3aaqnhaffdukg9p.xn--p1ai/words?keyword={name}'

        response = requests.get(url, params=search_parameters)
        x = response.url
        new_url = x.replace("?=", "")

        html_text = requests.get(new_url).text
        soup = BeautifulSoup(html_text, 'html.parser')

        k = soup.find_all('h3')
        try:
            for strong_tag in k[1]:
                return strong_tag.text
        except IndexError:
            return 'ответа не нашлось'

