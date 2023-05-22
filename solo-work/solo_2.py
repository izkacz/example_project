import math


class Trojkat:
    def __init__(self, a, b, c, h_a):
        self.a = a
        self.b = b
        self.c = c
        self.h_a = h_a

    def obwod(self):
        return self.a + self.b + self.c

    def pole(self):
        return self.a * self.h_a / 2


trojkatRownoboczny = Trojkat(10, 10, 10, 8)
trojatIzy = Trojkat(5, 12, 13, 12)
print(trojkatRownoboczny.obwod())
print(trojatIzy.pole())


class Kolo:
    def __init__(self, r):
        self.r = r

    def obwod(self):
        return 2 * math.pi * self.r

    def pole(self):
        return math.pi * (self.r ** 2)


duzeKolo = Kolo(10)
print(duzeKolo.obwod())
print(duzeKolo.pole())


class Student:
    def __init__(self, imie, nazwisko, numerIndeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numerIndeksu = numerIndeksu
        self.oceny = []

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.numerIndeksu}"

    def __int__(self):
        return 0
    def dodajOcene(self, ocena):
        self.oceny.append(ocena)

    def zwrocSrednia(self):
        return sum(self.oceny)/len(self.oceny)


studentIza = Student("Izabela", "Czumałowska", 120017)
studentIza.dodajOcene(5)
studentIza.dodajOcene(3)
print(studentIza.zwrocSrednia())

class Ksiazka:
    def __init__(self, tytul, imieAutora, nazwiskoAutora, liczbaStron, cena, gatunek):
        self.tytul=tytul
        self.imieAutora=imieAutora
        self.nazwiskoAutora=nazwiskoAutora
        self.liczbaStron=liczbaStron
        self.cena=cena
        self.gatunek=gatunek
        self.iloscZakupien = 0
        self.ocenyUzytkownikow = []

    def __str__(self):
         return f"{self.imieAutora} {self.nazwiskoAutora} {self.tytul}"

    def kupKsiazke(self):
        self.iloscZakupien += 1
        return print("Ilość zakupień książki to "+ str(self.iloscZakupien) + ", a ogólny przychód to "+ str(self.iloscZakupien*self.cena))

    def dodajOcene(self, ocena):
        self.ocenyUzytkownikow.append(ocena)


    def zwrocSrednia(self):
        return sum(self.ocenyUzytkownikow)/len(self.ocenyUzytkownikow)


nowaKsiazka=Ksiazka("Limes Inferior", "Janusz", "Zajdel", 350, 35, "science-fiction")
drugaKsiazka=Ksiazka("Paradyzja", "Janusz", "Zajdel", 220, 24, "science-fiction")
print(nowaKsiazka.kupKsiazke())
print(nowaKsiazka.kupKsiazke())
nowaKsiazka.dodajOcene(3.5)
nowaKsiazka.dodajOcene(5)
print(nowaKsiazka.zwrocSrednia())


