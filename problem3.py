'''
Design a data structure that can, efficiently with respect to time used, store and check, if the total of any
three successively added elements is equal to a given total.

For example, MovingTotal() creates an emptry container with no existing totals.
append([1,2,3]) appends elements [1,2,3], with means that there is only one existing total (1+2+3=6)
Append([4]) appends element 4 and creates an additional total from [2,3,4]. There would now be two totals 
(1+2+3=6 and 2+3+4=9). At this point contains(6) and contains(9) should return True, while contains(7) 
should return False
'''
import time as t

class MovingTotal():
	def __init__(self):
		self.elements = []
		self.totals = {}

	def append(self, numbers):
		for i in numbers:
			self.elements.append(i)

		n = 3 if len(self.elements) > 3 else len(self.elements) 
		self.totals[sum(self.elements[-n:])] = True

	def contains(self, total):
		return self.totals.get(total, False)


st = t.time()
for i in range(100000):
	mt = MovingTotal()
	mt.append([1,2,3])
	mt.append([4])
	s1 = mt.contains(6)
	s2 = mt.contains(9)
	s3 = mt.contains(7)
ft = t.time()

print("-"*80)
print("Solution: ", ft-st, " | ", s1, " | ", s2, " | ",s3)
print("-"*80)