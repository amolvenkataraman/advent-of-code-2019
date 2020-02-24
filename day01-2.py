import math

def calcfuel (i):
	n = math.floor(i / 3) - 2
	return(n)

f = open("input1.txt", "r")
sum = 0
for i in f:
	mass = int(i)
	while (mass > 0):
		mass = calcfuel(mass)
		if (mass > 0):
			sum += mass

print(sum)
f.colse()