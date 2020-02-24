import math

def calcfuel (i):
	n = math.floor(i / 3) - 2
	return(n)

f = open("input1.txt", "r")
sum = 0
for i in f:
	sum += calcfuel(int(i))

print(sum)
f.close()