from collections import deque
from enum import Enum

class Pulse(Enum):
    LOW = 0
    HIGH = 1

class State(Enum):
    OFF = 0
    ON = 1

class FlipFlop:
    def __init__(self, destinations):
        self.state = State.OFF
        self.destinations = destinations
    def HandlePulse(self, pulse, src):
        if pulse == Pulse.LOW:
            self.state = State.ON if self.state == State.OFF else State.OFF
            return Pulse.HIGH if self.state == State.ON else Pulse.LOW
        else:
            return None

class Conjunction:
    def __init__(self, destinations):
        self.inputs = {}
        self.destinations = destinations
    def HandlePulse(self, pulse, src):
        assert src in self.inputs
        self.inputs[src] = pulse
        return Pulse.HIGH if Pulse.LOW in self.inputs.values() else Pulse.LOW

class Broadcast:
    def __init__(self, destinations):
        self.destinations = destinations
    def HandlePulse(self, pulse, src):
        return pulse

def GetInput(filename):
    lines = []
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    modules = {}
    untyped = {}

    # First pass adds all modules
    for line in lines:
        # print(line)
        toks = line.split(' -> ')
        if toks[0][0] == '%':
            id = toks[0][1:]
            dests = toks[1].split(', ')
            # print(f'ID = {id}, Type=FlipFlop, dests={dests}')
            modules[id] = FlipFlop(dests)
        elif toks[0][0] == '&':
            id = toks[0][1:]
            dests = toks[1].split(', ')
            # print(f'ID = {id}, Type=Conjunction, dests={dests}')
            assert id not in modules
            modules[id] = Conjunction(dests)
        else:
            id = toks[0]
            assert id == 'broadcaster'
            assert id not in modules
            dests = toks[1].split(', ')
            # print(f'ID = {id}, Type=Broadcast, dests={dests}')
            modules[id] = Broadcast(dests)
        # print()
   
    # Second pass adds inputs to conjunctions
    for k, v in modules.items():
        for destId in v.destinations:
            if destId in modules:
                if isinstance(modules[destId], Conjunction):
                    modules[destId].inputs[k] = Pulse.LOW
                    # print(f'Added {k} as an input to Conjunction {destId}')
            else: 
                untyped[destId] = None
                print(f'Added untyped module {destId}')

    return modules, untyped

def PushButton(modules, untyped, count):
    low = 0
    high = 0

    for i in range(count):
        print(f'\n***** Button Push {i+1} *****')
        pulses = deque()
        pulses.append((Pulse.LOW, 'button', 'broadcaster'))
        rxLowCount = 0
        while len(pulses) > 0:
            pulseData = pulses.popleft()
            pulseType = pulseData[0]
            pulseSrc = pulseData[1]
            pulseDest = pulseData[2]
            if pulseType == Pulse.LOW:
                low += 1
            elif pulseType == Pulse.HIGH:
                high += 1
            print(f'{pulseSrc} -{pulseType.name}-> {pulseDest}')
            if pulseDest in modules:
                module = modules[pulseDest]
                output = module.HandlePulse(pulseType, pulseSrc)
                if output:
                    for dest in module.destinations:
                        newSrc = pulseDest
                        pulses.append((output, newSrc, dest))
            else:
                assert pulseDest in untyped
                if pulseType == Pulse.LOW:
                    rxLowCount += 1
        if (i+1) % 1000 == 0:
            print(f'Button Push {i+1}: RxLowCount = {rxLowCount}')
        # if rxLowCount == 1:
            # print(f'Button Push {i+1}: RxLowCount = {rxLowCount}')
            # return -1, -1
        input()

    return low, high

def Day20():
    modules, untyped = GetInput('input.txt')
    low, high = PushButton(modules, untyped, 1000)
    print(f'\nLow = {low}, High = {high}, Result = {low * high}')

Day20()