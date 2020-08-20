# Chapter 4 - Text versus Bytes

# Character issues

`encode()` and `decode()` method

## Byte Essentials

- immutable `byte`
- mutable `bytearray`

```python
cafe = bytes('café', encoding='utf_8')
cafe[0]
cafe[:1]
cafe_arr = bytearray(cafe)
cafe_arr
```

```python
import array
numbers = array.array('h', [-2, -1, 0, 1, 2]) 
octets = bytes(numbers) 
octets
```

## Structs and Memory Views

```python
>>> import struct
>>> fmt = '<3s3sHH' # 
>>> with open('filter.gif', 'rb') as fp:
... img = memoryview(fp.read()) # 
...
>>> header = img[:10] # 
>>> bytes(header) # 
b'GIF89a+\x02\xe6\x00'
>>> struct.unpack(fmt, header) # 
(b'GIF', b'89a', 555, 230)
>>> del header # 
>>> del img
```

## 

from page 109

omitted