import random

def cowbull(num_digits):
    randomnum = [random.randint(0, 9) for n in range(num_digits)]
    print("Выйгрышный код = " + str(randomnum))

    count = 0
    while True:
        count += 1
        print("Угадай: " + str(count))
        print("Введи " + str(num_digits) + "-Цыфры: ")
        guess = [int(i) for i in str(input())]

        if guess == randomnum:
            print("Ты выйграл.")
            print("Это заняло тебя "+str(count)+" хода.")
            break

        else:
            cow = 0
            bull = 0

            for x in range(0, num_digits):
                if guess[x] == randomnum[x]:
                    cow += 1
                elif guess[x] in randomnum:
                    bull += 1

        print("Коров: "+str(cow)+" Быков: "+str(bull))

cowbull(4)

