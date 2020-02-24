import copy
import math

def lcm(a, b):
	return int((a * b) // math.gcd(a, b))

def add(axis):
	for i in range(0, len(moons)):
			moons[i][axis] += vel[i][axis]

def calcvel(axis):
	for i in range(0, len(moons)):
		for j in range(0, len(moons)):
			if i != j:
					if moons[i][axis] > moons[j][axis]:
						vel[i][axis] -= 1
					if moons[i][axis] < moons[j][axis]:
						vel[i][axis] += 1

def check(i):
	if vel[0][i] == 0 and vel[1][i] == 0 and vel[2][i] == 0 and vel[3][i] == 0:
		ok = 0
		for x in range(0, 4):
			if moons[x][i] == moons1[x][i]:
				ok += 1
		if ok == 4:
			return True
		else:
			return False
	else:
		return False



f = open("input12.txt", "r")

moons = []
moons1 = []
for i in f:
	temp = []
	moon = i.rstrip().strip("<>").split(",")
	for j in moon:
		temp.append(int(j.split("=")[1]))
	moons.append(temp)
moons1 = copy.deepcopy(moons)
f.close()

print("Successfully imported.")
for i in moons:
	print(i)
print("\n")

vel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
repeat = []

for i in range(0, 3):
	steps = 0
	cont = False
	while(not cont):
		steps += 1
		calcvel(i)
		add(i)
		if check(i):
			repeat.append(steps)
			print("Axis ", i, " calculated")
			print("Steps required: ", steps, "\n")
			cont = True


lcm1 = lcm(repeat[0], repeat[1])
print("LCM1: ", lcm1)
lcm2 = lcm(lcm1, repeat[2])
print("LCM2: ", lcm2, "\n")

print("Final answer: ", lcm2)