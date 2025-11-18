# Create Tree Node Class
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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

# Take User Input
def tree_input():
    print("Take User Input for Tree Formation")
    data = int(input("Enter Data: "))
    if data == -1:
        return None

    root_node = BinaryTreeNode(data)

    left_child = tree_input()
    right_child = tree_input()

    root_node.left = left_child
    root_node.right = right_child

    return root_node

# Count the number of nodes
def tree_node_count(root: BinaryTreeNode) -> int:
	if root is None:
		return 0

	left_node_count = tree_node_count(root.left)
	right_node_count = tree_node_count(root.right)

	return 1 + left_node_count + right_node_count
