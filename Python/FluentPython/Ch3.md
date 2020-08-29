# Chapter 3 - Dictionaries and Sets

# Generic Mapping Types

## dict comprehensions

```python
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (81, 'Japan'),
]

country_code = {country:code for code, country in DIAL_CODES}
```

## get() and setdefault()

```python
# adapted from Alex Martelli's example in "Re-learning Python"
# http://www.aleax.it/Python/accu04_Relearn_Python_alex.pdf
# (slide 41) Ex: lines-by-word file index

# BEGIN INDEX_DEFAULT
"""Build an index mapping word -> list of occurrences"""

import sys
import re
import collections

WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list)     # <1>
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index[word].append(location)  # <2> 

# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])
# END INDEX_DEFAULT
```

## Flexible key lookup - collections.defaultdict

see the code block above

### the __missing__ method

```python
# BEGIN STRKEYDICT0
class StrKeyDict0(dict):  # <1>

    def __missing__(self, key):
        if isinstance(key, str):  # <2>
            raise KeyError(key)
        return self[str(key)]  # <3>

    def get(self, key, default=None):
        try:
            return self[key]  # <4>
        except KeyError:
            return default  # <5>

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()  # <6>

# END STRKEYDICT0
```

## Variation of Dict

- collections.OrderedDict
- collections.ChainMap
- collections.Counter

## Subclassing Userdict

```python
# BEGIN STRKEYDICT

import collections


class StrKeyDict(collections.UserDict):  # <1>

    def __missing__(self, key):  # <2>
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data  # <3>

    def __setitem__(self, key, item):
        self.data[str(key)] = item   # <4>

# END STRKEYDICT
```

## Immutable Mappings

MappingProxyType

```python
from types import MappingProxyType
d = {1 : 'A'}
d_proxy = MappingProxyType(d)
```

# Set Theory

## a needle in a haystack

```python
found = len(set(needles).intersection(haystack))
```
This works for any iterable objects

fast membership test

## set literals

## set comprehensions

# Under the Hood

hash table

omitted