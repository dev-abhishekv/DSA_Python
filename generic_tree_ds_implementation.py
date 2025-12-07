# Generic Tree Node Class
class GenericTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list() # or use []

# Pre Order Printing
def print_pre_order(root):
    if root is None:
        return

    print(root.data, end=" ")

    for node in root.children:
        print_pre_order(node)

# Root: Child Relation type printing
def print_tree_detailed(root):
    if root.data is None:
        return

    print(f"{root.data}:", end="")

    for node in root.children:
        if node is not None:
            print(node.data, end=",")
    
    print()

    for node in root.children:
        print_tree_detailed(node)

# Create Tree via User Input Data
def take_user_input():
    userInput = int(input("Enter Root Data: "))
    if userInput == -1:
        return None

    root = GenericTreeNode(userInput)

    child_count = int(input(f"Enter Number of children of {root.data}: "))

    for _ in range(child_count):
        childNode = take_user_input()
        root.children.append(childNode)

    return root

# Node Count in Generic Tree
def generic_tree_node_count(root):
    # Not the base case but edge case
    if root is None:
        return 0
    
    count = 1

    for child in root.children:
        count = count + generic_tree_node_count(child)

    return count

# Defining Nodes
gt_root = GenericTreeNode(5)
gt_1 = GenericTreeNode(2)
gt_2 = GenericTreeNode(9)
gt_3 = GenericTreeNode(8)
gt_4 = GenericTreeNode(7)
gt_5 = GenericTreeNode(15)
gt_6 = GenericTreeNode(1)

# Defining Relationships
gt_root.children.append(gt_1)
gt_root.children.append(gt_2)
gt_root.children.append(gt_3)
gt_root.children.append(gt_4)

gt_2.children.append(gt_5)
gt_2.children.append(gt_6)

# Normal Display
print("Tree in PreOrder")
print_pre_order(gt_root)
print()

# Well Formatted Display
print("Tree in more Intutive Fashion")
print_tree_detailed(gt_root)
print(f"Count of Nodes: {generic_tree_node_count(gt_root)}")

# Take User Input
print("Take User Input")
root = take_user_input()
print_tree_detailed(root)
print(f"Count of Nodes: {generic_tree_node_count(root)}")