#!/usr/bin

# A simple script to simulate the stick breaking process to generate Dirichlet distribution.

import random

def simulate(n, alpha, iterations):
	SUM=0
	for j in alpha:
		SUM+=j
	l=len(alpha)
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
			prod*=(1-variates[j])
		sample.append(1-sum(sample))
	 	print(sample)	 

if __name__ == "__main__":
	n = input("Enter the number of stick parts to be created: ")
	alpha = list()
	for i in range(int(n)):
		alpha.append(input("value for alpha " + `i` + ": "))
	iterations = input("Number of iterations: ")
	simulate(n, alpha, iterations); #function to simulate stick breaking process.
