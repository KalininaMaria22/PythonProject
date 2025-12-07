height=int(input('Введите высоту ёлки: '))
symbol=input("Введите символ: ")
print(" "*(height),"||")

for i in range(1,height-1):
    print(" "*(height-i-1),symbol*i,"||",symbol*i)
print(" "*(height),"||")