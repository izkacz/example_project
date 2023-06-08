# from array import *
import numpy as np


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


# function that returns element of fibonacci
# fibonacci int i
# is i between 0 or 1?
# yes -> return 1
# no -> return sum of 2 previous elements

def fibonacci(i):
    if i - 1 <= 1:
        return 1
    else:
        return fibonacci(i - 1) + fibonacci(i - 2)


print(fibonacci(7))


# function returning factorial of some number
# factorial int i
# is i = 1?
# yes -> return 1
#  no -> return i * wynik poprzedniego dzialania

def factorial(i):
    if i == 1:
        return i
    else:
        return i * factorial(i - 1)


print(factorial(5))

# function solving sudoku
# empty cells are filled with 0
# find blank positions in the grid
# for every row and column on the grid:
# is the cell blank?
# no-> go to the next cell
# yes -> take numbers from 1 to 10 and perform function isPossible:
# n is the number we want to fill in
# check if n already existed in columns
# if yes -> return False
# check rows
# if yes-> return False
# check the 3x3 grid
# if yes -> return False
# if all 3 are possible -> return True
# if isPossible = True -> fill in  and go to the next cell,
# if isPossible = False -> increase n by 1 and call isPossible again
# if no number is possible -> fill in latest cell with 0 and try again

def ifPossible(x, y, n, grid):
    for i in range(9):
        if grid[x][i] == n:
            return False

    for i in range(9):
        if grid[i][y] == n:
            return False

    z = (x // 3) * 3
    w = (y // 3) * 3
    for i in range(3):
        for j in range (3):
            if grid[z + i][w + j] == n:
                return False
    return True

def solveSudoku(grid):
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for n in range(1, 10):
                    if ifPossible(x, y, n, grid):
                        grid[x][y] = n
                        solveSudoku(grid)
                        grid[x][y] = 0
                return
    print(np.matrix(grid))

newGrid = [[0, 0, 0, 3, 0, 7, 4, 0, 0],
        [9, 0, 0, 0, 0, 4, 0, 0, 8],
        [3, 7, 0, 0, 0, 0, 0, 6, 0],
        [8, 2, 0, 9, 0, 0, 6, 0, 0],
        [0, 0, 1, 2, 0, 0, 9, 0, 4],
        [0, 4, 0, 0, 3, 8, 0, 5, 0],
        [2, 0, 8, 6, 9, 0, 7, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [7, 5, 0, 0, 0, 0, 0, 0, 6]]
solveSudoku(newGrid)