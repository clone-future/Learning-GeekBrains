# Напишите программу, которая находит в списке чисел элемент, самый
# близкий по величине к данному числу, если таких несколько выведите любое
my_list = input().split()
check = int(input())
i = 0
x = 0
c = 0
j = 0
res = 0
for n in my_list:
    if int(n) > check:
        i = int(n) - check
    else:
        i = check - int(n)
    if c == 0:
        x = i
    if i < x:
        x = i
        j = c
    c += 1
print(my_list[j])
