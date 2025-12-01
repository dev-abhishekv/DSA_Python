"""
Level Order Traversal:
For a given a Binary Tree of type integer, print it in a level order fashion where each level will be printed on a new line.
Elements on every level will be printed in a linear fashion and a single space will separate them.

Sample Input 1:
10 20 30 40 50 -1 60 -1 -1 -1 -1 -1 -1 

Sample Output 1:
10 
20 30 
40 50 60 
"""

import queue
from tree_operations_module import take_input_level_wise

# Way 1: Using 2 Queues
def printLevelWise_1(root):
    if root is None:
        return
    
    inputQ = queue.Queue()
    outputQ = queue.Queue()

    inputQ.put(root)

    while not inputQ.empty():

        while not inputQ.empty():
            currentNode = inputQ.get()
            print(currentNode.data, end = " ")

            if currentNode.left is not None:
                outputQ.put(currentNode.left)
            
            if currentNode.right is not None:
                outputQ.put(currentNode.right)

        print()

        inputQ, outputQ = outputQ, inputQ

# Way 2: Using Single Queue
def printLevelWise_2(root):
    if root is None:
        return
    
    q = queue.Queue()
    

    q.put(root)
    q.put(None)

    while not q.empty():
        currentNode = q.get()

        if currentNode is None:
            print()

            if not q.empty():
                q.put(None)
        else:
            print(currentNode.data, end= " ")
            
            if currentNode.left is not None:
                q.put(currentNode.left)
            if currentNode.right is not None:
                q.put(currentNode.right)

# Way 3: Using Count of Nodes at each level
def printLevelWise_3(root):
    if root is None:
        return

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        queue_size = q.qsize()

        for _ in range(queue_size):
            currentNode = q.get()
            print(currentNode.data, end=" ")

            if currentNode.left:
                q.put(currentNode.left)
            if currentNode.right:
                q.put(currentNode.right)
        
        print()

# Main
root = take_input_level_wise()

print()
printLevelWise_1(root)
print()
printLevelWise_2(root)
print()
printLevelWise_3(root)