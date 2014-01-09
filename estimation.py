#!/bin

#
#	A simple porgram to simuluate the coin toss experiment and calculate various probabilistic measures.
#

import random

# 0 = head
# 1 = tail

def MLE(iterations):
	toss = list()
	count=0
	parameter = list()
	for i in range(iterations):
		random.seed()
		if(random.random() <= 0.5):
			toss.append(0) # a head has occured.
			count+=1
		else:
		       	toss.append(1)
		parameter.append(float(count)/(i+1))
	formattedParameter = 	[ '%.2f' % elem for elem in parameter ]
	print(formattedParameter)
	print(toss)
	P=list()
	for p1 in range (0,int(1.05/0.05)):
		# probability function defined based upon bernouli's distribution.
		P.append(float(((p1*0.05)**count)*((1-(p1*0.05))**(iterations-count)))) #print(['%.2f' % elem for elem in P])
	
	maxIndex = 0
	currmax = P[0]
	for i in range(len(P)):
		if P[maxIndex] < P[i]:
			maxIndex=i
	print("probability of next number being a head is: " + str(maxIndex*0.05))

if __name__ == "__main__":
	print("estimating things like never before")
	MLE(15)
