from tree_operations_module import take_input_level_wise, display_formatted_tree

# Count Leaf Nodes
def count_leaf_nodes(root, leaf_count = 0):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1
    
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)


# Take User Input
tree_root = take_input_level_wise()

# Display Tree
display_formatted_tree(tree_root)

# Call Function and Print
print(f"Number of Leaf Nodes: {count_leaf_nodes(tree_root)}")