def adjacent(num):
	nums = str(num)
	if (nums[0] == nums[1] or nums[1] == nums[2] or nums[2] == nums[3] or nums[3] == nums[4] or nums[4] == nums[5]):
		return True
	return False

def increase(num):
	nums = str(num)
	if (nums[0] <= nums[1] and nums[1] <= nums[2] and nums[2] <= nums[3] and nums[3] <= nums[4] and nums[4] <= nums[5]):
		return True
	return False

inp = "146810-612564"
inp1 = inp.split("-")
num1 = int(inp1[0])
num2 = int(inp1[1])

password = []

for i in range(num1, num2+1):
	if adjacent(i) and increase(i):
		password.append(i)

print(len(password))