# Напишите программу, которая посчитает сумму всех четных чисел из списка,
# переданного на вход, и прибавит к этому сумму всех чисел,
# которые стоят на местах с нечетными индексами
my_list = input().split()
c = 0
odd_id = 0
even_number = 0
for k in my_list:
    if c % 2 != 0:
        odd_id = odd_id + int(k)
    if int(k) % 2 == 0:
        even_number = even_number + int(k)
    c += 1
print(odd_id + even_number)
