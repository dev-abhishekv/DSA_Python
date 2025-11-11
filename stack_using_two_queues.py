
from sys import stdin
from queue import Queue

class Stack :

	#Define data members and __init__()
	def __init__(self):
		self.__queue_1 = Queue()
		self.__queue_2 = Queue()

	'''----------------- Public Functions of Stack -----------------'''


	def getSize(self) :
		#Implement the getSize() function
		return self.__queue_1.qsize()

	def isEmpty(self) :
		#Implement the isEmpty() function
		return self.__queue_1.qsize() == 0

	def push(self, data) :
		#Implement the push(element) function
		self.__queue_1.put(data)

	def pop(self) :
		#Implement the pop() function
		if self.__queue_1.empty():
			return -1 

		while self.__queue_1.qsize() > 1:
			self.__queue_2.put(self.__queue_1.get())

		ele = self.__queue_1.get()

		temp = self.__queue_2
		self.__queue_2 = self.__queue_1
		self.__queue_1 = temp

		return ele

	def top(self) :
		#Implement the top() function
		#Implement the pop() function
		if self.__queue_1.empty():
			return -1

		while self.__queue_1.qsize() > 1:
			self.__queue_2.put(self.__queue_1.get())

		ele = self.__queue_1.get()

		self.__queue_2.put(ele)

		temp = self.__queue_2
		self.__queue_2 = self.__queue_1
		self.__queue_1 = temp
		
		return ele




#main
q = int(input("Enter Number of Queries: "))

stack = Stack()

while q > 0 :

	print("Choices: \n 1 -> Push \n 2 -> Pop \n 3 -> Top \n 4 -> Size \n Other -> Empty Check \n")
	inputs = input("Enter Choice and Value (to push) ").split()

	choice = int(inputs[0])
	if choice == 1 :
		data = int(inputs[1])
		stack.push(data)

	elif choice == 2 :
		print(stack.pop())

	elif choice == 3 :
		print(stack.top())

	elif choice == 4 : 
		print(stack.getSize())

	else :
		if stack.isEmpty() :
			print("true")
		else :
			print("false")

	q -= 1