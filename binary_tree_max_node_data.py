from tree_operations_module import take_input_level_wise, display_formatted_tree

# Take User Input
tree_root = take_input_level_wise()

# Find the Largest Value Node
def max_data(root):
    if root is None:
        return -9999999 # Ideally would have returned -infinity

    left_max = max_data(root.left)
    right_max = max_data(root.right)

    largest = max(left_max, right_max, root.data)

    return largest

print(f"Largest number in Tree is: {max_data(tree_root)}")



