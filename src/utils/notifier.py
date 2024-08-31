import subprocess

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

if __name__ == "__main__":
    phone_notify(
        date="30/08",
        weather="ensolarado", temperature="25ºC",
        dollar=5.25, dollar_state="decrease",
        euro=6.25, euro_state="decrease"
    )