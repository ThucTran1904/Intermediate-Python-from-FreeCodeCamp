import functools

# @mydecorator
# def dosomething():
#     pass

def start_end_decorator(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

result = add5(10)
    
# print_name = start_end_decorator(print_name)
print(result)
print(help(add5))
print(add5.__name__)

'''
Decorator template:

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do stuff
        result = func(*args, **kwargs)
        # Do stuff
        return result
    return wrapper
    

'''

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name} !!!")
    
greet('Alex')

# Class decorator
'''
- Class decorator do the same thing as function decorators, but they are typically used if we want to maintain and update a state 
'''
class CountCalls:
    def __init__(self, func):
        self.func = func 
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello")

say_hello()
say_hello()
say_hello()
