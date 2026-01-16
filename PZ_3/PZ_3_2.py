# Вариант 8.
# Единицы длины:
# 1 — дециметр
# 2 — километр
# 3 — метр
# 4 — миллиметр
# 5 — сантиметр
# Даны номер единицы длины (1–5) и длина отрезка.
# Найти длину отрезка в метрах.

number_length = int(input("Введите номер единицы длины (1–5): "))
length = float(input("Введите длину отрезка: "))

# Перевод в метры
if number_length == 1:        # дециметр
    result = length / 10
elif number_length == 2:      # километр
    result = length * 1000
elif number_length == 3:      # метр
    result = length
elif number_length == 4:      # миллиметр
    result = length / 1000
elif number_length == 5:      # сантиметр
    result = length / 100
else:
    result = None

if result is None:
    print("Ошибка: номер единицы должен быть от 1 до 5.")
else:
    print("Длина отрезка в метрах:", result)
