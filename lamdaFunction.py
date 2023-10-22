# Lambda arguments: Expression (The form)
'''
Lamda Function are typically used when you need a simple function that is used only 1 in your code
'''


def add10_function(x):
    return x + 10

'''
This function basically, take a argument and plus 10, and we can do it shortly with lambda function
'''
add10 = lambda x: x + 10 # The first X is the argument, and the second one is contained in the expression
# print( add10(5) )

# This is when we have multiple arguments
multiply = lambda x,y: x * y
# print( multiply(9,8) )

# We create a list containing a tuples
points2D = [(1,2), (15,1), (5,-1), (10,4)]
# print(points2D)

points2D_sorted = sorted(points2D)
# print(points2D_sorted)

points2D_sorted1 = sorted(points2D, key=lambda x: x[1]) # sort as the Y index
# print(points2D_sorted1)

# We can apply the same with normal function
def sort_by_y(x):
    return x[1]
points2D_sorted2 = sorted(points2D, key=sort_by_y)
# print(points2D_sorted2)

# Another lamda function
points2D_sorted3 = sorted(points2D, key=lambda x: x[0] + x[1])
# print(points2D_sorted3) # it sorst by sum of x[0] and x[1]

'''
Map Function: executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
Syntax: map(function, iterables)

'''
a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x*2,a)
print(b) # it gonna be displayed as a map function
# print(list(b)) # convert it to a list

# U can also do the same with list comprehension
c =[x*2 for x in a]
print(c)

'''
Filter function: returns an iterator where the items are filtered through a function to test if the item is accepted or not.
Syntax: filter(function, iterable)

'''
d = filter(lambda x: x%2 == 0, a)
print(d)
print(list(d))
# list comprehension
e = [x for x in a if x%2 == 0]
print(e)

'''
Reduce function:
'''
from functools import reduce
product_a = reduce(lambda x,y : x*y, a)
print(product_a)





