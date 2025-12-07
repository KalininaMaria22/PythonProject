a=int(input("Введите число A:"))
b=int(input("Введите число B:"))
if a<b:
    print("Последовательность чисел в порядке возрастания:")
    for i in range(a,b+1):
        print(i)
else:
    print("Последовательность чисел в порядке убывания:")
    for i in range(a,b-1,-1):
        print(i)