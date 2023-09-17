# Sets: unordered, mutable, no duplicate
Thukset = {1,2,3}
# U can't replicate the same items cause set doesn't allow duplication
print(Thukset)
# Conver a list to a set
numset = set([1,2,3])
print(numset)
# Convert a string -> a set
helloSet = set('Hello')
print(helloSet) # U can see that the order is arbitrary, cause set doesn't care ab the order

# Create a empty set like this
emptySet = {}
print(type(emptySet) ) # Python gonna classify this as a dict

# To avoid this one, here is the solution
newEmptySet = set()
print(type( newEmptySet ))

# Add new elements to the set
newEmptySet.add(1)
newEmptySet.add(2)
newEmptySet.add(3)
newEmptySet.add(4)
newEmptySet.add(5)
# Remove an item from the set
newEmptySet.remove(1)
# Discard the item from the set
newEmptySet.discard(2)
'''
Remove vs Discard
Similarity:
- They are both using for eliminating the element in a set
Difference:
- Remove: an element from the set, if it doesn't exist already, the programm gonna get error
- Discard: an element from the set, if it doesn't exist already, the program gonna still okay
'''
# Clear method, for empty our set
newEmptySet.clear()

# Pop method, remove the fist element from the set
print(newEmptySet.pop())

for x in newEmptySet:
    print(x)

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
prime = {2, 3, 5, 7}

# Union method, combine elements from 2 sets without duplication
unionOddEvens = odds.union(evens)
print(unionOddEvens)

# Intersection method, take elements that mutually include in 2 sets
i = odds.intersection(evens)
print(i) # it returns a empty set cause there is no any elements that mutually include in 2 sets
i2 = evens.intersection(prime)
print(i2)
i3 = odds.intersection(prime)
print(i3)

# Difference method, take every elements that only contain in the first set
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
diff = setA.difference(setB)
print(diff)

# Symmetric difference method, eliminate elements that contain mutually in the 2 sets
diff2 = setA.symmetric_difference(setB)
print(diff2)

# Update a set
setA.update(setB)
setA.intersection_update(setB)
'''
It happens the same with difference update, and symmetric difference update
'''
# print(setA)

print(setB.issubset(setA)) # If all the elements in the first set(B) are in the second set(A) then return True
print(setA.issuperset(setB)) # If the elements in the first set(A) are in the second set(B) then return True
setC = {7,8}
print(setB.isdisjoint(setC)) # If there is no common elements between 2 sets then return True

setD = set(setC) # SetC.copy()

# Frozen sets, can't change anything after its creation
a = frozenset([1,2,3,4,5])
print(a)   