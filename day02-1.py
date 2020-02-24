f = open("input2.txt", "r")

for i in f:
	inp = i.split(",")
f.close()

ind = 0

inp[1] = 12
inp[2] = 2

while(True):
	c1 = int(inp[ind])
	c2 = int(inp[ind + 1])
	c3 = int(inp[ind + 2])
	c4 = int(inp[ind + 3])

	if c1 == 1:
		inp[c4] = int(inp[c2]) + int(inp[c3])
	elif c1 == 2:
		inp[c4] = int(inp[c2]) * int(inp[c3])
	elif c1 == 99:
		print(inp[0])
		raise SystemExit
	ind += 4