Thukdict = {"name": "Thuk", 
            'age':21,
            'city': 'DaNang'}
print(Thukdict)
# Another way to create Thukdict
newThukdict = dict(name='ThukDepTrai', age=21,city=None)
print(newThukdict)

# Access the value in dic
value = Thukdict['age']
print(value)

# Cause the dic is immutable so u can add in a new contents to the dict
Thukdict['email'] = 'thuc.tran.data@gmail.com'
print(Thukdict['email'])

# Delete the item
del Thukdict['email'] # using delete statement
print(Thukdict)

# Thukdict.popitem() # Delete the last item using popitem method
# print(Thukdict)

try: 
    print(Thukdict['name'])
except: 
    print('Error')
  
for key in Thukdict: #Thukdict.keys() is also the same
    print(key)

for value in Thukdict.values():
    print(value)

# both of them
for key, value in Thukdict.items():
    print(key, value) 

# Create a copy dic 
ThukdictCopy = Thukdict.copy() # or dict(Thukdict) is also the same
ThukdictCopy['email'] = 'thuc.tran.data@gmail.com'
print(ThukdictCopy)
print(Thukdict)

# Merge 2 dict
dict1 = dict(name='Max', age=28, email='max@xyz.com')
dict2 = dict(name='Mary', age=27, city='Denver')
dict1.update(dict2)
print(dict1)

numb_dict = {3: 9, 4: 16, 5: 25, 6: 36}
value = numb_dict[4]
print(value)

mytuple = (8, 7)
dict3 = {mytuple: 15}
print(dict3)
'''
A tuple can be use as a key in a dict but list can not be use as a key in a dict.
- Cause lists are mutable n dict keys need to be hashable, and hashing mutable objects is a bad idea because hash values should be
computed on the basis of instance attributes
'''
# 