def reverseStack(inputStack, extraStack) :
    # When only one element then thats already reversed
	if len(inputStack) == 1 or len(inputStack) == 0:
		return
	
    # Move n elements to emptyStack
	while len(inputStack) != 0:
		extraStack.append(inputStack.pop())
	
    # Take 1st element of stack and save it
	last_ele = extraStack.pop()

    # Move n-1 elements back to original stack
	while len(extraStack) != 0:
		inputStack.append(extraStack.pop())

    # Call reverseStack recursively till 1 element is left in original stack
	reverseStack(inputStack, extraStack)

    # Keep appending the saved elements back in the original stack
	inputStack.append(last_ele)	
	# print(inputStack)


#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0

#Taking input using fast I/o method
def takeInput() :
	size = int(input("Enter size of List: "))
	inputStack = list()

	if size == 0 :
		return inputStack


	values = list(map(int, input("Enter List elements: ").split(" ")))
	inputStack = values

	return inputStack


# Main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack) :
	print(inputStack.pop(), end = " ")