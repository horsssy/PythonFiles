oppList = ["+","-","*","/"]
num1 = 0
num2 = 0
opp = 0
j = 100
while(j>0):
	r = 0.0000
	for i in range(len(oppList)):
		print(str(i)+". ["+str(oppList[i])+"] ")
	num1 = float(input("Enter Num1: "))
	num2 = float(input("Enter Num2: "))
	opp = int(input("Enter Operation"))
	if opp == 0:
		r = num1 +num2
	elif (opp == 1):
		r = num1-num2
	elif (opp == 2):
		r =num1*num2
	else:
		r = num1/num2
	print(str(num1)+" "+str(oppList[opp])+" "+str(num2)+" = "+str(r))
	q = "d"
	print(q)
	q = str(input("Enter 'q' to exit"))
	
	print(q)
	if (q == "q" or q =="Q"):
		break
	j-=1	
