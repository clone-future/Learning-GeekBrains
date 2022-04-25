import json


def read_entire_file(path2file):
    text = open(path2file, 'r').read()
    print(text)

    return 0


# read_entire_file('sample.txt')


def read_first_n_lines(path2file, n):
    text = open(path2file, 'r').readlines()
    for i in range(n):
        print(text[i])

    return 0


# read_first_n_lines('sample.txt', 2)


def add_end_to_file(path2file):
    this_file = open(path2file, 'a')
    this_file.write('\nEND OF FILE')
    this_file.close()

    return 0


# add_end_to_file('sample.txt')


def text2list(path2file):
    lines = list(open(path2file, 'r').readlines())
    return lines


# print(text2list('sample.txt'))


def longest_line(path2file):
    lines = list(open(path2file, 'r').readlines())
    return max(lines, key=len)


# print(longest_line('sample.txt'))


def add_info_to_file(path2file):
    file = open(path2file, 'r+')
    text = file.read()
    text = text.replace('\n', ' ')
    words = tokenize(text)
    words_count = len(words)
    diferent_count = len(set(words))
    file = write_to_file(file, [words_count, diferent_count])
    print(words)
    print(set(words))
    file.close()

    return 0


def tokenize(text):
    words = text.split()

    return words


def write_to_file(file, info):
    file.write('\n\nКоличество слов в тексте: {} \nКоличество различных слов в тексте: {}'.format(info[0], info[1]))
    file.close()

    return file


# add_info_to_file('sample.txt')


def get_names_from_json(path2file):
    file = open(path2file, 'r')
    data = json.load(file)
    file.close()
    names = list(data)

    return names


# print(*get_names_from_json('sample.json'))


def convert_marks(path2file):
    file = open(path2file, 'r')
    data = json.load(file)
    file.close()
    newdict = {}
    for i in data:
        if data[i] == 'A':
            rate = 5
        elif data[i] == 'B':
            rate = 4
        elif data[i] == 'C':
            rate = 3
        else:
            rate = 2
        newdict.update({i: rate})
    new_file = open('digit_marks.json', 'w')
    json.dump(newdict, new_file)
    new_file.close()

    return 0


convert_marks('sample.json')
