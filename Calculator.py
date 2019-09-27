def add(sum1, sum2):
	return sum1 + sum2 

def sub(sum1, sum2):
		return sum1 - sum2
		
def mul(sum1, sum2):
	return sum1 * sum2
	
def div(sum1, sum2):
	try:
		return sum1 / sum2
	except ZeroDivisionError:
		print("Divided by zero, returning zero")
		return 0

def runOperation(operation, sum1, sum2):
	#  Determining operator chosen by user 		
	if (operation == 1):
		print("adding...")
		print (add(sum1, sum2))
	elif(operation == 2):
		print("subtracting...")
		print (sub(sum1, sum2))
	elif (operation == 3):
		print("multipling...")
		print (mul(sum1, sum2))
	elif (operation == 4):
		print("dividing...")
		print (div(sum1, sum2))
	else:
		print ("Please select one of the operators provided")

		
def main():
	user_continue = True
	while user_continue:
		validInput = False	
		while not validInput:
			#  get user input
			try: 
				sum1 = int(input("Input Number: "))
				sum2 = int(input("Input Number: "))
				operation = int(input("What do you want to do? Please select an oporator by its number: 1. add, 2. subtract, 3. Multiply, 4. Divide "))
				validInput = True 	
			except ValueError:
				print("Invalid input, please try again")
			except:
				print("Unknown error")
		runOperation(operation, sum1, sum2)		
			
		repeatAnswer = input ("Would you like to go again? (Yes or No)")
		if(repeatAnswer == "yes" or repeatAnswer == "Yes"):
			continue  
		else:
			user_continue - False
			print("Thank you and goodbye")
			break 
		
		
main()




	