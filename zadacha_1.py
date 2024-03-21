from datetime import datetime
while True:
    date = input("Введіть дату: ")
    try:    
        date_datetime = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Введіть дату в форматі РРРР-ММ-ДД")
    else:
        data_today = datetime.now()
        defference_date = data_today - date_datetime
        print(f"{defference_date.days} дня")
        break