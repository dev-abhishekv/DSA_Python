"""
Create & Insert Duplicate Node:

For a given a Binary Tree of type integer, duplicate every node of the tree and attach it to the left of itself.
The root will remain the same. So you just need to insert nodes in the given Binary Tree.

Sample Input 1:
10 20 30 40 50 -1 60 -1 -1 -1 -1 -1 -1

Sample Output 1:
10 
10 30 
20 30 60 
20 50 60 
40 50 
40 
"""

from tree_operations_module import take_input_level_wise, print_level_wise, BinaryTreeNode

def insertDuplicateNode(root):
    if root is None:
        return
    
    # Get Data to be replicated
    root_data = root.data

    # Get original leftChild Reference
    left_child = root.left

    # Create New Node and attach it to roots left
    new_node = BinaryTreeNode(root_data)

    root.left = new_node

    # Attach original left child as left child of new node
    new_node.left = left_child

    insertDuplicateNode(left_child)
    insertDuplicateNode(root.right)

# Main
root = take_input_level_wise()

# Print original tree
print_level_wise(root)

# Print modified tree
insertDuplicateNode(root)
print("Modified Tree: ")
print_level_wise(root)
