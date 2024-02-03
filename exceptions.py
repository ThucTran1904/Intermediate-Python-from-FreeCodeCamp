x = 9
if x < 0:
    raise Exception('X should be positive')

assert ( x>=0), 'X is not positive'

try:
    a = 5 / 0
    b = 5 + '10'
except ZeroDivisionError as z:
    print(z)
except TypeError as t:
    print(t)
else:
    print('Everything is fine')
finally:
    print('Cleaning up...')
    
    
'''
Create your own Exception - Define an error
'''
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
        

def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')
    if x < 5: 
        raise ValueTooSmallError('Value is too small', x)

try: 
    test_value(4)
except ValueTooHighError as h:
    print(h)
except ValueTooSmallError as e:
    print(e.message, e.value)
    
    
