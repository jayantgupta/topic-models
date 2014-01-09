#!/usr/bin
# A simple script to simulate the stick breaking process to generate Dirichlet distribution.
# It outputs the final distribution based on the number of alpha values as the number of iterations increase
# the dirichlet tends towards more theoretical accuracy.

import random

def simulate(n, alpha, iterations):
	SUM=0
	for j in alpha:
		SUM+=j
	l=len(alpha)
	avgValues = list()
	for i in range(0, l):
		avgValues.append(0)
	for i in range(iterations):
		alphaSum=SUM
		variates=list()
		for j in range(l-1):
			variates.append(random.betavariate(alpha[j], alphaSum-alpha[j]))
			alphaSum-=alpha[j]
		#print(variates) // uncomment this to print variates.
		prod=1
		sample = list() 
		for j in range(l-1):
			sample.append(variates[j]*prod)
			avgValues[j]+=variates[j]*prod
			prod*=(1-variates[j])
		avgValues[l-1]+=(1-sum(sample)) #the order is important here...
		sample.append(1-sum(sample))
	for i in range(0,l):
		avgValues[i]/=iterations
	print(avgValues)

#print(sample)	 

if __name__ == "__main__":
	n = input("Enter the number of stick parts to be created: ")
	alpha = list()
	for i in range(int(n)):
		alpha.append(input("value for alpha " + `i` + ": "))
	iterations = input("Number of iterations: ")
	simulate(n, alpha, iterations); #function to simulate stick breaking process.
