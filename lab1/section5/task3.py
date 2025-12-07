import math
def rectangle_area(a,b):
    print("Вычисляем площадь прямоугольника")
    area=a*b
    return area
def circle_area(a):
    print("Вычисляем полощадь круга")
    area=math.pi*a**2
    return area
def triangle_area(a,h):
    print("Вычисляем площадь треугольника")
    area=0.5*a*h
    return area
print("Площадь чего вы хотите найти?\n1 - Прямоугольник\n2 - Круг\n3 - Треугольник")
choice = input("Введите номер фигуры (1-3): ")
if choice == '1':
    a = float(input("Введите длину прямоугольника: "))
    b = float(input("Введите ширину прямоугольника: "))
    result = rectangle_area(a, b)
    print(f"Площадь прямоугольника: {result}")

elif choice == '2':
    a = float(input("Введите радиус круга: "))
    result = circle_area(a)
    print(f"Площадь круга: {result}")

elif choice == '3':
    a = float(input("Введите основание треугольника: "))
    h = float(input("Введите высоту треугольника: "))
    result = triangle_area(a, h)
    print(f"Площадь треугольника: {result}")

else:
    print("Неверный выбор. Пожалуйста, введите число от 1 до 3.")