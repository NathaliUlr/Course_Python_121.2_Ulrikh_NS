def month_to_season(month_number):
    if month_number in [12, 1, 2]:
        print('Зима')
    elif month_number in [3, 4, 5]:
        print('Весна')
    elif month_number in [6, 7, 8]:
        print('Лето')
    elif month_number in [9, 10, 11]:
        print('Осень')
    else:
        print('Неверный номер месяца')


month_to_season(6)
