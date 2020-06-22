'''
Given list of numbers, return the sum of the maximum two
'''
import time as t


def find_max_sum(numbers):
	max1 = max(numbers) # O(n)
	numbers.pop(numbers.index(max1)) # O(n)
	max2 = max(numbers) # O(n)
	return max1 + max2 # O(1)

def find_max_sum_2(numbers):
	numbers.sort() # O(n log n)
	return numbers[-2] + numbers[-1] #O(1)

def find_max_sum_3(numbers):
	max1 = 0; max2 = 0
	for i in numbers:					# O(n)
		if i > max1:
			max2 = max1
			max1 = i
		elif i > max2:
			max2 = i
	return max1 + max2 					# O(1)


# Test
print(find_max_sum([5, 9, 10 ,7, 5]))


st = t.time()
for i in range(100000):
	n1 = find_max_sum([5, 9, 10 ,7, 5])	
ft = t.time()

print("-"*40)
print("Max: ", ft- st)
print("-"*40)


st = t.time()
for i in range(100000):
	n2 = find_max_sum_2([5, 9, 10 ,7, 5])	
ft = t.time()

print("-"*40)
print("Sort: ", ft- st)
print("-"*40)

st = t.time()
for i in range(100000):
	n3 = find_max_sum_3([5, 9, 10 ,7, 5])	
ft = t.time()

print("-"*40)
print("Window: ", ft- st)
print("-"*40)

print("Values: ", n1, " | ", n2, " | ", n3)