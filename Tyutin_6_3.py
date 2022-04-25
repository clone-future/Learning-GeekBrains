# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Сначала на ввод передается n - число стран, затем n строк
# (слова в строке разделены пробелами, первое слово в строке - название страны,
# остальные города, которые в ней находятся). Потом передается m - число городов,
# для которых надо вывести страну, затем каждый город на новой строке.
# Подсказка: воспользуйтесь структурой dict
def contry_towns_check(cnt=int(input("Введите число стран:")), cnt_check=int(input("Введите число городов:"))):
    ct = {}
    towns_check = list()
    res = []
    for i in range(cnt):
        country_towns = input(f"Введите {i+1}-ю из {cnt} строк вида 'страна_города':").split()
        country = country_towns[0]
        towns = country_towns[1:len(country_towns) + 1]
        ct[country] = towns

    for i in range(cnt_check):
        towns_check.append(input(f"Введите {i+1}-й из {cnt_check} городов:"))

    for check in towns_check:
        for c, t in ct.items():
            if check in t:
                res.append(c)
    return res


print(*contry_towns_check(), sep='\n')
