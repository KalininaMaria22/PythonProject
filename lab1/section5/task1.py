def factorial_sum(n):
    total=0
    factorial=1
    for i in range(1,n+1):
        factorial*=i
        total+=factorial
    print(f"Сумма всех факториалов={total}")
n=int(input("Введите n:"))
factorial_sum(n)

