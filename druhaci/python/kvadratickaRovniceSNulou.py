import math

a = 0
b = 3
c = 7

d = pow(b, 2) - 4 * a * c


if d == 0:
    x0 = -b / (2 * a) if a != 0 else 0
    print("Rovnice má jedno řešení x1 =", x0)

elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a) if a != 0 else 0
    x2 = (-b - math.sqrt(d)) / (2 * a) if a != 0 else 0
    print("Rovnice má dvě řešení x1 =", x1, "a x2 =", x2)

elif d < 0:
    print("Rovnice nemá řešení v reálném oboru čísel.")