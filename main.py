import webview
import time
import json
import subprocess


def start_interface():
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
    webview.start(api.start_program, debug=False)

def get_data():
    data = {
        'weather': 'Sunny',
        'date': '2024-08-30',
        'dollar_rate': '5.25',
        'euro_rate': '5.85'
    }

    return data

def phone_notify(date, weather, temperature, dollar, dollar_state, euro, euro_state):
    notification_name = f'Bom dia Lian ♥ ! Hoje é dia {date}'
    notification_title = f'Aqui estão as informações do dia'
    notification_body = (
        f'\nO tempo está {weather} ({temperature})' +
        f'\nO dólar {'caiu para' if dollar_state == 'decrease' else 'subiu para' if dollar_state == 'increase' else 'está em'} {str(dollar).replace('.', ',')}' +
        f' e o euro {'caiu para' if euro_state == 'decrease' else 'subiu para' if euro_state == 'increase' else 'está em'} {str(euro).replace('.', ',')}' +
        f'\nTenha um ótimo dia!'
    )

    command = f'~/.local/share/gnome-shell/extensions/gsconnect@andyholmes.github.io/service/daemon.js -d 45c542b0_25bf_43ec_8d48_1f31785b0649 --notification "{notification_title}" --notification-body "{notification_body}" --notification-appname "{notification_name}"'
    subprocess.run(command, shell=True, executable="/bin/bash")

def start_structure():
    """Starts all functionalities of the program
    such as the APIs, the data, day and weather
    then wraps them together"""
    ...

    # match case for dollar and euro state (for increase/decrease/stable)
    # match case for weather for each possible state
    phone_notify(
        date="30/08",
        weather="ensolarado", temperature="25ºC",
        dollar=5.25, dollar_state="decrease",
        euro=6.25, euro_state="decrease"
    )

if __name__ == '__main__':
    start_structure()
    #start_interface()