def addup(n):
	k = 0
	for i in range(1, n + 1):
		k += i
	return k

f = open("input6.txt", "r")

inp = []
inp1 = []
for i in f:
	inp.append(i.split(")")[0].strip())
	inp1.append(i.split(")")[1].strip())
f.close()

inp2 = []
for i in inp:
	if i != "COM":
		inp2.append(i)
	for i in inp1:
		if i not in inp2:
			inp2.append(i)

checked = []
end = []
orbit = 0
planet = ""
for i in inp2:
	if i not in checked:
		planet = i
		checked.append(i)
		while planet in inp:
			for j in range(0, len(inp)):
				if inp[j] == planet: 
					planet = inp1[j]
		if planet not in end:
			end.append(planet)

plan = []

for i in end:
	orb = 0
	planet = i
	canc = 0
	while planet in inp1:
		dup = []
		for j in range(0, len(inp)):
			if inp1[j] == planet:
				for a in range(0, len(plan)):
					if plan[a][0] == inp[j] and plan[a][1] == inp1[j]:
						if plan[a] not in dup:
							canc += 1
							dup.append(plan[a])
				orb += 1
				temp = []
				temp.append(inp[j])
				temp.append(inp1[j])
				plan.append(temp)
				planet = inp[j]
 
	orbit += addup(orb) - addup(canc)


print(orbit)