n = int(input("no of Students"))
s = []
g = []
for i in range(n):
   s.append(input("Name: "))
   g.append(float(input("Marks: ")))

for i in range(g.count(min(g))):
	g.remove(min(g))

for i , j in dict(sorted(zip(s,g))).items():
	if(j == min(g)):
		print(i)