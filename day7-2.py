import copy

def param(amp, ind):
	global base
	global exit
	global inp
	global ampind

	ind = ampind[amp]

	opcode = str(inp[amp][ind])
	param = int(opcode[-1])

	if opcode[-2:] == "99":
		exit = True
		return []

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

	if len(inp[amp]) > (ind + 1):
		if c == 0:
			c2 = inp[amp][ind + 1]
		elif c == 2:
			tempc = inp[amp][ind + 1]
			c2 = base + tempc
		else:
			c2 = ind + 1
	else:
		c2 = 0

	if len(inp[amp]) > (ind + 2):
		if b == 0:
			c3 = inp[amp][ind + 2]
		elif b == 2:
			tempc = inp[amp][ind + 2]
			c3 = base + tempc
		else:
			c3 = ind + 2
	else:
		c3 = 0

	if len(inp[amp]) > (ind + 3):
		if a == 0:
			c4 = inp[amp][ind + 3]
		elif a == 2:
			tempc = inp[amp][ind + 3]
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

def intcode(amp, res, ind, inp1, inp2):
	c1 = res[0]
	c2 = res[1]
	c3 = res[2]
	c4 = res[3]

	global base
	global exit
	global inpcount
	global out
	global outchanged
	global inp

	if c1 == 1:
		inp[amp][c4] = inp[amp][c2] + inp[amp][c3]
		skip = 4
	elif c1 == 2:
		inp[amp][c4] = inp[amp][c2] * inp[amp][c3]
		skip = 4
	elif c1 == 3:
		if inpcount[amp] == 0:
			inp[amp][c2] = int(inp1)
		else:
			inp[amp][c2] = int(inp2)
		inpcount[amp] += 1
		skip = 2
	elif c1 == 4:
		out = inp[amp][c2]
		outchanged = True
		print(inp[amp][c2])
		skip = 2
	elif c1 == 5:
		if inp[amp][c2] != 0:
			skip = inp[amp][c3] - ind
		else:
			skip = 3
	elif c1 == 6:
		if inp[amp][c2] == 0:
			skip = inp[amp][c3] - ind
		else:
			skip = 3
	elif c1 == 7:
		if inp[amp][c2] < inp[amp][c3]:
			inp[amp][c4] = 1
		else:
			inp[amp][c4] = 0
		skip = 4
	elif c1 == 8:
		if inp[amp][c2] == inp[amp][c3]:
			inp[amp][c4] = 1
		else:
			inp[amp][c4] = 0
		skip = 4
	elif c1 == 9:
		base += inp[amp][c2]
		skip = 2
	else:
		skip = 1
	return skip

def run(amp, inp1, inp2):
	global ampind
	global exit
	global inpcount
	global out
	global outchanged
	global inp

	ind = ampind[amp]

	while(ind < len(inp[amp])):
		res = param(amp, ind)
		if exit == True:
			break
		skip = intcode(amp, res, ind, inp1, inp2)
		ind += skip

		ampind[amp] = ind
		if outchanged == True:
			outchanged = False
			break
	return out

def phase(ampphase):
	global ampind
	global inpcount
	global out
	global outchanged
	global exit

	while exit == False:
		for i in range(0, 5):
			print("amp: ", i)
			out1 = run(i, ampphase[i], out)
			out = copy.deepcopy(out1)
				
	for i in range(0, 5):
		inp[i] = []
		for j in inp[5]:
			inp[i].append(j)

	for i in range(0, 5):
		ampind[i] = 0

	inpcount = [0, 0, 0, 0, 0]
	outchanged = False
	exit = False
	print("out: ", out)
	return out


f = open("input7.txt", "r")

inp0 = []
for i in f:
	inp0.append(i.rstrip().split(","))
f.close()

inp1 = []
for i in inp0:
	for j in i:
		if j != '':
			inp1.append(j)

inp = [[], [], [], [], [], []]
for i in range(0, 6):
	for j in inp1:
		inp[i].append(copy.deepcopy(int(j)))
	for j in range(0, 100000):
		inp[i].append(copy.deepcopy(j))

ampind = [0, 0, 0, 0, 0]
inpcount = [0, 0, 0, 0, 0]
out = 0
base = 0
outchanged = False
exit = False

outs = []

for a in range(5, 10):
	for b in range(5, 10):
		if b != a:
			for c in range(5, 10):
				if c != b and c != a:
					for d in range(5, 10):
						if d != c and d != b and d != a:
							for e in range(5, 10):
								if e != d and e != c and e != b and e != a:
									print(a, b, c, d, e)
									temp = phase([a, b, c, d, e])
									outs.append(temp)
									out = 0

print(outs)
print(max(outs))