def add(x,y):
    return x+y

def mutliply(x, y):
    return x*y

def diff(x, y):
    return x/y

def my_map(func, arg1, arg2):
    
    res = []
    print(func.__name__)
    print(arg1)
    print(arg2)
    # On recup un a un les nombre de chaque liste, et ensuite on utilise la func add pour les addtionner
    # zip is used to merge 2 lists together. 
    # It returns the first element of each list, then 2nd element of each list, etc.
    # This is a trick to consider the two lists as key and data to create a dictionary.
    for i, j in zip(arg1, arg2):
        res.append(func(i, j))
    return res

# test my_map
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

# Avec la prog fonctionnelle, on peux assigner une fonction a une variable
# On peux egalement placer une fonction en param
# result = my_map(diff, a, b)

# print(result)


# Un repère de l’espace est constitué de 3 axes : celui des abscisses, celui des ordonnées et celui des cotes.

# Si A(xA ; yA ; zA) et B(xB ; yB ; zB) 




import math 

def calc_distance(point1, point2):
    res = math.sqrt(
        ( (point2[0] - point1[0]) * (point2[0] - point1[0]) ) +
        ( (point2[1] - point1[1]) * (point2[1] - point1[1]) ) +
        ( (point2[2] - point1[2]) * (point2[2] - point1[1]) )
    )

    return res



points1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
points2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]

distances = map(calc_distance, points1, points2)

# L'object renvoyer par la fonction map est un un itérateur qui contient le résultat de l'application de votre fonction à chaque 
# élément des données
# print("Distance entre deux points :")
# print(list(distances))


def square(x):
    return x*x

def find_smallest(x, y, z):
    min = 0
    if x < y and x < z:
        min = x
    elif y < x and y < z:
        min = y
    else:
        min = z
    return min

a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
c = [1, 2, 1, 2, 1]

result_smallest = map(find_smallest, a, b, c)
result_square = map(square, b)

# print("result_smallest: ", list(result_smallest))
# print("result_square: ", list(result_square))

from functools import reduce

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

# Faire la somme du tableau renvoyer par la fonction add()

total = 0

result = map(add, a, b)

total = reduce(mutliply, a)

# exemple de « réduction »
# La liste de nombres a été réduite en une valeur totale en ajoutant chaque valeur à un total cumulatif
# La réduction est le complément du mapping
# La fonction de réduction peut être n'importe quelle fonction qui accepte deux arguments et renvoie une seule valeur

# for i in result: 
#     total += i

print(total)


# Exercise lab 2 : 

def join_strings(str1, str2):
    return str1 + " " + str2

a = ["You", "are", "despicable", "-", "Daffy", "Duck"]

result = reduce(join_strings, a)
print(result)


