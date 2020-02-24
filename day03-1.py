inp = []
w1coord = [0, 0]
w1 = []
w2coord = [0, 0]
w2 = []
crossing = []

f = open("input3.txt", "r")
for i in f:
	inp.append(i.split(","))
f.close()

for i in inp[0]:
	direc = i[0]
	mag = int(i[1::])
	if direc == "U":
		for i in range(1, mag+1):
			temp = []
			temp.append(w1coord[0])
			temp.append(w1coord[1] + i)
			w1.append(temp)
			temp = []
		w1coord[1] += mag
	elif direc == "D":
		for i in range(1, mag+1):
			temp = []
			temp.append(w1coord[0])
			temp.append(w1coord[1] - i)
			w1.append(temp)
			temp = []
		w1coord[1] -= mag
	elif direc == "R":
		for i in range(1, mag+1):
			temp = []
			temp.append(w1coord[0] + i)
			temp.append(w1coord[1])
			w1.append(temp)
			temp = []
		w1coord[0] += mag
	elif direc == "L":
		for i in range(1, mag+1):
			temp = []
			temp.append(w1coord[0] - i)
			temp.append(w1coord[1])
			w1.append(temp)
			temp = []
		w1coord[0] -= mag

for i in inp[1]:
	direc = i[0]
	mag = int(i[1::])
	if direc == "U":
		for i in range(1, mag+1):
			temp = []
			temp.append(w2coord[0])
			temp.append(w2coord[1] + i)
			w2.append(temp)
			temp = []
		w2coord[1] += mag
	elif direc == "D":
		for i in range(1, mag+1):
			temp = []
			temp.append(w2coord[0])
			temp.append(w2coord[1] - i)
			w2.append(temp)
			temp = []
		w2coord[1] -= mag
	elif direc == "R":
		for i in range(1, mag+1):
			temp = []
			temp.append(w2coord[0] + i)
			temp.append(w2coord[1])
			w2.append(temp)
			temp = []
		w2coord[0] += mag
	elif direc == "L":
		for i in range(1, mag+1):
			temp = []
			temp.append(w2coord[0] - i)
			temp.append(w2coord[1])
			w2.append(temp)
			temp = []
		w2coord[0] -= mag

for i in w1:
	if i in w2:
		crossing.append(abs(i[0]) + abs(i[1]))

crossing.sort()
print(crossing[0])