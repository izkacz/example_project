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