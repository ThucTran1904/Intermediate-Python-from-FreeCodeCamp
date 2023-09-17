tuple1 = "Thuc","10B$","DaNang"
tuple2 = ("Her",10,'Somewhere')
tuple3 = ('ThucDeptrai')
'''
In case you declare a tuple like the third one, python gonna consider it like a string, to handle this situation,
you need to add a comma to the end of that tuple
=> tuple3 = ('ThucDeptrai')
'''
print(type(tuple3))
# Create a tuple using a list
tuple4 = tuple(["Thuc","Deptrai-TaiGioi","DaNang"])
print(tuple4)
# Access the tuple
item = tuple4[0]
# print each item in the tuple
for x in tuple4:
    print(x)
# Check a specific item that contains in the tuple or not 
if "Thuc" in tuple4:
    print("Oh Yeahh")
else:
    print("Oh no")

#lend method for tuple
appleTuple = 'a','p','p','l','e'
length = len(appleTuple)
# using lend method with list                                                     
print(length)
# count method, to count the number of appearances of a specific item
print(appleTuple.count('e'))
# index method, return the first apperance of the sepecified item
print(appleTuple.index('e'))
# convert a tuple to a list and vice versa
convert_list = list(appleTuple)
print(convert_list)
# convert a that list to tuple again
tuplelist = tuple(convert_list)
print(tuplelist)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5] # except for the last element
print(b)

c = a[2:]
print(c)

d = a[::-2]
print(d)

# Unpack the tuple
Thuk_tuple = "Thuk", 21, "DaNang"
name, age, city = Thuk_tuple
print(name, age, city)

# We can unpack multiple elements with * (star)
new_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
i1, *i2, i3 = new_tuple
print(i2)

import sys 
tuplee = 0, 1, 2, "hello", True
listtt = [0, 1, 2, "hello", True]
print(sys.getsizeof(tuplee), "bytes")
print(sys.getsizeof(listtt), "bytes")
# ==> with the same items but tuple consume less bytes than the list

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4)", number=1000000))
# the time when creating a tuple is also much less than the time when creating a list