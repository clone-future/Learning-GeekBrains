# Напишите функцию, принимает на вход список слов и возвращает только те слова, которые являются палиндромом
# Пример ввода:
# level madam car lake stats
# Вывод программы:
# level madam stats
def pal(a):
    res = []
    for i in a.split():
        if i == i[::-1]:
            res.append(i)
    return res


print(*pal('level madam car lake stats'))
