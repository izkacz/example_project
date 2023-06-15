import pandas as pd
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
        if czyMieszka == ("Tak") and czyPPK == ("Tak"):
            dochod = self.pensjaBrutto - zus - skladkaZdrowotna - ppk - 250
        else:
            if czyMieszka == ("Nie") and czyPPK == ("Tak"):
                dochod = self.pensjaBrutto - zus - skladkaZdrowotna - ppk - 300
            else:
                if czyMieszka == ("Nie") and czyPPK == ("Nie"):
                    dochod = self.pensjaBrutto - zus - skladkaZdrowotna - 300
                else:
                    if czyMieszka == ("Tak") and czyPPK == ("Nie"):
                        dochod = self.pensjaBrutto - zus - skladkaZdrowotna - 250

        zaliczka = dochod * 0.12 - 300
        pensjaNetto = dochod - zaliczka
        return print(
            "Pensja netto wynosi: " + str(pensjaNetto) + ", składka emerytalna wynosi: " + str(skladkaEmerytalna)
            + ", składka rentowa wynosi: " + str(skladkaRentowa) + ", składka chorobowa wynosi: " + str(
                skladkaChorobowa)+ ", składka zdrowotna wynosi: "+ str(skladkaZdrowotna)
            + ", a zaliczka na podatek: " + str(zaliczka) + ".")

    def obliczKoszty(self):
        skladkaEmerytalna = self.pensjaBrutto * 0.0976
        skladkaRentowa = self.pensjaBrutto * 0.065
        skladkaWypadkowa = self.pensjaBrutto * 0.0167
        funduszPracy = self.pensjaBrutto * 0.0245
        funduszFGSP = self.pensjaBrutto * 0.001

        czyPPK = str(input("Czy pracownik płaci PPK?"))

        if czyPPK == "tak":
            ppk = self.pensjaBrutto * 0.015
        else:
            ppk = 0
        return print("Koszty pracodawcy wynoszą: na składkę emerytalną: "+ str(skladkaEmerytalna)+", na składkę rentową: "
                     + str(skladkaRentowa)+ ", na składkę wypadkową: "+str(skladkaWypadkowa)+ ", na fundusz pracy: "+str(funduszPracy)
                     +", na fundusz FGSP: "+ str(funduszFGSP)+", a na PPK: "+str(ppk)+".")

pracownicy= pd.read_csv(r'C:\Users\PC\Desktop\wszystko\studia\semestr 8\io\pracownicy.csv', sep=';')
pracownicyLista=pracownicy.values.tolist()

for pracownik in pracownicyLista:
    pracownik1 = Pracownik(*pracownik)
    print("Pracownik: "+ pracownik1.imie+ " "+pracownik1.nazwisko)
    pracownik1.obliczNetto()
    pracownik1.obliczKoszty()



