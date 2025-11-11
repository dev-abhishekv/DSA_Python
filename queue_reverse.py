from sys import setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

def reverseQueue(inputQueue) :
    if inputQueue.qsize() <= 1:
        return inputQueue
    
    first_ele = inputQueue.get()

    reverseQueue(inputQueue)

    inputQueue.put(first_ele)

'''-------------- Utility Functions --------------'''

def takeInput():
    n = int(input("Enter Length of Queue: "))

    qu = queue.Queue()
    values = list(map(int, input("Enter the elements: ").split()))

    for i in range(n) :
        qu.put(values[i])

    return qu


#main
t = int(input("Enter Test Cases: "))

while t > 0 :
    
    qu = takeInput()
    reverseQueue(qu)
    
    while not qu.empty() :
        print(qu.get(), end = " ")
        
    print()
    
    t -= 1