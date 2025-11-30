"""
Problem Statement:
Level Wise Input in Binary Tree
"""
from tree_operations_module import BinaryTreeNode, display_formatted_tree
from queue import Queue

def bt_level_wise_input():
    q = Queue()

    rootEle = int(input("Enter Root Element: "))
    if rootEle == -1:
        return None
    
    rootNode = BinaryTreeNode(rootEle)
    q.put(rootNode)

    while not q.empty():
        CurrentNode = q.get()

        leftEle = int(input("Enter left Element: "))
        if leftEle != -1:
            leftNode = BinaryTreeNode(leftEle)
            q.put(leftNode)
            CurrentNode.left = leftNode
        
        rightEle = int(input("Enter right Element: "))
        if rightEle != -1:
            rightNode = BinaryTreeNode(rightEle)
            q.put(rightNode)
            CurrentNode.right = rightNode
    
    return rootNode

root = bt_level_wise_input()
display_formatted_tree(root)





