import requests


def get_weather(some_city):
    params = {"n": "", "M": "", "q": "", "T": "", "lang": "ru"}
    url = "https://ru.wttr.in/{}".format(some_city)
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    cities = ("Лондон", "аэропорт Шереметьево", "Череповец")
    for city in cities:
        print(get_weather(city))
