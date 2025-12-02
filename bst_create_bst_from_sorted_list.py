"""
Problem statement
Given a sorted integer array A of size n, which contains all unique elements. You need to construct a balanced BST from this input array. Return the root of constructed BST.

Note: If array size is even, take first mid as root.

Sample Input 1:
7
1 2 3 4 5 6 7
Sample Output 1:
4 2 1 3 6 5 7 


Sample Input 2:
8
1 2 3 4 5 6 7 8
Sample Output 2:
4 2 1 3 6 5 7 8
"""

from tree_operations_module import BinaryTreeNode

def constructBST(lst):
    if len(lst) < 1:
        return None
    
    if len(lst) == 1:
        return BinaryTreeNode(lst[0])

    start = 0
    end = len(lst)-1
    mid_point = start+(end-start)//2 #(len(lst)-1)//2
    root = BinaryTreeNode(lst[mid_point])

    left_subtree = constructBST(lst[:mid_point])
    right_subtree = constructBST(lst[mid_point+1:])

    root.left = left_subtree
    root.right = right_subtree

    return root

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input("Enter Length of Array: "))
if(n>0):
    lst=[int(i) for i in input("Enter Array Elements: ").strip().split()]
else:
    lst=[]
root=constructBST(lst)
preOrder(root)