import requests


def compare_exchange(currency_today, currency_yesterday):
    if currency_today > currency_yesterday:
        return "increase"
    elif currency_today < currency_yesterday:
        return "decrease"
    else:
        return "stable"

def _get_exchange(date, currency):
    r = requests.get(f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date}/v1/currencies/{currency}.json")
    r = r.json()[f'{currency}']
    return r.get('brl')

def exchange_currencies(date_t, date_y):
    exchanges = []
    for i in [date_t, date_y]:
        _dollar = _get_exchange(i, 'usd')
        _euro = _get_exchange(i, 'eur')
        exchanges.append([_dollar, _euro])

    exchanges_dict = {
        "dollar_rate":f"{exchanges[0][0]}",
        "dollar_yesterday":f"{exchanges[1][0]}",
        "euro_rate":f"{exchanges[0][1]}",
        "euro_yesterday":f"{exchanges[1][1]}"
    }

    return exchanges_dict

if __name__ == "__main__":
    print(
        exchange_currencies('2024-08-31', '2024-08-30')
    )