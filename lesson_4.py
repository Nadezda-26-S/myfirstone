#______СтепановаНС________Урок 4-ФУНКЦИИ__________

# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка
#(могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);
import random

list_names = ['Roma', 'Artur', 'Zena', 'Dima', 'Andrey', 'Sergey', 'Yaroslav', 'Nina', 'Diego', 'Javex', 'Lobo', 'German', 'Maxx', 'Kris', 'Misha', 'Masha', 'Maksim', 'Arkadiy', 'Boris', 'Robert']
# global N = 100

random.shuffle(list_names)
print(list_names)
n = 100
len_list = 100   # !!! НЕ ПОНЯТНО ПРО ДЛИНУ СПИСКА ?
def func(list_names,len_list):
    return ramdom(list_names, n=len_list)
print(func(list_names, len_list))

# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
list_names_sort = sorted(list_names)
print(list_names_sort)

def most_frequent(list_names):
    counter = 0
    num = list_names[0]
    for i in list_names:
        curr_frequency = list_names.count(i)
        if (curr_frequency>counter):
            counter = curr_frequency
            num = i
    return num
print(most_frequent)

list_names = ['Roma', 'Artur', 'Zena', 'Dima', 'Andrey', 'Sergey', 'Yaroslav', 'Nina', 'Diego', 'Javex', 'Lobo', 'German', 'Maxx', 'Kris', 'Misha', 'Masha', 'Maksim', 'Arkadiy', 'Boris', 'Robert']

# ещё способ
from collections import Counter
def new_most_frequent(list_names):
    occurence_count = Counter(list_names)
    return occurence_count.most_common(1)[0][0]
print(new_most_frequent)

# ещё способ
def new_most_frequent_2(list_names):
    dict = {}
    count, itm = 0, ''
    for item in reversed(list_names):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count:
            count, itm = dict[item], item
    return (itm)
print(new_most_frequent_2(list_names))

# def most_frequent(names):
#     word = {}
#     for name in names:
#         word[name] = word.get(name, 0) + 1
#     word = list(word.items())
#     word.sort(key=lambda x: x[1], reverse=True)
#     return word[0][0]

# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
def most_frequent(list_names):
    letters = {}
    for name in list_names:
        for char in name:
            letters[char] = letters.get(char, 0) + 1
        letters = sorted(list(letters.items()), lambda x: x[1])
    return letters [0][0]
#min(set(list_names), key = list_names.count)
print(most_frequent(list_names))
