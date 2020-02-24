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

asts = []
# [x, y], rise, run, quadrant, angle, exists, coordsum
#  [0]     [1]  [2]     [3]     [4]    [5]      [6]
# Quadrants:
# 	1 - 4: Quadrants 1 - 4
# 	5: +ve Y axis
# 	6: +ve X axis
# 	7: -ve Y axis
# 	8: -ve X axis

for i in ast1:
	if i != ast1[ind]:
		temp = []
		temp.append(i)
		rise = ast1[ind][1] - i[1]
		temp.append(rise)
		run = i[0] - ast1[ind][0]
		temp.append(run)

		if rise > 0 and run > 0:
			quadrant = 1
		elif rise < 0 and run > 0:
			quadrant = 2
		elif rise < 0 and run < 0:
			quadrant = 3
		elif rise > 0 and run < 0:
			quadrant = 4
		elif rise == 0:
			if run > 0:
				quadrant = 6
			elif run < 0:
				quadrant = 8
		elif run == 0:
			if rise > 0:
				quadrant = 5
			elif rise < 0:
				quadrant = 7

		temp.append(quadrant)
		try:
			temp.append(abs(( rise / run) * 45))
		except ZeroDivisionError:
			temp.append(0.0)
		temp.append(True)
		temp.append(temp[0][0] + temp[0][1])
		asts.append(temp)

ang = sorted(asts, key=lambda asts: asts[4])
print("ANG: ", ang)

quad = [5, 1, 6, 2, 7, 3, 8, 4]

asts1 = []
for i in quad: 
	temp = []
	for j in ang:
		if j[3] == i:
			print(j)
			temp.append(j)
	asts1.append(temp)

for i in range(0, 8):
	print(quad[i])
	print(asts1[i], "\n")

print("VAPORISING BEGINS")

vaporised = 0
while(True):
	for i in asts1:
		angle = []
		for j in i:
			if j[5]:
				if j[4] not in angle:
					j[5] = False
					print(j)
					vaporised += 1
					angle.append(j[4])
					if vaporised == 200:
						print("\n\n\n", j)
						raise SystemExit