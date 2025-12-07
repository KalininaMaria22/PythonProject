students_2_MZ_4=['Атрощенко','Безуглова','Горбачева','Деревицкий','Каратаева','Коробков','Кудрявцева','Лаптев','Мешков','Овчинников']
students_2_MZ_2=['Баркалов','Васильева','Калинина','Ленина','Ларионова','Солдатенко','Солопов','Вишневская','Садовничая','Салимова']
sports_team=tuple(students_2_MZ_4[3:8]+students_2_MZ_2[5:10])
print("Группа 2-МЗ-4: ",students_2_MZ_4)
print("Группа 2-МЗ-2: ",students_2_MZ_2)
print("Спортивная команда: ",sports_team)
print("Человек в команде: ",len(sports_team))
sorted_sports_team = tuple(sorted(sports_team))
print(sorted_sports_team)
if "Иванов" in sports_team:
    count=sport_team.count("Иванов")
    print(f"Фамилия Иванов встречается {count} раз")
else:
    print("Студент Иванов не входит в команду")

