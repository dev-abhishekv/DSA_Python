# Create Tree Node Class
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def display_tree(root: BinaryTreeNode) -> None:
    if root is None:
        return

    print(root.data)
    display_tree(root.left)
    display_tree(root.right)

def display_formatted_tree(root: BinaryTreeNode) -> None:
    if root is None:
        return

    print(f"{root.data}:", end = " ")

    if root.left is not None:
        print(f"L{root.left.data}", end=", ")
    if root.right is not None:
        print(f"R{root.right.data}", end=" ")
    print()

    display_formatted_tree(root.left)
    display_formatted_tree(root.right)

# Defining Nodes
bt_root_node: BinaryTreeNode = BinaryTreeNode(100)
bt_child_1: BinaryTreeNode = BinaryTreeNode(20)
bt_child_2: BinaryTreeNode = BinaryTreeNode(30)
bt_child_4: BinaryTreeNode = BinaryTreeNode(80)
bt_child_5: BinaryTreeNode = BinaryTreeNode(89)

# Defining Relationships
bt_root_node.left = bt_child_1
bt_root_node.right = bt_child_2
bt_child_1.left = bt_child_4
bt_child_1.right = bt_child_5

# Normal Display
display_tree(bt_root_node)

# Well Formatted Display
display_formatted_tree(bt_root_node)


# Take User Input
def tree_input():
    data = int(input("Enter Data: "))
    if data is -1:
        return None

    root_node = BinaryTreeNode(data)

    left_child = tree_input()
    right_child = tree_input()

    root_node.left = left_child
    root_node.right = right_child

    return root_node

# User Input Tree
print("Take User Input for Tree Formation")
root_user_input_tree = tree_input()
display_formatted_tree(root_user_input_tree)