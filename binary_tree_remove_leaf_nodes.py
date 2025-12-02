"""
Sample Input 1:
10 20 30 40 50 -1 60 -1 -1 -1 -1 -1 -1 

Sample Output 1:
10 
20 30 
"""

from tree_operations_module import take_input_level_wise, print_level_wise

def remove_leaf_nodes(root):
    if root is None:
        return

    if root.left is None and root.right is None:
        return None
    
    leftNode = remove_leaf_nodes(root.left)
    rightNode = remove_leaf_nodes(root.right)

    root.left = leftNode
    root.right = rightNode

    return root

# Main
root = take_input_level_wise()
print("Input Tree")
print_level_wise(root)

print("Tree after leaf removal")
root = remove_leaf_nodes(root)
print_level_wise(root)
