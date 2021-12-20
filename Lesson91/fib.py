#!/usr/bin/python3
#Написать функцию, которая возвращает заданное число
#Фибоначчи (рекурсия)

def func(n):
    '''Возвращает n-ое число Фибоначчи
    n - аргумент, номер числа Фибоначчи, n > 0
    '''
    if n < 1:
        return -1
    if n < 3:
        return 1
    else:
        return func(n-1) + func(n-2)
