end = int(input("Введите число которое мы будем щитать с 1 до вашего числа: "))

for number in range(end, 0, -1):
    if number % 2 == 0:
        print(number, end=' ')