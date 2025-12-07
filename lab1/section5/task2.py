decimal_number=int(input("Введите десятичное число: "))
if decimal_number==0:
    binary_number="0"
else:
    binary_number=""
    num=decimal_number

    while num>0:
        remainder=num%2
        binary_number=str(remainder)+binary_number
        num=num//2
print(f"Десятичное число: {decimal_number}")
print(f"Двоичное представление: {binary_number}")

