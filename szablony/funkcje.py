import math


def pole_prostokata(a, b):
    return a*b


def pole_kwadratu(a):
    return a**2


def pole_trojkata(a, h):
    return (a*h)/2


def pole_trapezu(a, b, h):
    return 1/2*(a+b)*h


def pole_kola(r):
    return math.pi*r**2


print(pole_prostokata(2, 3))
print(pole_kwadratu(3))
print(pole_trojkata(2, 5))
print(pole_trapezu(3, 4, 2))
print(pole_kola(1))
