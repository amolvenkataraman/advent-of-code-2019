f = open("input14.txt", "r")

equations = []
for i in f:
	reactants1 = i.split("=>")[0]
	reactants0 = reactants1.split(", ")
	reactants = []
	for reactant in reactants0:
		temp = reactant.strip()
		temp1 = []
		temp1.append(int(temp.split(" ")[0]))
		temp1.append(temp.split(" ")[1])
		reactants.append(temp1)

	products1 = i.split("=>")[1]
	products0 = products1.strip()
	products = []
	products.append(int(products0.split(" ")[0]))
	products.append(products0.split(" ")[1])

	temp1 = []
	temp1.append(reactants)
	temp1.append(products)
	equations.append(temp1)

f.close()

print("Successfully imported")
print(equations)

chemical = ['FUEL'] 
nochemical = [1]
while True:
	temp = 0
	for i in chemical:
		if i == 'ORE':
			temp += 1
	if temp == len(chemical):
		break

	for chem in chemical:
		for equation in equations:
			if equation[1][1] == chem:
				print(chem)
				print(chemical)
				print(nochemical)
				chem1 = chemical.index(chem)
				nochem = nochemical[chem1]
				chemical.remove(chem)
				nochemical.pop(chem1)
				for i in equation[0]:
					chemical.append(i[1])
					nochemical.append(nochem * (i[0] / equation[1][0]))
					print(equation)

atoms = sum(nochemical)
print(atoms)