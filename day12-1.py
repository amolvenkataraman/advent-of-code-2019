def add():
	for i in range(0, len(moons)):
		for j in range(0, len(moons[i])):
			moons[i][j] += vel[i][j]

def calcvel():
	for i in range(0, len(moons)):
		for j in range(0, len(moons)):
			if i != j:
				for k in range(0, len(moons[i])):
					if moons[i][k] > moons[j][k]:
						vel[i][k] -= 1
					if moons[i][k] < moons[j][k]:
						vel[i][k] += 1

def energy():
	energy = 0
	for i in range(0, len(moons)):
		pot = 0
		kin = 0
		for j in range(0, len(moons[i])):
			pot += abs(moons[i][j])
			kin += abs(vel[i][j])
		energy += pot * kin
	return energy

f = open("input12.txt", "r")

moons = []
for i in f:
	temp = []
	moon = i.rstrip().strip("<>").split(",")
	for j in moon:
		temp.append(int(j.split("=")[1]))
	moons.append(temp)
f.close()

vel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 1000):
	calcvel()
	add()

print(energy())