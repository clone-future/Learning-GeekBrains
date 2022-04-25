# Даны два целых числа n и m (при этом n <= m). Напечатайте все числа n до m включительно.
n = int(input())
m = int(input())
for i in range(n, m + 1, 1):
    print(i)
