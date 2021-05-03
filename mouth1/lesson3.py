
while True:
    try:
        s = input("Знак (+,-,*,/): ")
        x = float(input("Введи число"))
        y = float(input("Введи 2 число"))

    except ValueError:
        x = float(input("Нормально введи даа!!"))
        y = float(input("Введи 2 число"))
        s = input("Знак (+,-,*,/): ")

    if s == 'Stop':
        break
    if s in ('+', '-', '*', '/'):
        if s == '+':
            print( x+y)
        elif s == '-':
            print (x-y)
        elif s == '*':
            print (x*y)
        elif s == '/':
            if y != 0:
                print(x/y)
            else:
                print("Деление на ноль!")
    else:
        print ("Неверный знак операции!")
