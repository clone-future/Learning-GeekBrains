# Напишите функцию min4(a, b, c, d), вычисляющую минимум четырех чисел,
# которая не содержит конструкции if, а использует стандартную функцию min от двух чисел.
# Считайте четыре целых числа и выведите их минимум.
min4 = lambda a, b, c, d: min(min(a, b), min(c, d))
print(min4(int(input()), int(input()), int(input()), int(input())))
