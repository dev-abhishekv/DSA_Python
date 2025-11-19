from tree_operations_module import take_input_level_wise, display_formatted_tree

# Replace Node Data with Depth value
def changeToDepthTree(root, depth=0):
    if root is None:
        return

    root.data = depth

    changeToDepthTree(root.left, depth+1)
    changeToDepthTree(root.right, depth+1)

# Take User Input
tree_root = take_input_level_wise()

# Display Tree
display_formatted_tree(tree_root)

# Call Function
changeToDepthTree(tree_root)

# Display Modified Tree
display_formatted_tree(tree_root)