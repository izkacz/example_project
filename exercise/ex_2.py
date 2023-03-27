
import math
#kwadrat
a=10
obwod=a*4
pole = a*a

print("Obwód kwadratu wynosi "+str(obwod)+", a pole " +str(pole)+ ".")

#prostokąt

b=5
obwodProst=(a*2)*(b*2)
poleProst=a*b

print("Obwód prostokąta wynosi "+str(obwodProst)+", a pole " +str(poleProst)+ ".")

#trapez
h=2
r=5
obwodTrap=a+b+(2*r)
poleTrap=((a+b)*h/2)
print("Obwód trapezu wynosi "+str(obwodTrap)+", a pole " +str(poleTrap)+ ".")

#koło
pi_zmienna= math.pi
obwodKol=2*pi_zmienna*r
poleKol=pi_zmienna*r**2
print("Obwód koła wynosi "+str(obwodKol)+", a pole " +str(poleKol)+ ".")

#trojkat
c=7
obwodTroj=a+b+c
poleTroj=(a+b)*h/2
print("Obwód trójkąta wynosi "+str(obwodTroj)+", a pole " +str(poleTroj)+ ".")