import funkcje
import math

wybor = input("""co chcesz zrobić ?:
1. pole prostokata
2. pole kwadratu
3. pole trojkata
4. pole trapezu
5. pole kola
""")
if wybor == '1':
    a = float(input("Podaj wartoś a: "))
    b = float(input("Podaj wartość b: "))
    print(funkcje.pole_prostokata(a, b))
elif wybor == '5':
    r = float(input("podaj r: "))
    print(funkcje.pole_kola(r))
