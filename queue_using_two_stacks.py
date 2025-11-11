class Queue:
    # Stacks to be used in the operations.
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    # Enqueues 'X' into the queue. Returns true after enqueuing.
    # Enqueue keeping O(1)
    def enqueue(self, X):
        self.stk1.append(X)
        return True

    """
      Dequeues top element from queue. Returns -1 if the queue is empty, 
      otherwise returns the popped element.

      1) In this implementation we have kept dequeue time complexity as O(n)
      2) In the dequeueImproved the time complexity is  O(1) amortized 
    """
    # Dequeue is O(n)
    def dequeue(self):
        if len(self.stk1) == 0:
            return -1
        
        while len(self.stk1) > 1:
            self.stk2.append(self.stk1.pop())
        
        ele = self.stk1.pop()

        while self.stk2:
            self.stk1.append(self.stk2.pop())
        
        return ele

    def dequeueImproved(self):
        if not self.stk1 and not self.stk2:
            return -1
        
        if not self.stk2:
            while self.stk1:
                self.stk2.append(self.stk1.pop())
        
        return self.stk2.pop()


# Main
# Create Object
queue = Queue()

t = int(input("No. of Queries: "))

while t > 0:

    user_input = list(map(int, input("Operation and Value(for Enqueue): ").split()))
    option = user_input[0]
    value = user_input[1] if len(user_input) == 2 else None

    if option == 1:
        print("Enqueue: ", queue.enqueue(value))
    elif option == 2:
        print("Dequeue: ", queue.dequeue())

    t-=1
