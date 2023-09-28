# intertools: product, permutation, combination, accumulation, grouby, and infinite iterators
from itertools import product 
from itertools import permutations 
from itertools import combinations, combinations_with_replacement
from itertools import accumulate 
import operator
from itertools import groupby
from itertools import count, cycle, repeat


# This is ab product
a = [1, 2]
b = [3, 4]
prod = product(a,b)
print(prod)
print(list(prod) )
# We can specify the number of repetitions
c = [1, 2]
d = [3]
prod1 = product(c,d, repeat=2)
print(list(prod1) )

# This is ab permutation in Vietnamese we call Chỉnh hợp
e = [1, 2, 3]
perm = permutations(e)
print(list(perm) )
# we also can specify the length of the permutation by pass the argument
perm1 = permutations(e, 2)
print(list(perm1) )

# This is ab combination in Vietnamese we call Tổ hợp
f = [1, 2, 3, 4]
comb = combinations(f, 2) # The length argument is mandatory, in this case is 2
print(list(comb) )
comb_wr = combinations_with_replacement(f, 2)
print(list(comb_wr) )

# This is ab accumulate function
g = [1, 2, 3, 4]
acc = accumulate(g)
print(g)
print(list(acc))
'''
So as you can see the result the first element is still the same, the second one is the sum of 1 n 2, similarly the 
third one is the sum of 3 n 3

'''
# The default is sum, but in case you want to multiply
h = [1, 2, 3, 4]
acc1 = accumulate(h, func=operator.mul)
print(h)
print(list(acc1) )
# max
i = [1, 2, 5, 9, 3, 4]
acc2 = accumulate(i, func=max)
print(i)
print(list(acc2) )

# This is ab groupby
j = [1, 2, 3, 4]

def smaller_than_3(x):
    return x < 3 # it will return true or false
group_obj = groupby(j, key=smaller_than_3)
print(group_obj)
for key, value in group_obj:
    print(key, list(value) )

'''
group_obj = groupby(j, key= lambda x: x<3)
print(group_obj)
for key, value in group_obj:
    print(key, list(value) )
    
It will also do the same thing

'''
# Another example
people = [{'name': 'Tim', 'age':25}, # This is a list containing 4 dicts
          {'name':'Dan', 'age':25},
          {'name':'Lisa', 'age':27},
          {'name':'Claire', 'age':28}
          ]

newGroup = groupby(people, key= lambda x: x['age']) # create a group containing people are as the same age
for key, value in newGroup:
    print(key, list(value))
    
# count fuction
for i in count(10):
    print(i)
    if i == 15:
        break
        
# cycle function
k = [1, 2, 3, 4]
for i in cycle(k):
    print(i)

