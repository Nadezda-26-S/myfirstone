#Задачи на циклы и оператор условия_Урок-2
'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
print ('Task 1')
i = 0
while i < 5:
    i = i+1
    print (i, '00000')
print (''*2)
for i in range(1,6):
    print(i, '000')
print (''*2)
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
print ('Task 2')
#HEEEEEELLLLPPPP: Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
amo = 0
#for i in range(11):
n = int(input('Введите 10 цифр: '))
#for '5' in n:
#for n % 10 // 10 == 5:
#if n // 5 == 1:
if n % 10 == 5:
    amo += 1
    #continue
print ('Количество цифр 5 равно ', amo)
print (''*2)
'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
print ('Task 3')
sum = 0
for i in range(1,101):
    sum+=i
print(sum)
print (''*2)
'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
print ('Task 4')
multi = 1
for i in range(1,11):
    multi*=i
print(multi)
print (''*2)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
#ЧТО ЗДЕСЬ ПРОИСХОДИТ?
print ('Task 5')
integer_number = 7853247
while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10
    if integer_number>1:
        break
print (integer_number)
#print (*integer_number[::-1], sep='\n')
print (''*2)
'''
Задача 6
Найти сумму цифр числа.
'''
print ('Task 6')
n = 6574
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
print(sum)
print (''*2)
'''
Задача 7
Найти произведение цифр числа.
'''
print ('Task 7')
n = 6574
multi = 1
while n > 0:
    multi *= n % 10
    n //= 10
print(multi)
print (''*2)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
print ('Task 8')
n = 834627345
while n>0:
    if n%10 == 5:
        print('Yes')
        break
    n = n//10
else: print('No')
print (''*2)
'''
Задача 9
Найти максимальную цифру в числе
'''
#ПОЧЕМУ ЗДЕСЬ ОСТАНАВЛИВАЕТСЯ ПРОГРАММА?
print ('Task 9')
n = 9227546
n = int(n)
max = 0
while n > 0:
   if n%10 > max:
       max = n%10
       n //= 10
print(max)
print (''*2)
'''
Задача 10
Найти количество цифр 5 в числе
'''
print ('Task 10')
amo = 0
n = 785424675
#ptint(str(n).count('5'))
if n % 10 == 5:
#if n % 5 == 1:
    n//=10
    amo += 1
print ('Количество цифр 5 в числе равно ', amo)