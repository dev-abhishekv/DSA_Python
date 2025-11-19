from tree_operations_module import take_input_level_wise, display_formatted_tree

# Find the Largest Value Node
def count_nodes_greater_than_x(root, x) :
    if root is None:
        return 0

    left_node = count_nodes_greater_than_x(root.left, x)
    right_node = count_nodes_greater_than_x(root.right, x)

    if root.data > x:
        return 1 + left_node + right_node
    else:
        return left_node + right_node



# Take User Input
tree_root = take_input_level_wise()

# Take x
x = int(input("Enter value of X: "))
print(f"Node's greater than X in Tree are: {count_nodes_greater_than_x(tree_root, x)}")



