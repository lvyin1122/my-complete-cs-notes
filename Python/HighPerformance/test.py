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