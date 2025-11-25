from tree_operations_module import take_input_level_wise, display_formatted_tree

root = take_input_level_wise()
x = int(input("Enter Value of x: "))

print("TREE")
display_formatted_tree(root)

def isNodePresent(root, x):
    if root is None:
        return False
    
    if root.data == x:
        return True
    
    is_present_on_left = isNodePresent(root.left, x)
    is_present_on_right = isNodePresent(root.right, x)

    if is_present_on_left or is_present_on_right:
        return True
    else:
        return False

print(f"Node with value {x} present: {isNodePresent(root, x)}")
