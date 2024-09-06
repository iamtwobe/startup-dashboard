from src.utils.wrapper import data_wrapper
import webview


def start_interface(window_name, debug=False):
    dashboard_page = 'templates/dashboard.html'
    index_page = 'templates/index.html'
    test_page = 'templates/test.html'

    class API:
        def start_program(self):
            window.load_url(dashboard_page)

        def home(self):
            window.load_url(dashboard_page)
        
        def bot_btn(self):
            window.load_url(index_page)

        def dashboard(self):
            window.load_url('templates/dashboard.html')

    api = API()

    window = webview.create_window(window_name, 'templates/', js_api=api, width=880, height=650, resizable=False)
    webview.settings = {
        'ALLOW_DOWNLOADS': False,
        'ALLOW_FILE_URLS': True,
        'OPEN_EXTERNAL_LINKS_IN_BROWSER': False,
        'OPEN_DEVTOOLS_IN_DEBUG': True
    }
    webview.start(api.start_program, debug=debug)


if __name__ == '__main__':
    #data_wrapper(notify=True, debug_notify=True)
    start_interface("Lian's Dashboard", debug=False)