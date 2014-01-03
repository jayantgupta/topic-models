#!/usr/bin

import random

a=[2,4,10]

for i in range(10):
	print "hello"
	u1 = random.betavariate(2,14)
	u2 = random.betavariate(4,10)
	sample = [u1, (1-u1)*u2, 1-u1 - (1-u1)*u2]
	print(sample)
