from timeit import default_timer as timer

# Strings: ordered, immutable, text representation
my_string = "Hello world"
multiline_string = """This
is 
a 
multiline 
string"""
print(my_string)
print(multiline_string)

# access the string
char = my_string[0]
char2 = my_string[-1]
print(char, char2)

# U can't now change the contents in the string, cause string is immutable
# for example we have my_string[0] = 'f'
''''U will see the notification str' object does not support item assignment, be aware of that'''

# Create a sub string
substring = my_string[::]
# substring = my_string[::-1] reverse the string
print(substring)

# Concatenate the strings
greeting = 'Hello'
name = 'Thuk dep trai'
greeting_sentence = greeting + ' ' + name
print(greeting_sentence)

# Print each element in the string
for i in greeting_sentence:
    print(i)

# Check a letter or sting are in the another string, or not
if 'e' in greeting_sentence:
    print('Oh yeahhhh')

# Remove white space (exception for whitespace between characeters)
exclamatory_sting = '     What the fuck are you doing, right now ?    '
print(exclamatory_sting.strip())

# Upper case n Lower case
print(exclamatory_sting.upper() )
print(exclamatory_sting.lower())

# Startswith n endswith
print(greeting_sentence.startswith(greeting))
print(greeting_sentence.startswith('Hello'))
print(greeting_sentence.endswith(name))

# Return the index of it's first item appearance in the sting | In case it can't find the item, it'll return -1
print(greeting_sentence.find('o')) 
print(greeting_sentence.find('clm')) 

# Count method, count how many a particular character in that list 
print(greeting_sentence.count('l')) 

# Replace method
print(my_string.replace('world', 'Universe') )

# Split method
howOld = 'How old are you ?'
print(howOld.split(' '))

howOldnew = 'How|old|are|you}?'
print(howOld.split('|'))

# Join method takes all items in an iterable and joins them into 1 sting
newString = '-'.join(howOld.split(' '))
print(newString)

#
a_string = ['a'] * 100
print(a_string)

'''
This is a bad Python code, cause string is immutable, then it has to create a new string and assign it back to the old one. So we can say
that this operation is kinda expensive
'''
start = timer()
thuk_string = ''
for i in a_string:
    thuk_string += i
stop = timer()
print(stop - start)

'''
The better one, it much cleaner 
'''
begin = timer()
thuk_string = ''.join(a_string)
end = timer()
print(end - begin)
'''
As you can see the execution time of the second one is really much less than the first one
'''

# %, .format, f-string
var = "Tom"
var2 = 'The variable is %s' % var # the character s stands for string

var3 = 3
var4 = 'The variable is %d' % var3 # the character d stands for decimal integer, Aware that it only supports decimal integer values not floating
print(var4)

var5 = 3.1412312312
var6 = 'The variable is %f' % var5 # the character f stands for floating point, we can specify how many digits we want to have we can try %.2f
print(var6)

# format method
var8 = 69
var7 = 'The variable is {:.2f} and {}'.format(var5,var8)
print(var7)

var9 = f'The variable is {var5} and {var8*69}'
print(var9)