import requests


def show_weather(some_city):
    url = "https://ru.wttr.in/{}?n?M?q?T".format(some_city)
    response = requests.get(url)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    cities = ("Лондон", "аэропорт Шереметьево", "Череповец")
    for city in cities:
        print(show_weather(city))
