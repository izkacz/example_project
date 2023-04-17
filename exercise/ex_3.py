def trojkat(bok_a, bok_b, bok_c, wysokosc_a):
    obwod = bok_a + bok_b + bok_c
    pole = (bok_a * wysokosc_a) / 2
    return obwod, pole


# kwadrat, prostokat dla studenta 1
def kwadrat(bok):
    obwod = 4*bok
    pole = bok**2
    return obwod, pole


def prostokat(bok_a, bok_b):
    obwod = (2*bok_a)+(2*bok_b)
    pole = bok_a*bok_b
    return obwod, pole

# rownoleglobok i romb dla studenta 2
def rownoleglobok(bok_a, bok_b, wysokosc_a):
    obwod = 2*bok_a + 2*bok_b
    pole = bok_a*wysokosc_a
    return obwod, pole


def romb(bok, wysokosc):
    obwod = 4*bok
    pole = bok*wysokosc
    return obwod, pole

# trapez i kolo dla studenta 3
def trapez(bok_a, bok_b, bok_c, bok_d, wysokosc_a):
    obwod = bok_a + bok_b + bok_c + bok_d
    pole = ((bok_a + bok_b) * wysokosc_a)/ 2
    return obwod, pole


def kolo(promien):
    import math
    pi_zmienna = math.pi
    obwod = 2 * promien * pi_zmienna
    pole = pi_zmienna * promien**2
    return obwod, pole

import math
assert trojkat(10, 15, 16, 8) == (41, 40)
assert trapez(10, 15, 7, 14, 2) == (46, 25)
assert kolo(2) == (4*math.pi, 4*math.pi)
assert trojkat(6, 7, 10, 5) == (23, 15)
assert trapez(20, 17, 12, 8, 6) == (57, 111)
assert kolo(3) == (6*math.pi, 9*math.pi)
assert kwadrat(20) == (80, 400)
assert kwadrat(10) == (40, 100)
assert prostokat(12, 10) == (44, 120)
assert prostokat(6, 8) == (28, 48)
assert rownoleglobok(6, 5, 2) == (22, 12)
assert rownoleglobok(15, 8, 3) == (46, 45)
assert romb(10, 5) == (40, 50)
assert romb(13, 7) == (52, 91)
