# Mastering Python Performance - 01

## Profiling

- event-based profiling  
- statistical profiling

### event-based profiling

```python
import sys
def profiler(frame, event, arg):
    print ('PROFILER: %r %r' % (event, arg))
sys.setprofile(profiler)
#simple (and very ineficient) example of how to calculate the Fibonacci sequence for a number.
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def fib_seq(n):
    seq = [ ]
    if n > 0:
        seq.extend(fib_seq(n-1))
    seq.append(fib(n))
    return seq

print(fib_seq(2))
```

```terminal
PROFILER: 'call' None
PROFILER: 'call' None
PROFILER: 'call' None
PROFILER: 'call' None
PROFILER: 'return' 0
PROFILER: 'c_call' <built-in method append of list object at 0x0000022126786980>
PROFILER: 'c_return' <built-in method append of list object at 0x0000022126786980>
PROFILER: 'return' [0]
PROFILER: 'c_call' <built-in method extend of list object at 0x0000022126784540>
PROFILER: 'c_return' <built-in method extend of list object at 0x0000022126784540>
PROFILER: 'call' None
PROFILER: 'return' 1
PROFILER: 'c_call' <built-in method append of list object at 0x0000022126784540>
PROFILER: 'c_return' <built-in method append of list object at 0x0000022126784540>
PROFILER: 'return' [0, 1]
PROFILER: 'c_call' <built-in method extend of list object at 0x0000022125FC0B80>
PROFILER: 'c_return' <built-in method extend of list object at 0x0000022125FC0B80>
PROFILER: 'call' None
PROFILER: 'call' None
PROFILER: 'return' 1
PROFILER: 'call' None
PROFILER: 'return' 0
PROFILER: 'return' 1
PROFILER: 'c_call' <built-in method append of list object at 0x0000022125FC0B80>
PROFILER: 'c_return' <built-in method append of list object at 0x0000022125FC0B80>
PROFILER: 'return' [0, 1, 1]
PROFILER: 'c_call' <built-in function print>
[0, 1, 1]
PROFILER: 'c_return' <built-in function print>
PROFILER: 'return' None
```

