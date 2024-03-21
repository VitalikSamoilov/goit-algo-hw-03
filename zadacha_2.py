import random
while True:
    try:
        min = int(input("Введіть мінімальне число в наборі від 1 до 1000: "))
    except ValueError:
        print("Введіть число")
        continue
    else: 
        if min < 1:
            print("Введіть число більше 1")
            continue
        elif min > 1000:
            print("Введіть число менше 1000")
            continue
    try:        
        max = int(input("Введіть максимальне число в наборі не більше 1000: "))
    except ValueError:
        print("Введіть число")
        continue
    else:
        if max < min:
            print("Введіть число більше мінімального")
            continue
        elif max > 1000:
            print("Введіть число менше 1000")
            continue
    try:
        quantity = int(input("Введіть кількість чисел які потрібно вибрати: "))
    except ValueError:
        print("Введіть число")
        continue
    else:
        if quantity < min:
            print("Введіть число в заданому діапазоні")
            continue
        elif quantity > max:
            print("Введіть число в заданому діапазоні")
            continue
    get_numbers_ticket = set()
    while len(get_numbers_ticket) < quantity:
        get_numbers_ticket.add(random.randint(min, max))
    listt = list(get_numbers_ticket)
    listt.sort()
    print(listt)
    break