# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Сколько монеток на столе? '))
# Здесь я бы создала список из n элементов, который состоял бы из 0 и 1
# 1 - решка  0 - орел

reshka = 0
orel = 0
for i in range :
    if (i == 1) :
        reshka =+ 1
        i += 1
    else : orel =+ 1
    i += 1

if (reshka < orel):
    print(reshka)
else : (orel)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать.Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

S = int(input('Петя, назови сумму чисел : '))
P = int(input('Петя, назови произведение чисел : '))

for i in range(S) :
    for j in range(P) :
        if S == i + j and P == i * j:
            print(i , j)


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
a = 1
n = int(input("N = "))
while 2 ** a <= n :
    print(2 ** a)
    a += 1
