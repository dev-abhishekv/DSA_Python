"""
Sum of All Node

Problem statement
Given a generic tree, find and return the sum of all nodes present in the given tree.

Sample Input 1:
10 3 20 30 40 2 40 50 0 0 0 0 

Sample Output 1:
190
"""

import sys
import queue

class TreeNode :
    def __init__(self, data) :
        self.data = data
        self.children = list()

# Level Wise Input Generic Tree
def inputLevelWise(li) :
    i = 0
    data = li[i] 
    i += 1
    if data == -1 :
        return None
    root = TreeNode(data) 
    q = queue.Queue()
    q.put(root)
    while (not q.empty()) :
        frontNode = q.get()
        noOfChildren = li[i]
        i += 1
        childrenArray = li[i : i+noOfChildren]
        for childData in childrenArray :
            childNode = TreeNode(childData)
            frontNode.children.append(childNode)
            q.put(childNode)
        i = i+noOfChildren
    return root

# Sum of Nodes
def sumOfAllNodes(root) :
    if root is None:
        return 0

    total_sum = root.data

    for child in root.children:
        total_sum = total_sum + sumOfAllNodes(child)
    
    return total_sum
    
#main
sys.setrecursionlimit(10**6)
# List with Data and Child Count
li = [int(elem) for elem in list(input().strip().split())]

# Prepare Generic Tree
root = inputLevelWise(li)

# Call and Print Sum of all nodes
print(sumOfAllNodes(root))