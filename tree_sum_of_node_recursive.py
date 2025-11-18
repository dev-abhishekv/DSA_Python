from tree_operations_module import BinaryTreeNode, display_formatted_tree, take_input_level_wise


def getSum(root):
    if root is None:
        return 0

    left_sum = getSum(root.left)
    right_sum = getSum(root.right)

    return left_sum + right_sum + root.data

# Take user input and create tree
root_node = take_input_level_wise()

# Display Tree
display_formatted_tree(root_node)

# Print Sum
print(f"Sum of Nodes: {getSum(root_node)}")