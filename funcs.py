'''
Unpack using * operator
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
*beginning, last = numbers # When unpacking the result is always a list
print(beginning, last)

my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}
new_list = [*my_tuple, *my_list, *my_set]
print(new_list)

dict_a = {'a': 1, 'b': 2, 'c': 3}
dict_b = {'d': 1, 'e': 2, 'f': 3}
my_dict = {**dict_a,**dict_b}
print(my_dict)
