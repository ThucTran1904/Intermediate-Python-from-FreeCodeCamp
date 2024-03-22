def myGenerator():
    yield 1
    yield 3
    yield 2

g = myGenerator()
# for i in g:
#     print(i)
    
print("Another way: ")
# value = next(g)
# print(value)

# value = next(g)
# print(value)

# value = next(g)
# print(value)

# print(sum(g)) 
# print(sorted(g))

def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1
        
cd = countdown(5)
value = next(cd)
print(value)

print(next(cd))
print(next(cd))


'''
- Generators are memory efficient, they save a lot of memory when u work with a lot of data
- Another advantage of the generator object is that we don't have to wait until all the elements have been generated bf we start to use them
'''
import sys

def first(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums 

'''
The same functionality but apply the generator
'''
def first_generator(n):
    num = 0 
    while num < n:
        yield num
        num += 1
'''
Compare the size of 2 function, the first one is normal function | The second one is generator function
'''
print(sys.getsizeof(first(1000000)))
print(sys.getsizeof(first_generator(1000000)))

def fibonacci(limit):
    # 0 1 1 2 3 5 8 ...
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(35)
for i in fib:
    print(i)



myGenerator = (i for i in range(100) if i % 2 == 0)
for i in myGenerator:
    print(i)
print(sys.getsizeof(myGenerator) )

# Similar to list comprehension
mylist = [i for i in range(100) if i % 2 == 0]
print(mylist)
print( sys.getsizeof(mylist) )
