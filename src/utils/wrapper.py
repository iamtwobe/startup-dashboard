from src.utils.notifier import phone_notify
from src.api.exchange_api import exchange_currencies, compare_exchange
from src.utils.get_date import get_date
from src.api.weather_api import get_weather
import json


def data_wrapper(notify=False, debug_notify=False):
    """Starts all functionalities of the program
    such as the APIs, the data, day and weather
    then wraps them together"""
    
    today, yesterday, weekday = get_date()
    
    currencies = exchange_currencies(date_t=today, date_y=yesterday)
    dollar_t, dollar_y = currencies.get('dollar_rate')[:4], currencies.get('dollar_yesterday')[:4]
    euro_t, euro_y = currencies.get('euro_rate')[:4], currencies.get('euro_yesterday')[:4]

    dollar_state = compare_exchange(
        currency_today=dollar_t,
        currency_yesterday=dollar_y
    )
    euro_state = compare_exchange(
        currency_today=euro_t,
        currency_yesterday=euro_y
    )

    weather_condition, temperature, weather_img = get_weather()

    data = {
            "weather": weather_condition,
            "weather_img": weather_img,
            "temperature": f"{temperature}ºC",
            "date": f"{today[8:]}/{today[5:7]}",
            "weekday": weekday,
            "dollar_rate": str(dollar_t).replace('.', ','),
            "dollar_state": dollar_state,
            "euro_rate": str(euro_t).replace('.', ','),
            "euro_state": euro_state
        }

    if notify:
        phone_notify(
            date=data["date"],
            weather=data["weather"], temperature=data["temperature"],
            dollar=data["dollar_rate"], dollar_state=data["dollar_state"],
            euro=data["euro_rate"], euro_state=data["euro_state"],
            debug=debug_notify
        )
    
    with open('templates/data/data.json', 'w') as f:
        json.dump(data, f, indent=4)
        f.close()