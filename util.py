import numpy as np
import csv

# given cities
cities = []
#solution
sol = []

# Euclidean distance measuring function
def distance(x,y):
	dist = np.linalg.norm(np.array(x)-np.array(y))
	return dist
	
# 1. get solution sequence and reordering (sort from 0)
with open('example_solution.csv', mode='r', newline='') as solution:
	
	# read solution sequence
	reader = csv.reader(solution)
	for row in reader:
		sol.append(int(row[0]))
		
	#reordering solution sequence
	idx = sol.index(0)
	
	front = sol[idx:]
	back = sol[0:idx]
	
	sol = front + back
	
	# expand 0 city (start) for simplicity
	sol.append(int(0))
	
# 2. get TSP city map
with open('2024_AI_TSP.csv', mode='r', newline='') as tsp:
	# read TSP city map
	reader = csv.reader(tsp)
	for row in reader:
		cities.append(row)
		
# 3. evaluate solution cost
total_cost = 0

for idx in range(len(sol)-1):

	# get city positions
	pos_city_1 = [float(cities[sol[idx]][0]), float(cities[sol[idx]][0])]
	pos_city_2 = [float(cities[sol[idx+1]][0]), float(cities[sol[idx+1]][0])]
	
	# distance calculation
	dist = distance(pos_city_1, pos_city_2)
	
	# accumulation
	total_cost += dist
	
print('final cost: ' + str(total_cost))