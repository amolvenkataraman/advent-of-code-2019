import copy

def param(ind):
	global base
	global exit
	opcode = str(inp[ind])
	param = int(opcode[-1])
	if opcode[-2:] == "99":
		exit = True

	try:
		param += int(opcode[-2] * 10)
	except:
		param += 0

	try:
		c = int(opcode[-3])
	except IndexError:
		c = 0

	try:
		b = int(opcode[-4])
	except IndexError:
		b = 0

	try:
		a = int(opcode[-5])
	except IndexError:
		a = 0
	
	c1 = param

	if len(inp) > (ind + 1):
		if c == 0:
			c2 = inp[ind + 1]
		elif c == 2:
			tempc = inp[ind + 1]
			c2 = base + tempc
		else:
			c2 = ind + 1
	else:
		c2 = 0

	if len(inp) > (ind + 2):
		if b == 0:
			c3 = inp[ind + 2]
		elif b == 2:
			tempc = inp[ind + 2]
			c3 = base + tempc
		else:
			c3 = ind + 2
	else:
		c3 = 0

	if len(inp) > (ind + 3):
		if a == 0:
			c4 = inp[ind + 3]
		elif a == 2:
			tempc = inp[ind + 3]
			c4 = base + tempc
		else:
			c4 = ind + 3
	else:
		c4 = 0

	res = []
	res.append(c1)
	res.append(c2)
	res.append(c3)
	res.append(c4)
	return res

def intcode(res, ind):
	global base
	global valin
	global valout
	global valout1
	global outs
	c1 = res[0]
	c2 = res[1]
	c3 = res[2]
	c4 = res[3]

	if c1 == 1:
		inp[c4] = inp[c2] + inp[c3]
		skip = 4
	elif c1 == 2:
		inp[c4] = inp[c2] * inp[c3]
		skip = 4
	elif c1 == 3:
		inp[c2] = valin
		skip = 2
	elif c1 == 4:
		if outs == 0:
			valout = inp[c2]
		else:
			valout1 = inp[c2]
		outs += 1
		skip = 2
	elif c1 == 5:
		if inp[c2] != 0:
			skip = inp[c3] - ind
		else:
			skip = 3
	elif c1 == 6:
		if inp[c2] == 0:
			skip = inp[c3] - ind
		else:
			skip = 3
	elif c1 == 7:
		if inp[c2] < inp[c3]:
			inp[c4] = 1
		else:
			inp[c4] = 0
		skip = 4
	elif c1 == 8:
		if inp[c2] == inp[c3]:
			inp[c4] = 1
		else:
			inp[c4] = 0
		skip = 4
	elif c1 == 9:
		base += inp[c2]
		skip = 2
	return skip


f = open("input11.txt", "r")

for i in f:
	inp1 = i.split(",")
f.close()

inp = []
for i in inp1:
	inp.append(int(i))

print("Successfully imported")
print(inp)

for i in range(0, 1000000):
	inp.append(i)

ind = 0
skip = 0
base = 0
outs = 0

valin = 1
valout = 0
valout1 = 0
panels = 0
exit = False

coord = [0, 0]
facing = "U"
whitepanels = []
paintedpanels = []

whitepanels.append(copy.deepcopy(coord))

while(ind < len(inp)):
	res = param(ind)
	if exit == True:
		break
	skip = intcode(res, ind)
	ind += skip


	if outs == 2:
		outs = 0
		if coord not in paintedpanels:
			panels += 1
			paintedpanels.append(copy.deepcopy(coord))
		if valout == 1:
			if coord not in whitepanels:
				whitepanels.append(copy.deepcopy(coord))
		elif valout == 0:
			if coord in whitepanels:
				whitepanels.remove(coord)

		if valout1 == 0:
			if facing == "U":
				facing = "L"
			elif facing == "L":
				facing = "D"
			elif facing == "D":
				facing = "R"
			elif facing == "R":
				facing = "U"
		elif valout1 == 1:
			if facing == "U":
				facing = "R"
			elif facing == "R":
				facing = "D"
			elif facing == "D":
				facing = "L"
			elif facing == "L":
				facing = "U"

		if facing == "U":
			coord[1] += 1
		elif facing == "R":
			coord[0] += 1
		elif facing == "D":
			coord[1] -= 1
		elif facing == "L":
			coord[0] -= 1

		if coord in whitepanels:
			valin = 1
		else:
			valin = 0

print("Part 1: ", panels)

whitex = []
for i in whitepanels:
	whitex.append(i[0])

whitey = []
for i in whitepanels:
	whitey.append(i[1])

ans = []

for i in range(max(whitey), min(whitey) -1, -1):
	temp = []
	print("I: ", i)
	for j in whitepanels:
		if j[1] == i:
			temp.append(copy.deepcopy(j[0]))
	if temp != []:
		print(temp)
		ans.append(copy.deepcopy(sorted(temp)))

print(ans)
print("min", min(whitex))
print("max", max(whitex))
print("\n\n\n")

for i in ans:
	#print(i)
	for j in range(min(whitex), max(whitex)):
		if j in i:
			print("#", end="")
		else:
			print(" ", end="")
	print()