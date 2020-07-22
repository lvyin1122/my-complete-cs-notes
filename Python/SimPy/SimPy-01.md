# SimPy-01

# 1. An Introudction to Discrete-Event Simulation Programming

step function

parallel programming

progress simultaneously

languages or paradigms

## The Activity-Oriented Paradigm

jobs arrives at random time

continuous random variables

- break time into increments
- look around all the activities
- goal: average waiting time

```
QueueLength = 0
NJobsServed = 0
SumResidenceTimes = 0
ServerBusy = false
generate NextArrivalTime // random # generation
NIncrements = MaxSimTime / 0.001
for SimTime = 1*0.001 to NIncrements*0.001 do
    if SimTime = NextArrivalTime then
        add new jobobject to queue
        QueueLength++
        generate NextArrivalTime // random # generation
        if not ServerBusy then
            ServerBusy = true
            jobobject.ArrivalTime = SimTime
            generate ServiceFinishedtime
            currentjob = jobobject
            delete head of queue and assign to currentjob
            QueueLength--
    else
        if SimTime = ServiceFinishedtime then
            NJobsServed++
            SumResidenceTimes += SimTime - currentjob.ArrivalTime
            if QueueLength > 0 then
                generate ServiceFinishedtime // random # generation
                delete currentjob from queue
                QueueLength--
            else
                ServerBusy = false
print out SumResidenceTimes / NJobsServed
```

Slow, wasting processor time


## The Event-Oriented Paradigm

![image](CE3F397423DB42178169068BB732E50A)

event set: the set of all pending events

at least one event pending, the next arrival

update the SimTime to the minimum among the scheduled pending events

## The Process-Oriented Paradigm

application-specific threads

### Arrivals Thread

![image](85F458FD1F084D3788198131558F713A)

![image](6A1ACB87E8A7449B851C477A13E7CF8F)


### Server Thread

![image](B01B64152BE0496BA3F949EC0E52DFAB)

### Event Manager

![image](8E13CB8E7C9840CBA37D08B6E3E53BD0)

### Main Function

![image](94A7CEEF39074B139821A855D706540D)

# 2. Introduction to the SimPy Simulation Language

Python's generators capability

prematuraly exited and then later re-entered at the point of the last exit: **coroutines** => thread

## Overview

### Classes
- Process: simulates an entity which evolves time
- Resource: simulates something to be queued for

### Functions:

```python
activate()
simulate()
yield hold
yield request
yield release
yield passivate
```

## Real Python Tutorial


1. Establish an environment
2. Pass in the parameters
3. Run the simluation

```python
# Set up the environment
env = simpy.Environment()

# Assume you've defined checkpoint_run() beforehand
env.process(checkpoint_run(env, num_booths, check_time, passenger_arrival))

# Let's go!
env.run(until=10)
```

Implementation: Theater

```python
class Theater(object):
    def __init__(self, env, num_cashiers):
        self.env = env
        self.cashier = simpy.Resource(env, num_cashiers)

    def purchase_ticket(self, moviegoer):
        yield self.env.timeout(random.randint(1, 3))
```



