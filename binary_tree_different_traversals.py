from tree_operations_module import take_input_level_wise


def display_in_order(root):
    if root is None:
        return 

    display_in_order(root.left)
    print(root.data)
    display_in_order(root.right)

def display_pre_order(root):
    if root is None:
        return

    print(root.data)

    display_pre_order(root.left)
    display_pre_order(root.right)

def display_post_order(root):
    if root is None:
        return

    display_post_order(root.left)
    display_post_order(root.right)     
    print(root.data)

# Take user input and create tree
root_node = take_input_level_wise()

# Display Tree
print("Pre_Order Traversal")
display_pre_order(root_node)

print("Post_Order Traversal")
display_post_order(root_node)

print("In_Order Traversal")
display_in_order(root_node)
