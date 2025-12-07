number=int(input())
if 65<=number<=90:
    print (f"Код {number} соответствует заглавной букве '{chr(number)}'")
elif 97<=number<=122:
    print(f"Код {number} соответствует строчной английской букве '{chr(number)}'")
else:
    print(f"Код {number} cоответствует другому символу: '{chr(number)}'")

