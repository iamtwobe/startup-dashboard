from src.utils.notifier import phone_notify
from src.api.exchange_api import exchange_currencies, compare_exchange
from src.utils.get_date import get_date
from src.api.weather_api import get_weather
import webview
import time
import json


def start_interface(window_name, debug=False):
    dashboard_page = 'templates/dashboard.html'
    loading_page = 'templates/loading_page/index.html'
    index_page = 'templates/index.html'
    test_page = 'templates/test.html'

    class API:
        def start_program(self):
            window.load_url(loading_page)
            time.sleep(0) # mudar para 5 dps
            window.load_url(dashboard_page)

        def home(self):
            window.load_url(dashboard_page)
        
        def bot_btn(self):
            window.load_url(index_page)

        def dashboard(self):
            window.load_url('templates/dashboard.html')

    api = API()

    window = webview.create_window(window_name, 'templates/', js_api=api)
    webview.settings = {
        'ALLOW_DOWNLOADS': False,
        'ALLOW_FILE_URLS': True,
        'OPEN_EXTERNAL_LINKS_IN_BROWSER': False,
        'OPEN_DEVTOOLS_IN_DEBUG': True
    }
    webview.start(api.start_program, debug=debug)


def start_structure(notify=False):
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
            debug=True
        )
    
    with open('templates/data/data.json', 'w') as f:
        json.dump(data, f, indent=4)
        f.close()

if __name__ == '__main__':
    #start_structure(notify=False)
    start_interface("Lian's Dashboard", debug=False)