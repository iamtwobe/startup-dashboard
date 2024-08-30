import webview
import time
import json


def start_interface():
    loading_page = 'templates/loading_page/index.html'
    index_page = 'templates/index.html'
    test_page = 'templates/test.html'

    class API:
        def start_program(self):
            window.load_url(loading_page)
            time.sleep(0) # mudar para 5 dps
            window.load_url(index_page)

        def home(self):
            window.load_url(test_page)
        
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
    webview.start(api.start_program, debug=False)

def get_data():
    data = {
        'weather': 'Sunny',
        'date': '2024-08-30',
        'dollar_rate': '5.25',
        'euro_rate': '5.85'
    }

    return data

if __name__ == '__main__':
    start_interface()