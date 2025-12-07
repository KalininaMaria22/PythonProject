def add_student():
    surname = input("Введите фамилию студента: ")
    email = input("Введите почтовый адрес: ")
    with open("2_MZ_4.txt", "w", encoding="utf-8") as file:
        file.write(f"{surname}: {email}\n")
    print("\nСодержимое файла:")
    with open("2_MZ_4.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
add_student()


