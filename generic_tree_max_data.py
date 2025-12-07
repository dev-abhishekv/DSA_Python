"""
Node With Largest Data

Problem statement:
Given a generic tree, find and return the node with maximum data.

Note: Return null if the tree is empty.

Sample Input 1:
10 3 20 30 40 2 40 50 0 0 0 0 
Sample Output 1:
50
"""


import sys
sys.setrecursionlimit(3000)

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def maxDataNode(tree):
    if tree is None:
        return None
    
    max_node = tree

    for child in tree.children:
        child_max = maxDataNode(child)
        if child_max and child_max.data > max_node.data:
            max_node = child_max
        
    return max_node

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in input("Enter Array: ").split())
tree = createLevelWiseTree(arr)
print(maxDataNode(tree).data)