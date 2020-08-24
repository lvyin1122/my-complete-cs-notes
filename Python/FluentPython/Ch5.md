# Chapter 5 - First-class Functions

- Created at runtime
- Assigned to a variable or element in a data structure
- Passed as an argument to a function
- Returned as the result of a function

```python
>>> fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
>>> sorted(fruits, key=len)
```

map, filter, reduce, apply

all(iterable) any(iterable)

## Anonymous Functions

```python
>>> fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
>>> sorted(fruits, key=lambda word: word[::-1])
```

## Callable Objects

- User-defined functions
- Built-in functions
- Built-in methods
- Methods
- Classes
- Class instances
- Generator functions

## User-defined callable objects

```python
import random
class BingoCage:
    def __init__(self, items):
        self._items = list(items) 
        random.shuffle(self._items) 
    
    def pick(self): 
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage') 
    
    def __call__(self): 
        return self.pick()
```

## Function introspection

dir()

## From Positional to Keyword-Only Parameters

```python
def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                            for attr, value
                            in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                        (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)
```

put keyword-only parameters after a *

```python
>>> def f(a, *, b):
... return a, b
...
>>> f(1, b=2) (1, 2)
```

## Retrieving Information about Parameters

```python
# clip.py
def clip(text, max_len=80):
    """Return text clipped at the last space before or after max_len
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # no spaces were found
        end = len(text)
    return text[:end].rstrip()
```

`__code__` and `__defaults__`

`clip.__code__.co_varnames`

`clip.__code__.co_argcount`

### the inspect module

```py
from inspect import signature

>>> from clip import clip
>>> from inspect import signature
>>> sig = signature(clip)
>>> sig # doctest: +ELLIPSIS
<inspect.Signature object at 0x...>
>>> str(sig)
'(text, max_len=80)'
>>> for name, param in sig.parameters.items():
... print(param.kind, ':', name, '=', param.default)
```

## Function Annotations

```py
def clip(text:str, max_len:'int > 0'=80) -> str:  # <1>
    """Return text clipped at the last space before or after max_len
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # no spaces were found
        end = len(text)
    return text[:end].rstrip()
```

```py
clip.__annotations__

sig = signature(clip)
sig.return_annotation

>>> for param in sig.parameters.values():
... note = repr(param.annotation).ljust(13) # param.annotation
... print(note, ':', param.name, '=', param.default)
```

# Packages for Functional Programming

```python
from functools import reduce
from operator import mul

def fact(n):
    return reduce(mul, range(1, n+1))
```

```python
>>> from operator import itemgetter
>>> for city in sorted(metro_data, key=itemgetter(1)):
... print(city)

# multiple index arguments
>>> cc_name = itemgetter(1, 0)
>>> for city in metro_data:
... print(cc_name(city))
```

```python
>>> [name for name in dir(operator) if not name.startswith('_')]
['abs', 'add', 'and_', 'attrgetter', 'concat', 'contains',
'countOf', 'delitem', 'eq', 'floordiv', 'ge', 'getitem', 'gt',
'iadd', 'iand', 'iconcat', 'ifloordiv', 'ilshift', 'imod', 'imul',
'index', 'indexOf', 'inv', 'invert', 'ior', 'ipow', 'irshift',
'is_', 'is_not', 'isub', 'itemgetter', 'itruediv', 'ixor', 'le',
'length_hint', 'lshift', 'lt', 'methodcaller', 'mod', 'mul', 'ne',
'neg', 'not_', 'or_', 'pos', 'pow', 'rshift', 'setitem', 'sub',
'truediv', 'truth', 'xor']
```

## The operator module

### itemgetter, attrgetter, methodcaller

itemgetter

```py
>>> metro_data = [
... ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
... ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
... ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
... ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
... ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
... ]
>>>
>>> from operator import itemgetter
>>> for city in sorted(metro_data, key=itemgetter(1)):
... print(city)
```

attrgetter

```py
>>> metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) # 
... for name, cc, pop, (lat, long) in metro_data]
>>> metro_areas[0]
Metropolis(name='Tokyo', cc='JP', pop=36.933, coord=LatLong(lat=35.689722,
long=139.691667))
>>> metro_areas[0].coord.lat # 
35.689722
>>> from operator import attrgetter
>>> name_lat = attrgetter('name', 'coord.lat') # 
>>>
>>> for city in sorted(metro_areas, key=attrgetter('coord.lat')): # 
... print(name_lat(city))
```

methodcaller

```py
>>> from operator import methodcaller
>>> s = 'The time has come'
>>> upcase = methodcaller('upper')
>>> upcase(s)
'THE TIME HAS COME'
>>> hiphenate = methodcaller('replace', ' ', '-')
>>> hiphenate(s)
'The-time-has-come'
```

## Freezing Arguments with functools.partial

```py
from operator import mul
from functools import partial
triple = partial(mul, 3)
```
