# Queue implementationg using Array
class QueueUsingArray:
    def __init__(self):
        self.__queue = []
        self.__count = 0
        self.__front = 0

    def enqueue(self, value):
        self.__queue.append(value)
        self.__count += 1
        
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return

        element = self.__queue[self.__front]
        self.__front += 1
        self.__count -= 1

        return element

    def getSize(self):        
        return self.__count

    def front(self):
        if self.isEmpty():
            print("Queue is empty")
            return

        return self.__queue[self.__front]
    
    def isEmpty(self):
        return self.__count == 0

#Following is the structure of the node class for a Singly Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

# Queue Implementation using Linked List
class QueueUsingLL:
    # Constructor
    def __init__(self):
        self.__count = 0
        self.__head = self.__tail = None

    '''----------------- Public Functions of Queue -----------------'''

    def getSize(self) :
        # Return size of Queue
        return self.__count


    def isEmpty(self) :
        # Return True/False based on emptiness of Queue
        return self.__count == 0


    def enqueue(self, data) :
        # Inserts an element in the Queue
        newNode = Node(data)
        if self.__head is None:
            self.__head = self.__tail = newNode
        else:
            self.__tail.next = newNode
            self.__tail = self.__tail.next
        
        self.__count += 1


    def dequeue(self) :
        # Removes the front element from the Queue and returns it.
        if self.isEmpty():
            return -1
        
        element = self.__head.data

        self.__head = self.__head.next
        self.__count -= 1

        return element
    
    def front(self) :
        # Return the front element of the queue
        if self.isEmpty():
            return -1

        return self.__head.data   

# Main
q = int(input("Enter Number of Operations: "))

queue = QueueUsingArray()
# queue = QueueUsingLL()

while q > 0 :

    print("Choices: \n 1 -> Enqueue \n 2 -> Dequeue \n 3 -> Front \n 4 -> Size \n Other -> Empty Check \n")

    inputs = list(map(int, input("Enter: ").strip().split(" ")))
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        queue.enqueue(data)

    elif choice == 2 :
        print(queue.dequeue())

    elif choice == 3 :
        print(queue.front())

    elif choice == 4 : 
        print(queue.getSize())

    else :
        if queue.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1
