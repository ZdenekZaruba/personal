import math

a = 2
b = -11
c = 14

d = pow(b, 2) - 4 * a * c


if d == 0:
    x0 = -b / (2 * a)
    print("Rovnice má jedno řešení x1 =", x0)

elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("Rovnice má dvě řešení x1 =", x1, "a x2 =", x2)

elif d < 0:
    print("Rovnice nemá řešení v reálném oboru čísel.")