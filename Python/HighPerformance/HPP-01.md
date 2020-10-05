# High Performance Python - Ch.2

CPU-bound problems



## Use timeit module
```
$ python -m timeit -n 5 -r 5 -s "import julia1"
 "julia1.calc_pure_python(desired_width=1000,
 max_iterations=300)"
```

Output:
```
C:\Users\heyu.wang\.git_projects\my-complete-cs-notes\Python\HighPerformance>python -m timeit -s "import julia_set_main" "julia_set_main.calc_pure_python(desired_width=1000, max_iterations=300)"
Length of x: 1000
Total elements: 1000000
@timefn: calculate_z_serial_purepython took 8.623921871185303 seconds
Length of x: 1000
Total elements: 1000000
@timefn: calculate_z_serial_purepython took 6.632766485214233 seconds
Length of x: 1000
Total elements: 1000000
@timefn: calculate_z_serial_purepython took 6.718905210494995 seconds
Length of x: 1000
Total elements: 1000000
@timefn: calculate_z_serial_purepython took 6.642599105834961 seconds
Length of x: 1000
Total elements: 1000000
@timefn: calculate_z_serial_purepython took 6.606563091278076 seconds
Length of x: 1000
Total elements: 1000000
@timefn: calculate_z_serial_purepython took 6.954281806945801 seconds
1 loop, best of 5: 6.97 sec per loop
```
Inside IPython
```
%timeit calc_pure_python(desired_width=1000, max_iterations=300)
```

## time in Unix shell
```
$ /usr/bin/time --verbose python julia1_nopil.py
Length of x: 1000
Total elements: 1000000
calculate_z_serial_purepython took 12.3145110607 seconds
    Command being timed: "python julia1_nopil.py"
    User time (seconds): 13.46
    System time (seconds): 0.05
    Percent of CPU this job got: 99%
    Elapsed (wall clock) time (h:mm:ss or m:ss): 0:13.53
    Average shared text size (kbytes): 0
    Average unshared data size (kbytes): 0
    Average stack size (kbytes): 0
    Average total size (kbytes): 0
    Maximum resident set size (kbytes): 131952
    Average resident set size (kbytes): 0
    Major (requiring I/O) page faults: 0
    Minor (reclaiming a frame) page faults: 58974
    Voluntary context switches: 3
    Involuntary context switches: 26
    Swaps: 0
    File system inputs: 0
    File system outputs: 1968
    Socket messages sent: 0
    Socket messages received: 0
    Signals delivered: 0
    Page size (bytes): 4096
    Exit status: 0
```

## cProfile Module

```
python -m cProfile -s cumulative julia2.py
python -m cProfile -o profile.stats julia2.py
```

Output:
```
         36222012 function calls in 14.063 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   14.063   14.063 {built-in method builtins.exec}
        1    0.024    0.024   14.063   14.063 julia2.py:1(<module>)
        1    0.892    0.892   14.039   14.039 julia2.py:20(calc_pure_python)
        1    0.000    0.000   12.808   12.808 julia2.py:7(measure_time)
        1    8.426    8.426   12.808   12.808 julia2.py:59(calculate_z_serial_purepython)
 34219980    4.382    0.000    4.382    0.000 {built-in method builtins.abs}
  2002000    0.331    0.000    0.331    0.000 {method 'append' of 'list' objects}
        1    0.007    0.007    0.007    0.007 {built-in method builtins.sum}
        3    0.001    0.000    0.001    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 julia2.py:6(timefn)
        1    0.000    0.000    0.000    0.000 functools.py:34(update_wrapper)
        1    0.000    0.000    0.000    0.000 functools.py:64(wraps)
        7    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        2    0.000    0.000    0.000    0.000 {built-in method time.time}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        5    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
        1    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

## Use runsnakerun to visualize cProfile

## line_profiler

## memory_profiler

```python
@profile
def calculate_z_serial_purepython(maxiter, zs, cs):
    """Calculate output list using Julia update rule"""
    with profile.timestamp("create_output_list"):
        output = [0] * len(zs)
    time.sleep(1)
    with profile.timestamp("create_range_of_zs"):
        iterations = range(len(zs))
        with profile.timestamp("calculate_output"):
            for i in iterations:
                n = 0
                z = zs[i]
                c = cs[i]
                while n < maxiter and abs(z) < 2:
                    z = z * z + c
                    n += 1
                output[i] = n
    return output
```

## heapy - inspecting objects

## dowser - live graphing

## dis - CPython Bytecode

## Unit testing

