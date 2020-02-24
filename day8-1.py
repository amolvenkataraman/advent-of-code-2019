def countnum(n, arr):
	count = 0
	for i in arr:
		if i == n:
			count += 1
	return count

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

zeroes = []
ones = []
twos = []

for i in layer1:
	zeroes.append(countnum('0', i)) 
	ones.append(countnum('1', i))
	twos.append(countnum('2', i))

zs = 1000000
for i in range(0, len(zeroes)):
	if zeroes[i] < zs:
		zs = zeroes[i]
		z = i

out = ones[z] * twos[z]
print(out)