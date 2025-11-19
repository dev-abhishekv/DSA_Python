from tree_operations_module import take_input_level_wise, display_formatted_tree

def height(root) :
    if root is None:
        return 0
    
    left_height = height(root.left)
    right_height = height(root.right)

    return max(left_height, right_height) + 1

# Take User Input
tree_root = take_input_level_wise()

# We are considering a single node tree (i.e. Having Root node only) to be of height 1
print(f"Height of tree is: {height(tree_root)}")