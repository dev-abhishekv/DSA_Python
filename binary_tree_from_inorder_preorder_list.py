"""
Construct Tree from preorder & inorder
Problem statement
For a given preorder and inorder traversal of a Binary Tree of type integer stored in an array/list,
create the binary tree using the given two arrays/lists. You just need to construct the tree and return the root.

Note: Assume that the Binary Tree contains only unique elements.

TC: O(n^2) can be optimized
SC: O(n)
"""
from tree_operations_module import BinaryTreeNode
import queue

def printLevelWise(root):
    if root is None :
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty(): 
        frontNode = pendingNodes.get()
    
        if frontNode is None :
            print()
            
            if not pendingNodes.empty() :
                pendingNodes.put(None)
                
        else :
            print(frontNode.data, end = " ")
            
            if frontNode.left is not None :
                pendingNodes.put(frontNode.left)
                
                
            if frontNode.right is not None :
                pendingNodes.put(frontNode.right)


def find_root(inorder_list):
    return inorder_list[0]


def get_left_right_io_subtree(inorder_list, rootEle):
    # Serach for index of root Node data
    root_index = inorder_list.index(rootEle)

    # Return left and right subtree from inorder 
    return inorder_list[:root_index], inorder_list[root_index+1:]


def get_left_right_po_subtree(pre_order, left_st_len):
    # Get left subtree last element index
    left_sub_tree_last_index = 1+left_st_len

    # Return left and right subtree from pre-order 
    return pre_order[1:left_sub_tree_last_index], pre_order[left_sub_tree_last_index:]


def buildTree(preOrder, inOrder, n) :
    if len(inOrder) < 1:
        return None

    if len(inOrder) == 1:
        return BinaryTreeNode(inOrder[0])

    # Get Root Element
    rootEle = find_root(preOrder)
    rootNode = BinaryTreeNode(rootEle)
     
    # Get left and right subtree from in-order list
    left_st_io, right_st_io = get_left_right_io_subtree(inOrder, rootEle)
    
    # Get left and right subtree from pre-order list
    left_st_po, right_st_po = get_left_right_po_subtree(preOrder, len(left_st_io))

    # Create Left Node
    leftNode = buildTree(left_st_po, left_st_io, len(left_st_io))
    
    # Create Right Node
    rightNode = buildTree(right_st_po, right_st_io, len(right_st_io))

    # Connect Nodes to Root Node
    rootNode.left = leftNode
    rootNode.right = rightNode

    return rootNode

# Main
def takeInput():
    n = int(input("Length: "))

    if n == 0 :
        return list(), list(), 0

    preOrder = list(map(int, input("PreOrder: ").split()))
    inOrder = list(map(int, input("InOrder: ").split()))

    return preOrder, inOrder, n

preOrder, inOrder, n = takeInput()
root = buildTree(preOrder, inOrder, n)
printLevelWise(root)