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
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        result = num1 + num2
    elif choice == '2':
        print("Действие: вычесть первое число из второго \n")
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        result = num1 - num2
    elif choice == '3':
        print("Действие: перемножить два числа \n")
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        result = num1 * num2
    elif choice == '4':
        print("Действие: Разделить первое на второе \n")
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        while True:
            num2 = int(input("Введите второе число: "))
            if num2 == 0:
                print("Ошибка: делить на 0 нельзя.")
                continue
        result = num1 / num2
    elif choice == '5':
        print("Действие: возвести в степень N первое число \n")
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите степень: "))
        result = num1 ** num2
    elif choice == '6':
        print("Действие: найти квадратный корень из числа \n")
        while True:
            num1 = int(input("Введите число: "))
            if num1 <= 0:
                print("Ошибка: квадратный корень отрицательного числа.")
                continue
        result = math.sqrt(num1)
    elif choice == '7':
        print("Действие: найти факториал из числа \n")
        while True:
            num1 = int(input("Введите число: "))
            if num1 < 0:
                print("Ошибка: факториал отрицательного числа.")
                continue
        result = math.factorial(int(num1))
    elif choice == '8':
        print("Действие: нахождение sin \n")
        num1 = int(input("Введите число: "))
        result = math.sin(num1)
    elif choice == '9':
        print("Действие: нахождение cos \n")
        num1 = int(input("Введите число: "))
        result = math.cos(num1)
    elif choice == '10':
        print("Действие: нахождение tg \n")
        num1 = int(input("Введите число: "))
        result = math.tan(num)
    elif choice == '0':
        print("Завершение работы.")
        break
    else:
        print("Ошибка: Неправильный выбор операции.")
        continue
    print("Ответ: " + str(result))