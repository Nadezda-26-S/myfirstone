#______СтепановаНС________Урок 3-Списки.Словари.Кортежи.Множества__________

#file = open('C:\Users\Надежда\Documents\ПРОГРАММИРОВАНИЕ_статьи и материалы\Университет_ИИ\Курс_Python-разработчик\myfirstone\\text.txt')

# import pymorphy2
# morph = pymorphy2.MorphAnalyzer()
#from .analyzer import MorphAnalyzer

file = open(file='text.txt', mode='r', encoding='UTF-8')
text_dict = {}
#char = ('.', ',', ':', ';', '!', '&', '"', '"', '?', '(', ')', '-') \\ ?задать множеством?
for line in file:
    print ('ИСХОДНЫЙ ТЕКСТ: ', '\n', '', line)
    line = line.replace(',', ' ') #методами строк очистить текст от знаков препинания;
    line = line.replace('.', ' ')
    line = line.replace('/', ' ')
    line = line.replace('.', ' ')
    line = line.replace(':', ' ')
    line = line.replace(';', ' ')
    line = line.replace('!', ' ')
    line = line.replace('?', ' ')
    line = line.replace('«', ' ')
    line = line.replace('»', ' ')
    line = line.replace('-', ' ')
    line = line.replace('(', ' ')
    line = line.replace(')', ' ')
    if line == '\n': # чтобы выводил весь текст, а не первую строчку только
        continue
    print('\n', 'ТЕКСТ БЕЗ СИМВОЛОВ И ДО РАЗБИЕНИЯ В СЛОВАРЬ: ', '\n', line)
    line = line.split() #сформировать list со словами (split);
    print('\n', 'ТЕКСТ БЕЗ СИМВОЛОВ до приведения к нижнему регистру: ', '\n', '', line)
    line = list(map(lambda word: word.lower(), line)) #привести все слова к нижнему регистру (map);
# способ 2: line = [word.lower() for word in line]
    print('\n', 'ТЕКСТ БЕЗ СИМВОЛОВ, приведенный к нижнему регистру, СПИСКОМ: ', '\n', '', line)
# p = morph.parse([word])
    for word in line: #получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
        if word in text_dict:
            text_dict[word]['count'] +=1
        else:
            text_dict[word] = {'count': 1}
    print('\n', 'ТЕКСТ БЕЗ СИМВОЛОВ, приведенный к нижнему регистру, СПИСКОМ по частоте встречаемости слов: ', '\n', '', text_dict)
# i = ['count']
result_tuple = list(text_dict.items()) #вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
result_tuple.sort(key=lambda i: i[1]['count'], reverse=True)
# for key, value in text_dict.items():
#     print(key, value)
for i in range(5):
    print(result_tuple[i])
print(len(text_dict))


#мои шпоры
#MorphAnalyzer.parse()
# >>> p = morph.parse('стали')[0]
# >>> p.normalized
# Parse(word='стать', tag=OpencorporaTag('INFN,perf,intr'), normal_form='стать', para_id=879, idx=0, estimate=1.0)
# , 'normal_form': p.normal_form
