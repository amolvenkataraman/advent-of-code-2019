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

def intcode(res):
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
		inp[c2] = int(input())
		skip = 2
	elif c1 == 4:
		print(inp[c2])
		skip = 2
	else:
		raise SystemExit
	return skip


f = open("input5.txt", "r")

for i in f:
	inp1 = i.split(",")
f.close()

inp = []
for i in inp1:
	inp.append(int(i))

ind = 0
skip = 4

while(ind < len(inp)):
	res = param(ind)
	skip = intcode(res)
	ind += skip