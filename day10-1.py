import math

f = open("input10.txt", "r")

ast = []
for i in f:
	temp = i.split()[0]
	temp1 = []
	for j in temp:
		temp1.append(j)
	ast.append(temp1)
f.close()

ast1 = []
ast2 = []
for i in range(0, len(ast)):
	for j in range(0, len(ast[i])):
		if ast[i][j] == "#":
			asteroid = [j, i]
			asteroids = 0
			for k in range(0, len(ast)):
				for l in range(0, len(ast[k])):
					if k != i or l != j:
						if ast[k][l] == "#":
							blocked = False
							ydiff = k - i
							xdiff = l - j
							gcd = math.gcd(ydiff, xdiff)
							addy = int(ydiff / gcd)
							addx = int(xdiff / gcd)
							y = i
							x = j
							while(True):
								y += addy
								x += addx
								if y == k and x == l:
									break
								if ast[y][x] == "#":
									blocked = True
							if not blocked:
								asteroids += 1
			temp = []
			temp.append(j)
			temp.append(i)
			ast1.append(temp)
			ast2.append(asteroids)

ind = ast2.index(max(ast2))
print(ast1[ind])
print(ast2[ind])