from src.utils.notifier import phone_notify
import webview
import time
import json


def start_interface(debug=False):
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

    window = webview.create_window("Lian's Dashboard", 'templates/', js_api=api)
    webview.settings = {
        'ALLOW_DOWNLOADS': False,
        'ALLOW_FILE_URLS': True,
        'OPEN_EXTERNAL_LINKS_IN_BROWSER': False,
        'OPEN_DEVTOOLS_IN_DEBUG': True
    }
    webview.start(api.start_program, debug=debug)


def start_structure(notify=True):
    """Starts all functionalities of the program
    such as the APIs, the data, day and weather
    then wraps them together"""
    ...

    # match case for dollar and euro state (for increase/decrease/stable)
    # match case for weather for each possible state
    if notify:
        phone_notify(
            date="30/08",
            weather="ensolarado", temperature="25ºC",
            dollar=5.25, dollar_state="decrease",
            euro=6.25, euro_state="decrease"
        )

if __name__ == '__main__':
    start_structure()
    start_interface(debug=False)