def trojkat(bok_a, bok_b, bok_c, wysokosc_a):
    obwod = bok_a + bok_b + bok_c
    pole = (bok_a * wysokosc_a) / 2
    return obwod, pole


# kwadrat, prostokat dla studenta 1 (próba druga)
def kwadrat(bok):
    obwod1 = 4*bok
    pole1 = bok*bok
    return obwod1, pole1


def prostokat(bok_a, bok_b):
    obwod2 = 2*bok_a+2*bok_b
    pole2 = bok_a*bok_b
    return obwod2, pole2

# rownoleglobok i romb dla studenta 2
def rownoleglobok(bok_a, bok_b, wysokosc_a):
    # TODO
    return 0, 0

def romb(bok, wysokosc):
    # TODO
    return 0, 0

# trapez i kolo dla studenta 3
def trapez(bok_a, bok_b, bok_c, bok_d, wysokosc_a):
    # TODO
    return 0, 0


def kolo(promien):
    # TODO
    return 0, 0


# assert trojkat(10, 15, 16, 8) == (41, 40)
# assert kwadrat(20) == (80, 400)
# assert prostokat(12, 10) == (44, 120)
# assert rownoleglobok(6, 5, 2) == (22, 12)
# assert romb(10, 5) == (40, 50)
# assert trapez(10, 15, 7, 14, 2) == (45, 25)
# TODO na koniec! dopisz 2 testy dla kola i dla kazdej innej figury po jednym dodatkowym tescie