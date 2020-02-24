def intcode (noun, verb):
	ind = 0
	inp[1] = noun
	inp[2] = verb

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
			return int(inp[0])
		ind += 4

f = open("input2.txt", "r")

for i in f:
	inp = i.split(",")
	inp1 = i.split(",")
f.close()

for i in range (0, 100):
	for j in range (0, 100):
		k = intcode (i, j)
		if k == 19690720:
			print ((100 * i) + j)
			raise SystemExit
		for l in range(0, len(inp)):
			inp[l] = inp1[l]