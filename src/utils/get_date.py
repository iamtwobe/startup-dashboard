from datetime import datetime, timedelta


def get_date():
    try:
        weekdays = (
            "monday", "tuesday", 
            "wednesday", "thursday",
            "friday", "saturday",
            "sunday"
        )

        _date = datetime.now()
        today = _date.strftime("%Y-%m-%d")
        yesterday = (_date - timedelta(days=1)).strftime("%Y-%m-%d")
        weekday = _date.weekday()
        daytime = _date.strftime("%H")

        return today, yesterday, weekdays[weekday], daytime
    except Exception as e:
        print(e)
        return None

if __name__ == "__main__":
    print(
        get_date()
    )