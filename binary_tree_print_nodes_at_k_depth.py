from tree_operations_module import take_input_level_wise, display_formatted_tree

# Count Leaf Nodes
def nodes_at_depth_k(root, k, depth=0):
    if root is None:
        return None
    
    if depth == k:
        print(root.data, end = ", ")


    nodes_at_depth_k(root.left, k, depth+1)
    nodes_at_depth_k(root.right, k, depth+1)


# Take User Input
tree_root = take_input_level_wise()
k = int(input("Enter k (depth): "))
# Display Tree
display_formatted_tree(tree_root)

# Call Function and Print
nodes_at_depth_k(tree_root, k)