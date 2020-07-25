a = [i for i in input("Enter Names for list 1: ").split()]
b = [i for i in input("Enter Names for list 2: ").split()]
c = []
for i in range(len(a)):
	if(a[i] not in b):
		c.append(a[i])
for i in range(len(b)):
	if(b[i] not in a):
		c.append(b[i])
print("Final List: ",c)