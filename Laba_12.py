'''Вычислить сумму знакопеременного ряда |х^n|/n!, где х-матрица ранга к (к и матрица задаются случайным образом),
n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
У алгоритма д.б. линейная сложность. Знак первого слагаемого  -'''

import random
import numpy as np
from decimal import Decimal, getcontext


def sum(current_x, first_x, t):
    n = 1
    det = np.linalg.det(current_x)
    factorial = 1
    res = 0

    while True:
        curr_term = Decimal(det / factorial)

        if abs(curr_term) < 1 / (10 ** t):
            break

        res += curr_term

        n += 1
        factorial *= -n
        current_x *= first_x

    return res


def gen_matrix():
    k = random.randint(2, 10)
    current_x = np.random.randint(-1, 2, (k, k))
    if abs(np.linalg.det(current_x)) == 0:
        return gen_matrix()
    else:
        return current_x


print("Введите число t:")
try:
    t = int(input())
    while t < 1:
        t = int(input("Ведите число t, большее или равное 1:\n"))
    print()
except ValueError:
    print('Для работы программы нужно было ввести число')
    exit()

current_x = gen_matrix()
first_x = current_x

print("Сгенерированная матрица")
print(first_x)
print('__________________________')

getcontext().prec = t
result = sum(current_x, first_x, t)

print(f"Сумма ряда |х^n|/n! с точностью {t} знаков после запятой: {result:.{t}f}".rstrip('0').rstrip('.'))
