# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Сначала на ввод передается n - число стран, затем n строк
# (слова в строке разделены пробелами, первое слово в строке - название страны,
# остальные города, которые в ней находятся). Потом передается m - число городов,
# для которых надо вывести страну, затем каждый город на новой строке.
# Подсказка: воспользуйтесь структурой dict

cnt = int(input())
ct = {}
towns = set()
towns_check = list()
for i in range(cnt):
    country_towns = input().split()
    country = country_towns[0]
    towns = country_towns[1:len(country_towns) + 1]
    ct[country] = towns

cnt_check = int(input())
for i in range(cnt_check):
    towns_check.append(input())

for check in towns_check:
    for c, t in ct.items():
        if check in t:
            print(c)
