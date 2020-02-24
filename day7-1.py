def param(ind):
	opcode = str(inp[ind])
	param = int(opcode[-1])
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
		else:
			c2 = ind + 1
	else:
		c2 = 0

	if len(inp) > (ind + 2):
		if b == 0:
			c3 = inp[ind + 2]
		else:
			c3 = ind + 2
	else:
		c3 = 0

	if len(inp) > (ind + 3):
		if a == 0:
			c4 = inp[ind + 3]
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

def intcode(res, ind, inp1, inp2):
	c1 = res[0]
	c2 = res[1]
	c3 = res[2]
	c4 = res[3]

	global exit
	global inpcount
	global out

	if c1 == 1:
		inp[c4] = inp[c2] + inp[c3]
		skip = 4
	elif c1 == 2:
		inp[c4] = inp[c2] * inp[c3]
		skip = 4
	elif c1 == 3:
		if inpcount == 0:
			inp[c2] = int(inp1)
		else:
			inp[c2] = int(inp2)
		inpcount += 1
		skip = 2
	elif c1 == 4:
		out = inp[c2]
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
	else:
		exit = True
		skip = 0
	return skip

def run(inp1, inp2):
	global exit
	global inpcount
	global out
	global inp
	exit = False
	inpcount = 0
	out = 0

	inp = []
	for i in inpx:
		inp.append(i)

	ind = 0
	inpcount = 0
	while(ind < len(inp)):
		res = param(ind)
		skip = intcode(res, ind, inp1, inp2)
		if exit:
			break
		ind += skip
	return out

f = open("input7.txt", "r")

for i in f:
	inp1 = i.split(",")
f.close()

inp = []
inpx = []
for i in inp1:
	inp.append(int(i))
	inpx.append(int(i))

inpcount = 0
out = 0
exit = False

thrust = []

for a in range(0, 5):
	for b in range(0, 5):
		if b != a:
			for c in range(0, 5):
				if c != b and c != a:
					for d in range(0, 5):
						if d != c and d != b and d != a:
							for e in range(0, 5):
								if e != d and e != c and e != b and e != a:
									run(a, 0)
									run(b, out)
									run(c, out)
									run(d, out)
									run(e, out)

									thrust.append(out)

print(max(thrust))