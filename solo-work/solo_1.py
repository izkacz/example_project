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
