# Stack based approach
def isBalancedStack(expression) :
	arr = []
	for bracket in expression:
		if bracket == '(':
			arr.append('(')
		elif len(arr) != 0:
			arr.pop()
		else:
			return False

	if len(arr) == 0:
		return True 
	else:
		return False

# Counter based approach since only "(" and ")"
def isBalancedCounter(expression):
	count = 0

	for bracket in expression:
		if bracket == "(":
			count += 1
		else:
			count -= 1

		if count < 0:
			return False
	
	if count == 0:
		return True
	else:
		return False

#main
expression = input("Enter Sequence of Parentheses: ")

print("Stack Based: ", end = "")
if isBalancedStack(expression) :
	print("true")

else :
	print("false")

print("Counter Based: ", end="")	
if isBalancedCounter(expression) :
	print("true")

else :
	print("false")
