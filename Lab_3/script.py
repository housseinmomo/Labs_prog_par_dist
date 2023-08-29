# from functools import reduce

# # Avec un lambda, vous êtes limité à créer des fonctions qui n'ont qu'une seule expression

# a = [1, 2, 3, 4, 5]

# product = reduce(lambda x, y: x * y, a)

# print(product)

# squares = map(lambda x: x * x, a)

# print(list(squares))

# square = lambda x: x * x

# print(square(5))

# def add(x, y): 
#     return x + y

# plus_cinq = lambda x: add(x, 5)

# print(plus_cinq(5))

# def multiply(x, y):
#     return x * y

# double_a = map(lambda x: multiply(x, 2), a)

# print(list(double_a))


# Exercise Lab 03: 

# Question A :

f = lambda str1, str2: str1 + " " + str2  

print(f("mugen", "sama"))

# Question B : 

numbers = [10, -28, 33, 28, -49, 56, 49]

numbers = list(map(lambda n: abs(n), numbers))

print(numbers)

    # Result : [10, 28, 33, 28, 49, 56, 49]

# Question C : 

a = [5, -1, 12, 10, 2, 8]

largest_even = max(list(filter(lambda x: x % 2 == 0, a)))

print(largest_even)


# Question D :

transform_text = lambda word: word[1:] + word[0] + 'ay'

tab_word = lambda str1: str1.split()


#  double_a = map(lambda x: multiply(x, 2), a)

pig_latin = map(lambda x: transform_text(map(tab_word(x))))


print(pig_latin("Hello world"))


