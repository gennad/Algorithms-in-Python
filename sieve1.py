#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sieve1(n):
    a = [0] * n # создание массива с n количеством элементов
    for i in range(n): # заполнение массива ...
        a[i] = i # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2 # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n: # перебор всех элементов до заданного числа
        if a[m] != 0: # если он не равен нулю, то
            j = m * 2 # увеличить в два раза (текущий элемент простое число)
            while j < n:
                a[j] = 0 # заменить на 0
                j = j + m # перейти в позицию на m больше
        m += 1

    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    print (b)

def sieve2(n):
    primes = [i for i in range(1, n+1)]
    primes[0] = 0

    for i in xrange(0, n):
        if primes[i] != 0:
            for j in xrange(i+primes[i], n, primes[i]):
                primes[j] = 0

    lst = [x for x in primes if x != 0]
    print lst


if __name__ == '__main__':
    sieve1(50)
    sieve2(50)
