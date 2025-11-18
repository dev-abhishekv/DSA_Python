from tree_operations_module import tree_input, BinaryTreeNode, display_formatted_tree

def tree_node_count(root: BinaryTreeNode) -> int:
	if root is None:
		return 0

	left_node_count = tree_node_count(root.left)
	right_node_count = tree_node_count(root.right)

	return 1 + left_node_count + right_node_count

root = tree_input()

display_formatted_tree(root)
print(f"Node count is: {tree_node_count(root)}")
