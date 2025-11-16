from sys import stdin
import queue

# Solution with SC: O(n) and TC: O(2n) ~O(n)
def reverseKElements_UO(inputQueue, k) :
    if inputQueue.empty() or k == 0:
        return inputQueue
    
    holder_list = []

    # take all elements in a list
    while not inputQueue.empty():
        holder_list.append(inputQueue.get())
    
    # Starting from k-1th element to 0th element, enque  the elements in the queue
    for i in holder_list[k-1::-1]:
        inputQueue.put(i)
    
    # Then enqueue elements from kth to end of list in the queue
    for i in holder_list[k:]:
        inputQueue.put(i)

    return inputQueue

# Optimized Solution SC: O(k) and TC: O(n)
def reverseKElements(inputQueue, k) :
    if inputQueue.empty() or k == 0:
        return inputQueue

    # List 
    holder_stack = []

    # Take first k element and push in stack
    for i in range(k):
        holder_stack.append(inputQueue.get())
    
    # Pop from stack and enque in Queue k elements
    while not isEmpty(holder_stack):
        inputQueue.put(top(holder_stack))
        holder_stack.pop()
    
    # Deque and Enque remaining elements from the queue to the queue
    for i in range(inputQueue.qsize()-k):
        inputQueue.put(inputQueue.get())
    
    return inputQueue


# Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack):
    return len(stack) == 0

# Takes a list as a stack and returns the element at the top
def top(stack) :
    #assuming the stack is never empty
    return stack[len(stack) - 1]

def takeInput():
    n_k = list(map(int, input("Enter n and k: ").split(" ")))
    n = n_k[0]
    k = n_k[1]

    qu = queue.Queue()
    values = list(map(int, input("Enter List: ").split()))

    for i in range(n) :
        qu.put(values[i])

    return k, qu


#main
k, qu = takeInput()

qu = reverseKElements(qu, k)

while not qu.empty() :
    print(qu.get(), end = " ")
