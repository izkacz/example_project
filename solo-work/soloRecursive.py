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
       firstEl=lista.pop(0)
       return firstEl + sumList(lista)


list1 = [1, 2, 3]
print(sumList(list1))


# find max value in a list
# function findMax list l
# is length of l =1?
# yes -> return

