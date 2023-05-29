class Pracownik:
    def __init__(self, imie, nazwisko, pensjaBrutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensjaBrutto = pensjaBrutto

    def __str__(self):
        pass

    def obliczNetto(self):
        skladkaEmerytalna = self.pensjaBrutto * 0.0976
        skladkaRentowa = self.pensjaBrutto * 0.015
        skladkaChorobowa = self.pensjaBrutto * 0.0245
        zus = skladkaEmerytalna + skladkaRentowa + skladkaChorobowa
        skladkaZdrowotna = (self.pensjaBrutto - zus) * 0.09
        ppk = self.pensjaBrutto * 0.02
        # jesli pracownik mieszka na miejscu -250 zl jesli nie 300zl
        czyPPK = str(input("Czy pracownik płaci PPK?"))
        czyMieszka = str(input("Czy pracownik mieszka na miejscu?"))
        if czyMieszka==("Tak") and czyPPK==("Tak"):
            dochod = self.pensjaBrutto - zus - skladkaZdrowotna - ppk - 250

        else:
            if czyMieszka==("Nie") and czyPPK==("Tak"):
                dochod = self.pensjaBrutto - zus - skladkaZdrowotna - ppk - 300

            else:
                if czyMieszka==("Nie") and czyPPK==("Nie"):
                    dochod = self.pensjaBrutto - zus - skladkaZdrowotna - 300


                else:
                    if czyMieszka==("Tak") and czyPPK==("Nie"):
                        dochod = self.pensjaBrutto - zus - skladkaZdrowotna - 250

        zaliczka = dochod * 0.12 - 300
        pensjaNetto = dochod - zaliczka
        return print(
            "Pensja netto wynosi: " + str(pensjaNetto) + ", składka emerytalna wynosi: " + str(skladkaEmerytalna)
            + ", składka rentowa wynosi: "+ str(skladkaRentowa) + ", składka chorobowa wynosi: " + str(skladkaChorobowa)
            + ", a zaliczka na podatek: " + str(zaliczka) + ".")

    def obliczKoszty(self):
        return 0

    #
    # pracownicy = []
    #
    # # for pracownik in pracownicy:
    # #     print("Pracownik Kowalski: ")
    # #     print("-pensja brutto: ")
    # #     print("-pensja netto: ")
    # #     print("-koszty pracodawcy: ")
    # #     print("-koszt całkowity: ")
    # #
    # # print("Suma kosztów wynosi: ")


pracownik1 = Pracownik("Izabela", "Czumałowska", 5500)
pracownik1.obliczNetto()
