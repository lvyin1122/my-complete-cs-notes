# Docs

# 1. Intro

```python
import simpy

def clock(env, name, tick):
    while True:
        print(name, env.now)
        yield env.timeout(tick)
        
env = simpy.Environment()
env.process(clock(env, 'fast', 0.5))

```

# 2. Get Started


## Basic Concepts

process-based discrete-event simluation framework

Processes: behaviours of active componenets
Environment
Events

```python
def car(env):
    while True:
        print('Start parking at %d' % env.now)
        parking_duration = 5
        yield env.timeout(parking_duration)

        print('Start driving at %d' % env.now)
        trip_duration = 2
        yield env.timeout(trip_duration)
```

## Process Interaction

```python
class Car(object):
    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())
        
    def run(self):
        while True:
            print('Start parking and charging at %d' % self.env.now)
            charge_duration = 5
            yield self.env.process(self.charge(charge_duration))
            
            print('Start driving at %d' % self.env.now)
            trip_duration = 2
            yield self.env.timeout(trip_duration)
            
    def charge(self, duration):
        yield self.env.timeout(duration)
```
