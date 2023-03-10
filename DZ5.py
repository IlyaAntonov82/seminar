# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
#
# def f(A, B):
#     if (B == 1):
#         return (A)
#     if (B != 1):
#         return (A * f(A, B - 1))
# A = int(input('Введите число: '))
# B = int(input('Введите степень: '))
# print(f(A, B))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

a = int(input("Введите число А: "))
b = int(input("Введите число B: "))
def sum(a, b):
    return a if b == 0 else sum(a+1, b-1) if b > 0 else sum(a-1, b+1)
print(sum(a, b))
