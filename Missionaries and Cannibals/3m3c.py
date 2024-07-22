#Python program to illustrate Missionaries & cannibals Problem 
#This code is contributed by Sunit Mal 
print("\n") 
print("\tGame Start\nNow the task is to move all of them to right side of the river") 
print("rules:\n1. The boat can carry at most two people\n2. If cannibals num greater than missionaries then the cannibals would eat the missionaries\n3. The boat cannot cross the river by itself with no people on board") 
left_missionaries = 3		 #left_missionaries = Left side Missionaries number 
left_cannibals = 3		 #left_cannibals = Laft side Cannibals number 
right_missionaries=0		 #right_missionaries = Right side Missionaries number 
right_cannibals=0		 #right_cannibals = Right side cannibals number 
useright_missionaries = 0	 #useright_missionaries = User input for number of missionaries for right to left side travel 
useright_cannibals = 0	 #useright_cannibals = User input for number of cannibals for right to left travel 
k = 0
print("\nM M M C C C |	 --- | \n") 
try: 
	while(True): 
		while(True): 
			print("Left side -> right side river travel") 
			#uM = user input for number of missionaries for left to right travel 
			#uC = user input for number of cannibals for left to right travel 
			uM = int(input("Enter number of Missionaries travel => "))	 
			uC = int(input("Enter number of Cannibals travel => ")) 

			if((uM==0)and(uC==0)): 
				print("Empty travel not possible") 
				print("Re-enter : ") 
			elif(((uM+uC) <= 2)and((left_missionaries-uM)>=0)and((left_cannibals-uC)>=0)): 
				break
			else: 
				print("Wrong input re-enter : ") 
		left_missionaries = (left_missionaries-uM) 
		left_cannibals = (left_cannibals-uC) 
		right_missionaries += uM 
		right_cannibals += uC 

		print("\n") 
		for i in range(0,left_missionaries): 
			print("M ",end="") 
		for i in range(0,left_cannibals): 
			print("C ",end="") 
		print("| --> | ",end="") 
		for i in range(0,right_missionaries): 
			print("M ",end="") 
		for i in range(0,right_cannibals): 
			print("C ",end="") 
		print("\n") 

		k +=1

		if(((left_cannibals==3)and (left_missionaries == 1))or((left_cannibals==3)and(left_missionaries==2))or((left_cannibals==2)and(left_missionaries==1))or((right_cannibals==3)and (right_missionaries == 1))or((right_cannibals==3)and(right_missionaries==2))or((right_cannibals==2)and(right_missionaries==1))): 
			print("Cannibals eat missionaries:\nYou lost the game") 

			break

		if((right_missionaries+right_cannibals) == 6): 
			print("You won the game : \n\tCongrats") 
			print("Total attempt") 
			print(k) 
			break
		while(True): 
			print("Right side -> Left side river travel") 
			useright_missionaries = int(input("Enter number of Missionaries travel => ")) 
			useright_cannibals = int(input("Enter number of Cannibals travel => ")) 
			
			if((useright_missionaries==0)and(useright_cannibals==0)): 
					print("Empty travel not possible") 
					print("Re-enter : ") 
			elif(((useright_missionaries+useright_cannibals) <= 2)and((right_missionaries-useright_missionaries)>=0)and((right_cannibals-useright_cannibals)>=0)): 
				break
			else: 
				print("Wrong input re-enter : ") 
		left_missionaries += useright_missionaries 
		left_cannibals += useright_cannibals 
		right_missionaries -= useright_missionaries 
		right_cannibals -= useright_cannibals 

		k +=1
		print("\n") 
		for i in range(0,left_missionaries): 
			print("M ",end="") 
		for i in range(0,left_cannibals): 
			print("C ",end="") 
		print("| <-- | ",end="") 
		for i in range(0,right_missionaries): 
			print("M ",end="") 
		for i in range(0,right_cannibals): 
			print("C ",end="") 
		print("\n") 

	

		if(((left_cannibals==3)and (left_missionaries == 1))or((left_cannibals==3)and(left_missionaries==2))or((left_cannibals==2)and(left_missionaries==1))or((right_cannibals==3)and (right_missionaries == 1))or((right_cannibals==3)and(right_missionaries==2))or((right_cannibals==2)and(right_missionaries==1))): 
			print("Cannibals eat missionaries:\nYou lost the game") 
			break
except EOFError as e: 
	print("\nInvalid input please retry !!")
