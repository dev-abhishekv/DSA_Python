"""
Print Level Wise

Problem statement:
    * For a given a Binary Tree of type integer, print the complete information of every node, when traversed in a level-order fashion.
    * To print the information of a node with data D, you need to follow the exact format :

        D:L:X,R:Y

    Where D is the data of a node present in the binary tree. 
    X and Y are the values of the left(L) and right(R) child of the node.
    Print -1 if the child doesn't exist.
"""
import queue
from tree_operations_module import take_input_level_wise

def printLevelWise(root):
    q = queue.Queue()

    # Check is root Empty
    if root is None:
        print("Empty Tree")
        return

    # Enque root Node
    q.put(root)

    # Iterate till queue is having element
    while not q.empty():
        # Deque currentNode
        currentNode = q.get()

        # Check and enque left Node
        leftNode = currentNode.left 
        if leftNode is not None:
            q.put(leftNode)
        
        # Check and enque right Node
        rightNode = currentNode.right
        if rightNode is not None:
            q.put(rightNode)
        
        leftChild = leftNode.data if leftNode else -1
        rightChild = rightNode.data if rightNode else -1        
        
        print(f"{currentNode.data}:L:{leftChild},R:{rightChild}")

root = take_input_level_wise()
printLevelWise(root)