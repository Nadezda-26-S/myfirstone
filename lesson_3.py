#______СтепановаНС________Урок 3-Списки.Словари.Кортежи.Множества__________

#file = open('C:\Users\Надежда\Documents\ПРОГРАММИРОВАНИЕ_статьи и материалы\Университет_ИИ\Курс_Python-разработчик\myfirstone\\text.txt')

file = open(file='text.txt', mode='r', encoding='UTF-8')
text_dict = {}
#char = ('.', ',', ':', ';', '!', '&', '"', '"', '?', '(', ')', '-') \\ ?задать множеством?
for line in file:
        print ('ИСХОДНЫЙ ТЕКСТ: ', '\n', line)
        line = line.replace(',', ' ') #методами строк очистить текст от знаков препинания;
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
        print('ТЕКСТ БЕЗ СИМВОЛОВ И ДО РАЗБИЕНИЯ В СЛОВАРЬ: ', '\n', line)
        line = line.split() #сформировать list со словами (split);
        print('ТЕКСТ БЕЗ СИМВОЛОВ до приведения к нижнему регистру: ', '\n', line)
        line = list(map(lambda word: word.lower(), line)) #привести все слова к нижнему регистру (map);
# способ 2: line = [word.lower() for word in line]
        print('ТЕКСТ БЕЗ СИМВОЛОВ, приведенный к нижнему регистру, СПИСКОМ: ', '\n', line)
        for word in line: #получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
            if word in text_dict:
                text_dict[word]['count'] +=1
            else:
                text_dict[word] = {'count': 1}
        print('ТЕКСТ БЕЗ СИМВОЛОВ, приведенный к нижнему регистру, СПИСКОМ по частоте встречаемости слов: ', '\n', text_dict)
        result_tuple = list(text_dict.items()) #вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
        result_tuple = result_tuple.sort(lambda i: i['count'], line)
        i = ['count']
        for key, value in text_dict.items():
            print(key, value)
        for i in range(5):
            print(result_tuple(i))


