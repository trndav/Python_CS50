# Counter, namedtuple, OrderDict, defaultdict, deque

from collections import Counter # Count elements and values in dict object
a = "aaabbbccccaaa"
mycounter = Counter(a)
print(mycounter)
print(mycounter.items())
print(mycounter.keys())
print(mycounter.values())
print(mycounter.most_common(2))
print(mycounter.most_common(2)[0][1])
print(list(mycounter.elements())) # Convert a to list

from collections import namedtuple # 
Point = namedtuple('Point', 'x,y') # Class Point with fields x,y
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

from collections import OrderedDict # Remember order of inserted items
ordered_dict = OrderedDict() # With py 3.7 this is not needed as dict {} remembers order items
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 0
print(ordered_dict)

from collections import defaultdict # Will have default value if key is not set (preventy raise keyerror)
d = defaultdict(float) # Int or float, list
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['c'])

from collections import deque # Add to tuple list from position, left, right
d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3) # Add to left
d.append(5)
print(d)
d.pop()
print(d)
d.popleft() # Remove from left
print(d)

d.extend([4, 5, 6])
d.extendleft([8, 9])
print(d)
d.rotate(1)
print(d)
d.rotate(-2)
print(d)