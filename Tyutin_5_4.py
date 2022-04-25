# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке
# (то есть раньше по алфавиту). Подсказка:
# разбить строку на слова можно с помощью оператора split с разделением по
# пробелу строки можно сравнивать с помощью оператора >.
# dog cat monkey cat monkey monkey cat
main_string = input().split()
string_set = sorted(set(main_string))
words_cnt = {}
for i in string_set:
    for k in main_string:
        if i == k:
            words_cnt[i] = int(words_cnt.get(i, 0) + 1)
j = 0
result_words = list()
for w, c in words_cnt.items():
    if c > j:
        j = c
        result_words.clear()
        result_words.append(w)
    elif c == j:
        result_words.append(w)
print(sorted(result_words)[0])
