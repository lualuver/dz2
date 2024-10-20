end = int(input("Введите число для факториала: "))

faktorial = 1


for number in range(1, end+1):
    faktorial *= number

print(faktorial)
