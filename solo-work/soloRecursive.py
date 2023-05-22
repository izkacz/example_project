from array import *


# adding elements to an arrayList l in recursive
# function sumList l
# is l empty?
# yes -> 0
# no -> [0]+ sumList[rest of the list]

def sumList(lista):
    if len(lista) == 0:
        return 0
    else:
        firstEl = lista.pop(0)
        return firstEl + sumList(lista)


list1 = [1, 2, 3]
print(sumList(list1))


# find max value in a list
# function findMax list l
# is length of l =1?
# yes -> return l[0]
# no -> is l[0] bigger than l[1]?
# yes -> return l without l[1]
# no -> return l without l[0]

def findMax(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        if lista[0] > lista[1]:
            element = lista.pop(1)
            return findMax(lista)
        else:
            element = lista.pop(0)
            return findMax(lista)


list2 = [10, 11, 3, 6, 8, 17, 5, 9]
print(findMax(list2))
