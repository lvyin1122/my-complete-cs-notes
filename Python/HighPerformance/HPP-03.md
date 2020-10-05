# High Performance Python - Ch.3

# Dictionaries and Sets

```python
def index_sequence(key, mask=0b111, PERTURB_SHIFT=5):
    perturb = hash(key) # 
    i = perturb & mask
    yield i
    while True:
        i = ((i << 2) + i + perturb + 1)
        perturb >>= PERTURB_SHIFT
        yield i & mask
```

