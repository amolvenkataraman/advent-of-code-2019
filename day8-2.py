wide = 25
tall = 6

f = open("input8.txt", "r")

for i in f:
	inp = i
f.close()

layers = int(len(inp) / (wide * tall))
layer = []
layer1 = []

ind = 0
for i in range(0, layers):
	temp = []
	tempx = []
	for j in range(0, tall):
		temp1 = []
		for k in range(0, wide):
			temp1.append(inp[ind])
			tempx.append(inp[ind])
			ind += 1
		temp.append(temp1)
	layer.append(temp)
	layer1.append(tempx)

for i in range(0, tall):
	for j in range(0, wide):
		ok = True
		for k in range(0, layers):
			if layer[k][i][j] != "2":
				if ok:
					#print(layer[k][i][j], end="")
					if layer[k][i][j] == "1":
						print("#", end="")
					else:
						print(" ", end="")
					ok = False
	print()