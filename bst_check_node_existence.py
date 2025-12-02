"""
Problem statement
Given a BST and an integer k. Find if the integer k is present in given BST or not. You have to return true, if node with data k is present, return false otherwise.

Note:
Assume that BST contains all unique elements.

Sample Input 1 :
8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
2
Sample Output 1 :
true
"""
from tree_operations_module import take_input_level_wise, print_level_wise

def searchInBST(root, k):
    if root is None:
        return False 
    
    if root.data == k:
        return True
    elif root.data > k:
        return searchInBST(root.left, k)
    else:
        return searchInBST(root.right, k)

# Main
root = take_input_level_wise()
k=int(input("Enter Element to Search: "))
print_level_wise(root)
ans = searchInBST(root, k)

print(f"Element exists in Tree: {ans}")
