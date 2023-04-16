# zadanie 1.1

hello = "Hello"
student = "Ola"

print("{}".format(hello)+" {}".format(student))

# zadanie 1.2

student = input("Wpisz swoje imie ")

print("Hello "+student)

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]

liczba_studentow = len(studenci)
print("Liczba studentow wynosi: " + str(liczba_studentow))

# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

for i in range(len(studenci)):
    print("Hello "+ studenci[i])

# zadanie 1.5

liczba = 3
potega = 4

wynik = liczba**potega

print("Wynik wynosi: " +str(wynik))

# zadanie 1.6

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
nawias = "("
liczba_nawiasow_otwierajacych = ciag_znakow.count(nawias)

print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

# zadanie 1.7

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
posortowaniStudenci = sorted(studenci)
for student in posortowaniStudenci:
    print(student)

# zadanie 1.8

studenci2 = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
posortowaneNazwiska = sorted(studenci2, key=lambda x: x.split()[1])
for student in posortowaneNazwiska:
    print(student)

# zadanie 1.9

studenci3 = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
liczba_n = 0
for i in studenci3:
    if i.split()[1].startswith("N"):
        liczba_n+=1
print("Liczba studentow na N wynosi: "+ str(liczba_n))

# zadanie 1.10

wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

def czyLiniowa(wykres):
    a1 = (wykres[1][1]-wykres[0][1])/(wykres[1][0]-wykres[0][0])
    a2 = (wykres[2][1]-wykres[0][1])/(wykres[2][0]-wykres[0][0])
    if a1==a2:
        funkcja = True
    else:
        funkcja = False
    return funkcja

wykres_1_funkcja_liniowa = czyLiniowa(wykres_1)
wykres_2_funkcja_liniowa = czyLiniowa(wykres_2)
wykres_3_funkcja_liniowa = czyLiniowa(wykres_3)

if wykres_1_funkcja_liniowa:
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")
