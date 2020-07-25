n = input("Enter the Number: ")
z = 0
if((n[0] == '7' or n[0] == '8' or n[0] == '9') and len(n) == 10):
	for i in range(len(n)):
		if(ord(n[i]) >= 48 and ord(n[i]) <= 57):
			z += 1
	if(z == len(n)):
		print("VALID")
	else:
		print("NOT VALID")
else:
	print("NOT VALID")