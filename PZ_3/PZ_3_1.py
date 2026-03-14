#  Вариант 8.
#  Даны два целых числа: A, B.
#  Проверить истинность высказывания: «Каждое из чисел A и B нечетное».

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print("Неправильно ввели!")
        A = input("Введите число A: ")

while type(B) != int:
    try:
        B = int(B)
    except ValueError:
        print("Неправильно ввели!")
        B = input("Введите число B: ")

result = (A % 2 != 0) and (B % 2 != 0)

print("Оба числа нечётные:", result)