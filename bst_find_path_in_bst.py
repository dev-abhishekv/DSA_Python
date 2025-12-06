"""
Find Path iN BST:

Problem statement
Given a BST and an integer k. Find and return the path from the node with data k and root (if a node with data k is present in given BST) in a list. Return empty list otherwise.

Note: Assume that BST contains all unique elements.

Sample Input 1:
8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
2

Sample Output 1:
2 5 8
"""
from tree_operations_module import take_input_level_wise, print_level_wise

# In Case of BST
def findPathBST(root,data, li = []):
    if root is None:
        return []
    
    if root.data == data:
        li.append(root.data)
        return li
    
    if root.data > data:
        findPathBST(root.left, data)
    else:
        findPathBST(root.right, data)

    if li == []:
        return []
    else:
        li.append(root.data)
        return li

# In Case BT
def findPathBT(root,data):
    if root is None:
        return []
    
    if root.data == data:
        li = []
        li.append(root.data)
        return li
    
    # When root.data != data we call on left subtree
    left_subtree = findPathBT(root.left, data)
    if left_subtree != []:
        left_subtree.append(root.data)
        return left_subtree

    # If left subtree also do not have data we call on right subtree
    right_subtree = findPathBT(root.right, data)
    if right_subtree != []:
        right_subtree.append(root.data)
        return right_subtree
    
    # If data is not found at all we return empty list
    return []
    

# Main
root = take_input_level_wise()
element = int(input("Enter Element to Search: "))

print("Tree is: ")
print_level_wise(root)

bst_search = findPathBST(root, element)
bt_search = findPathBT(root, element)

print(f"Path bst_search: {bst_search}")
print(f"Path bt_search: {bt_search}")