# Chapter 2 - An Array of Sequences

## List comprehensions and generator expressions

List comprehensions
```python
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
```

Generator expressions
```python
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes): 
    print(tshirt)
```

## Tuples as records

```python
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

for passport in sorted(traveler_ids): 
    print('%s/%s' % passport)
```

## Unpacking

```python
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), 
    ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids): 
    print('%s/%s' % passport)

b, a = a, b


divmod(20, 8)

t = (20, 8)
divmod(*t)

quotient, remainder = divmod(*t)
quotient, remainder
# (2, 4)

import os
_, filename = os.path.split('/home/.../.ssh/idrsa.pub')
filename
# _ as a placeholder
```

Using * to grab excess items
```python
a, b, *rest = range(5)
a, b, rest
# (0, 1, [2, 3, 4])

# any position
a, *body, c, d = range(5)
*head, b, c, d = range(5)
```

Nested Tuple Unpacking

```python
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),  
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas: 
    if longitude <= 0: 
        print(fmt.format(name, latitude, longitude))
```

## Named Tuples

```python
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

tokyo.population
tokyo.coordinates
tokyo[1]
```

```
City._fields
City._make(delhi_data)
delhi._asdict() # returns a collections.OrderedDict built from the named tuple instance
```

## Tuples as Immutable Lists

Omitted 

## Slicing 

advanced forms of slicing 

why slices and range exclude the last item: easy to see ...

## Slice Objects

```python
s[::3]
s[::-1]
s[::-2]
```

`[start:stop:step]` 

### To parse flat-file data

Omitted

## Multidimensional Slicing and Ellipsis

Ellipsis object

## Assigning to Slices

```python
l = list(rang(0, 10))
l[2:5] = [4, 10]
del l[1:2]
```

## Augmented Assignment with Sequences

+= *=

## list.sort() and sorted

.sort() => inplace sorting
sorted => new object

```
sorted(fruits, reverse=True)
sorted(fruits, key=len)
```



