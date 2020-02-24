inp = []
w1coord = [0, 0]
w1 = []
w1dist = [0]
w2coord = [0, 0]
w2 = []
w2dist = [0]
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
			w1dist[0] += 1
			temp.append(w1coord[0])
			temp.append(w1coord[1] + i)
			w1.append(temp)
			w1dist.append(w1dist[0])
			temp = []
		w1coord[1] += mag
	elif direc == "D":
		for i in range(1, mag+1):
			temp = []
			w1dist[0] += 1
			temp.append(w1coord[0])
			temp.append(w1coord[1] - i)
			w1.append(temp)
			w1dist.append(w1dist[0])
		w1coord[1] -= mag
	elif direc == "R":
		for i in range(1, mag+1):
			temp = []
			w1dist[0] += 1
			temp.append(w1coord[0] + i)
			temp.append(w1coord[1])
			w1.append(temp)
			w1dist.append(w1dist[0])
			temp = []
		w1coord[0] += mag
	elif direc == "L":
		for i in range(1, mag+1):
			temp = []
			w1dist[0] += 1
			temp.append(w1coord[0] - i)
			temp.append(w1coord[1])
			w1.append(temp)
			w1dist.append(w1dist[0])
			temp = []
		w1coord[0] -= mag

for i in inp[1]:
	direc = i[0]
	mag = int(i[1::])
	if direc == "U":
		for i in range(1, mag+1):
			temp = []
			w2dist[0] += 1
			temp.append(w2coord[0])
			temp.append(w2coord[1] + i)
			w2.append(temp)
			w2dist.append(w2dist[0])
			temp = []
		w2coord[1] += mag
	elif direc == "D":
		for i in range(1, mag+1):
			temp = []
			w2dist[0] += 1
			temp.append(w2coord[0])
			temp.append(w2coord[1] - i)
			w2.append(temp)
			w2dist.append(w2dist[0])
			temp = []
		w2coord[1] -= mag
	elif direc == "R":
		for i in range(1, mag+1):
			temp = []
			w2dist[0] += 1
			temp.append(w2coord[0] + i)
			temp.append(w2coord[1])
			w2.append(temp)
			w2dist.append(w2dist[0])
			temp = []
		w2coord[0] += mag
	elif direc == "L":
		for i in range(1, mag+1):
			temp = []
			w2dist[0] += 1
			temp.append(w2coord[0] - i)
			temp.append(w2coord[1])
			w2.append(temp)
			w2dist.append(w2dist[0])
			temp = []
		w2coord[0] -= mag

for i in range(0, len(w1)):
	for j in range(0, len(w2)):
			if(w1[i] == w2[j]):
				crossing.append(w1dist[i+1] + w2dist[j+1])

crossing.sort()
print(crossing[0])