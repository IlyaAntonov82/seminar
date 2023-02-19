# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2


# n = int(input('Введите количество монет: '))
# count = 0
# for i in range(n):
#     coin = int(input('Введите значение 1 - "решка" или 0 - "герб": '))
#     count += coin
#     i += 1
# if count <= n//2:
#     print('Минимальное количество монет, которые нужно перевернуть ', count)
# else:
#     print('Минимальное количество монет, которые нужно перевернуть ', n - count)



# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

# total = int(input('Сумма задуманных чисел S равна '))
# product = int(input('Произведение задуманных чисел P равно '))
# flag = False
# for i in range(1, 1001):
#     for j in range(1, 1001):
#         if i + j == total and i * j == product:
#             flag = True
#             x = i
#             y = j
#         j += 1
#     i += 1
# if flag:
#     print('Петя задумал числа {} и {}.'.format(x, y))
# else:
#     print('Увы, Петя ошибся, такие целые числа невозможно подобрать.')


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8


finish = int(input('Введите N = '))
i = 0
while 2**i <= finish:
    print(2**i, end=' ')
    i += 1