#!/usr/bin

# A simple script to simulate the chinese restaurant process to generate the partition of n-inputs.

import random

def chinese_restaurant_process(num_customers, alpha):
	if( num_customers <= 0):
		return []

	table_assignments = [1]
	next_open_table = 2
	for i in range(1, num_customers):
		random.seed()
		r=random.random()
		if (r < float(alpha)/(alpha+i)):
			table_assignments.append(next_open_table)
			next_open_table+=1
		else:
			which_table = table_assignments[random.randint(0, i-1)]
			table_assignments.append(which_table)

	return table_assignments

if __name__ == "__main__":
	print("Simulating chinese restaurant process")
	print(chinese_restaurant_process(10,5))
