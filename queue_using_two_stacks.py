class Queue:
    # Stacks to be used in the operations.
    def __init__(self):
        self.__stk1 = []
        self.__stk2 = []

    # Enqueues 'X' into the queue. Returns true after enqueuing.
    # Enqueue keeping O(1)
    def enqueue(self, X):
        self.__stk1.append(X)
        return True

    """
      Dequeues top element from queue. Returns -1 if the queue is empty, 
      otherwise returns the popped element.

      1) In this implementation we have kept dequeue time complexity as O(n)
      2) In the dequeueImproved the time complexity is  O(1) amortized 
    """
    # Dequeue is O(n)
    def dequeue(self):
        if len(self.__stk1) == 0:
            return -1
        
        while len(self.__stk1) > 1:
            self.__stk2.append(self.__stk1.pop())
        
        ele = self.__stk1.pop()

        while self.__stk2:
            self.__stk1.append(self.__stk2.pop())
        
        return ele

    def dequeueImproved(self):
        if not self.__stk1 and not self.__stk2:
            return -1
        
        if not self.__stk2:
            while self.__stk1:
                self.__stk2.append(self.__stk1.pop())
        
        return self.__stk2.pop()


# Main
# Create Object
queue = Queue()

t = int(input("No. of Queries: "))

while t > 0:

    user_input = list(map(int, input("Operation and Value(for Enqueue): ").split()))
    option = user_input[0]
    value = None

    if option == 1:
        if len(user_input) == 2:
            value = user_input[1]
            print("Enqueue: ", queue.enqueue(value))
        else:
            print("Enter the Value to be enqueued, Invalid Input")

    elif option == 2:
        print("Dequeue: ", queue.dequeue())

    t-=1
