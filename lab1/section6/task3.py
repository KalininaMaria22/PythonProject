import operator
precipitation = {'Январь': 60, 'Февраль': 30, 'Март': 35,'Апрель': 60, 'Май': 85, 'Июнь': 70,'Июль': 90, 'Август': 80,
    'Сентябрь': 55, 'Октябрь': 50, 'Ноябрь': 40, 'Декабрь': 48}
months_list = list(precipitation.items())
months_list.sort(key=operator.itemgetter(1))
for month, rain in months_list:
    print(f"{month} - {rain} мм")

