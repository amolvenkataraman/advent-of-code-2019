def addup(n):
	k = 0
	for i in range(1, n + 1):
		k += i
	return k

f = open("input6.txt", "r")

inp = []
inp1 = []
for i in f:
	inp.append(i.split(")")[0].strip())
	inp1.append(i.split(")")[1].strip())
f.close()

print("Successfully imported data:")
print(inp)
print(inp1)
print("\n")

inp2 = []
for i in inp:
	if i != "COM":
		inp2.append(i)
	for i in inp1:
		if i not in inp2:
			inp2.append(i)

checked = []
end = []
orbit = 0
planet = ""
for i in inp2:
	if i not in checked:
		planet = i
		checked.append(i)
		while planet in inp:
			for j in range(0, len(inp)):
				if inp[j] == planet: 
					planet = inp1[j]
		if planet not in end:
			end.append(planet)

print("Starting claculations")

plan = []

you = inp1.index("YOU")
san = inp1.index("SAN")

you1 = []
san1 = []

planet = inp[you]
while planet in inp1:
	you1.append(planet)
	planet = inp[inp1.index(planet)]

planet = inp[san]
while planet in inp1:
	san1.append(planet)
	planet = inp[inp1.index(planet)]

print("Found route to COM")
print(you1)
print(san1)

ok = True
for i in you1:
	if i in san1:
		if ok:
			ok = False
			ans = you1.index(i) + san1.index(i)

print("Calculation complete")
print(ans)