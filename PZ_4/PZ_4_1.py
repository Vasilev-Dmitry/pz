# Вариант 8.
# Даны два целых числа A и B (A < B).
# Найти сумму квадратов всех целых чисел от A до B включительно.

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

# Сумма квадратов от A до B
sum_squares = 0
for i in range(A, B + 1):
    sum_squares += i * i

print("Сумма квадратов чисел от A до B:", sum_squares)