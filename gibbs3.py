#Simulating a bivariate normal using gibbs sampling.
#standard normal distribution.

import math
import matplotlib.pyplot as plt
import random

def snd(arg1):
	f=1/(math.pi*2)**2
	denominator=100
	x=float(arg1)/denominator
	val = f*math.e**(-1*(x**2)/2)
	return val

def simulate_normal():
	print('hello, testing normal distributions.')
	f_x=[0 for i in range(0,201)]
	x=[i for i in range(-100,101)]
	count=0
	for i in range(-100,101):
		f_x[count]=snd(i)
		count+=1
	plt.plot(x,f_x)
	plt.show()

# X|Y = rho*y + math.sqrt(1-rho*rho)*snd(1)
# Y|X = rho*x + math.sqrt(1-rho*rho)*snd(1)

def simulate_gibbs():
	n=input('Number of samples to be collected : ')
	x=[i for i in range(0,n)]
	y=[i for i in range(0,n)]
	rho=0.9
	c=math.sqrt(1-rho**2)
	for i in range(1,n):
		x[i]=rho*y[i-1] + c*random.gauss(0,1)
		y[i]=rho*x[i] + c*random.gauss(0,1)
	f, axarr=plt.subplots(2, sharex=True)
	axarr[0].plot(x[0:n],y[0:n],'r.')
	axarr[1].plot(x[0:n],y[0:n])
	print(sum(x)/n) # calculate the mean at this point, to see whether it matches with the input mean.
	plt.show()

def simulate_example():
	B=5
	print('B = '+str(B))
	x_axis=[(float(i)/100)*5 for i in range(1,101)]
	vals=[0 for i in range(1,101)]
	for i in range(1,101):
	 for j in range(1,101):
	  x=(float(i)/100)*5
	  y=(float(j)/100)*5
	  vals[i-1]+=y*math.e**(-1*y*x)
	 vals[i-1]/=100
	plt.plot(x_axis, vals)
	plt.show()


if __name__ == "__main__":
#	simulate_normal()
#	simulate_gibbs()
	simulate_example()
