# Напишите функцию, которая разворачивает строку или возвращает
# пустую строку, если ей передали другой тип данных
def reverse(a):
    if type(a) is not str:
        return ''
    return a[::-1]
print(reverse(input()))
