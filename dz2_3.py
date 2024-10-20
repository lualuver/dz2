import random



def guess_number():
    attempts = 0
    secret_number = random.randint(1,10)
    while attempts < 3:
        attempts += 1
        guess = int(input("Угадайте число от 1 до 10 :"))
        if guess < secret_number:
            print("Больше")
        elif guess > secret_number:
            print("Меньше")
        else:
            print("Вы угадали число!")
            break

guess_number()