'''
Implement a class Veterinarian that will be used as a part of a larger simulation of a verterinarian office.

The class Veterinarian needs to be efficient with respect to time used and contain the following methods:
- accept(petName): puts the specified pet at the end of the line.
- heal(): removes the pet's name from the queue and returns it. If no pets are in the queue, an IndexError
exception should be raised

Example:

veterinarian = Veterinarian()
veterinarian.accept("Barkley")
veterinarian.accept("Mittens")
print(veterinarian.heal())
print(veterinarian.heal())

'''
from time import time
from collections import deque


class Veterinarian:
	def __init__(self):
		self.queue = []

	def accept(self, petName):
		self.queue.append(petName)

	def heal(self):
		return self.queue.pop(0)


class Veterinarian_2:
	def __init__(self):
		self.queue = deque()

	def accept(self, petName):
		self.queue.append(petName)

	def heal(self):
		return self.queue.popleft()


class Veterinarian_3:
	def __init__(self):
		self.queue = {}
		self.indEntry = 0
		self.indExit = 0

	def accept(self, petName):
		self.queue[self.indEntry] = petName
		self.indEntry += 1

	def heal(self):
		h = self.queue[self.indExit]
		self.indExit += 1
		return h

class Veterinarian_4:
	def __init__(self):
		self.queue = set()

	def accept(self, petName):
		self.queue.add(petName)

	def heal(self):
		return self.queue.pop()


# Tests
st = time()
for i in range(1000000):
	veterinarian = Veterinarian()
	veterinarian.accept("Barkley")
	veterinarian.accept("Mittens")
	v1 = veterinarian.heal()
	v2 = veterinarian.heal()
ft = time()
print("-"*80)
print("Lists: ", ft- st, "  	Values: ", v1, " | ", v2)
print("-"*80)

st = time()
for i in range(1000000):
	veterinarian = Veterinarian_2()
	veterinarian.accept("Barkley")
	veterinarian.accept("Mittens")
	v3 = veterinarian.heal()
	v4 = veterinarian.heal()
ft = time()
print("-"*80)
print("Deque: ", ft- st, "  	Values: ", v3, " | ", v4)
print("-"*80)

st = time()
for i in range(1000000):
	veterinarian = Veterinarian_3()
	veterinarian.accept("Barkley")
	veterinarian.accept("Mittens")
	v5 = veterinarian.heal()
	v6 = veterinarian.heal()
ft = time()
print("-"*80)
print("Dicts: ", ft- st, "  	Values: ", v5, " | ", v6)
print("-"*80)

st = time()
for i in range(1000000):
	veterinarian = Veterinarian_4()
	veterinarian.accept("Barkley")
	veterinarian.accept("Mittens")
	v7 = veterinarian.heal()
	v8 = veterinarian.heal()
ft = time()
print("-"*80)
print("Set: ", ft- st, "  	Values: ", v7, " | ", v8)
print("-"*80)



