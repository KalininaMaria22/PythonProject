import random
number=random.randint(1,10)
attempts=3
for attempt in range(1,attempts+1):
    guess=int(input(f"Попытка {attempt}. Введите число от 1 до 10: "))
    if guess==number:
        print("Ура! Вы угадали")
        break
    else:
        print("Не угадали")
else:
    print(f"К сожалению, Вы проиграли. Загаданное число: {number}")

