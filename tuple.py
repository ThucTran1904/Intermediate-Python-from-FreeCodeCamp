tuple1 = "Thuc","10B$","DaNang"
tuple2 = ("Her",10,'Somewhere')
tuple3 = ('ThucDeptrai')
'''
In case you declare a tuple like the third one, python gonna consider it like a string, to handle this situation,
you need to add a comma to the end of that tuple
=> tuple3 = ('ThucDeptrai',)

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
print()
