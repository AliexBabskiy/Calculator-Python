import math
print("Добро пожаловать. Нажмите на Enter клавишу для запуска калькулятора.")
input()
print("Список действий:")
print("1. Сложить 2 числа")
print("2. Вычесть первое из второго")
print("3. Перемножить два числа")
print("4. Разделить первое на второе")
print("5. Возвести в степень N первое число")
print("6. Найти квадратный корень из числа")
print("7. Найти факториал из числа")
print("8. Найти синус")
print("9. Найти косинус")
print("10. Найти тангенс")
print("0. Выйти из программы\n")
while True:
    choice = input("Выберите действие: ")
    if choice == '1':
        print("Действие: сложение двух чисел \n")
        while True:
            try:
                num1 = int(input("Введите первое число: "))
                break
            except ValueError:
                print("Ошибка, введено некорректное значение ")
        while True:
            try:
                num2 = int(input("Введите второе число: "))
                break
            except ValueError:
                print("Ошибка, введено некорректное значение ")
        result = num1 + num2
    elif choice == '2':
        print("Действие: вычесть первое число из второго \n")
        while True:
            try:
                num1 = int(input("Введите первое число: "))
                break
            except ValueError:
                print("Ошибка, введено некорректное значение ")
        while True:
            try:
                num2 = int(input("Введите второе число: "))
                break
            except ValueError:
                print("Ошибка, введено некорректное значение ")
        result = num1 - num2
    elif choice == '3':
        print("Действие: перемножить два числа \n")
        while True:
            try:
                num1 = int(input("Введите первое число: "))
                break
            except ValueError:
                print("Ошибка, введено некорректное значение ")
        while True:
            try:
                num2 = int(input("Введите второе число: "))
                break
            except ValueError:
                print("Ошибка, введено некорректное значение ")
        result = num1 * num2
    elif choice == '4':
        print("Действие: Разделить первое на второе \n")
        while True:
            try:
                num1 = int(input("Введите первое число: "))
                break
            except ValueError:
                print("Ошибка, введено некорректное значение ")
        exit = False
        while exit == False:
            while True:
                try:
                    num2 = int(input("Введите второе число: "))
                    break
                except ValueError:
                    print("Ошибка, введено некорректное значение ")
            if num2 != 0:
                result = num1 / num2
                exit = True
            else:
                print("Ошибка: делить на 0 нельзя.")
        exit = False
    elif choice == '5':
        print("Действие: возвести в степень N первое число \n")
        while True:
            try:
                num1 = int(input("Введите первое число: "))
                break
            except ValueError:
                print("Ошибка, введено некорректное значение ")
        num2 = int(input("Введите степень: "))
        while True:
            try:
                num2 = int(input("Введите степень: "))
                break
            except ValueError:
                print("Ошибка, введено некорректное значение ")
        result = num1 ** num2
    elif choice == '6':
        print("Действие: найти квадратный корень из числа \n")
        exit = False
        while exit == False:
            while True:
                try:
                    num1 = int(input("Введите число: "))
                    break
                except ValueError:
                    print("Ошибка, введено некорректное значение ")
            if num1 > 0:
                result = math.sqrt(num1)
                print("Ошибка: квадратный корень отрицательного числа.")
            else:
                print("Ошибка: квадратный корень отрицательного числа.")
        exit = False
    elif choice == '7':
        print("Действие: найти факториал из числа \n")
        exit = False
        while exit == False:
            while True:
                try:
                    num1 = int(input("Введите число: "))
                    break
                except ValueError:
                    print("Ошибка, введено некорректное значение ")
            if num1 >= 0:
                result = math.factorial(int(num1))
                exit = True
            else:
                print("Ошибка: факториал отрицательного числа.")
        exit = False
    elif choice == '8':
        print("Действие: нахождение sin \n")
        while True:
            try:
                num1 = int(input("Введите число: "))
                break
            except ValueError:
                print("Ошибка, введено некорректное значение ")
        result = math.sin(num1)
    elif choice == '9':
        print("Действие: нахождение cos \n")
        while True:
            try:
                num1 = int(input("Введите число: "))
                break
            except ValueError:
                print("Ошибка, введено некорректное значение ")
        result = math.cos(num1)
    elif choice == '10':
        print("Действие: нахождение tg \n")
        while True:
            try:
                num1 = int(input("Введите число: "))
                break
            except ValueError:
                print("Ошибка, введено некорректное значение ")
        result = math.tan(num)
    elif choice == '0':
        print("Завершение работы.")
        break
    else:
        print("Ошибка: Неправильный выбор операции.")
        continue
    print("Ответ: " + str(result))