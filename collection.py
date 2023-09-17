# Collection: Counter, namedtuple, OrderedDict, DefaultDict, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque


a = 'aaaaabbbbccc'
myCounter = Counter(a)
print(myCounter)
print(myCounter.items())
print(myCounter.keys())
print(myCounter.values())


# Find most common elements
print(myCounter.most_common(1)) # Return a list with a tuple in it
# Access the tuple
print(myCounter.most_common(1)[0]) 
# Acess more deeper
print(myCounter.most_common(1)[0][0])

print(myCounter.elements())
print(list(myCounter.elements()))

# namedtuple
point = namedtuple('Point', 'X,Y')
pt = point(1, -4)
print(pt)

# Access the field
print(pt.X, pt.Y)

# ordered dict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)
# If we change the order of the dict, it gonna be apply

# Default dict 
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d)
# Access the key 
print(d['a']) # when u state a key that is not exist before it gonna return the default int value: 0

# Deque
de = deque()
de.append(1)
de.append(2)
de.appendleft(3)

# pop and pop left
# de.popleft()

# clear, extend, extendleft 
de.extendleft([4,5,6])
print(de)
# Rotate all elements 1 place to the right 
de.rotate(2)
print(de)
