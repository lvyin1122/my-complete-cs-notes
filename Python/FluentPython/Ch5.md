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

