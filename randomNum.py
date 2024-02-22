import random

a = random.uniform(1,10) # Float
b = random.randint(1,10) # Integer | randrange also works | Note that the upper bound is not included
c = random.normalvariate(0,1)

theList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(theList)

# Pick a random element
# choice = random.choice(theList)
choice = random.choices(theList,k=1) # In this case k = 1 | The are 2 options choice and choices
print(choice)

# Pick some random elements
choice1 = random.sample(theList, 3)
print(choice1)

# Shuffle the elements
random.shuffle(theList)
print(theList)

# Reproduce the data with the random.seed function
random.seed(100) 
print(random.random() )
print(random.randint(1,10))

'''
Because these numbers are reproducible. They are not recommended for security purposes. For this purpose we use 'secret' module
- It specifically uses for things like passwords, security tokens or account authentication 
'''

import secrets
d = secrets.randbelow(11)
print('D is',d)  
e = secrets.randbits(4)
'''
- The upper one gonna return a random number with the maximum 4 bits
+ 2 = 0100
+ 3 = 0110
+ 15 = 1111
'''
print(e)

newList = list('ABCDEFGH')
f = secrets.choice(newList)
print(f)

import numpy as np

array = np.random.rand(3,3) # Create a m x n array, in this case it is 3 x 3 array (matrix)
array1 = np.random.randint(0, 10, (3,4) )
arr = np.array([ [1,2,3], [4,5,6], [7,8,9] ])
np.random.shuffle(arr)

print(array)
print(array1)
print(arr)

np.random.seed(1)
array2 = np.random.randint(0, 100, (4,3))
print(array2)
