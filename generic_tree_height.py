"""
Find height of Generic Tree
Problem statement
Given a generic tree, find and return the height of given tree. The height of a tree is defined as the longest distance from root node to any of the leaf node.
Assume the height of a tree with a single node is 1.

Sample Input 1:
10 3 20 30 40 2 40 50 0 0 0 0 

Sample Output 1:
3
"""
import sys
import queue

class GenericTreeNode:
    def __init__(self, data):
        self.data: int = data
        self.children: list = []

#main
sys.setrecursionlimit(10**6)
## Read input as specified in the question.
def take_level_wise_input_gt(li: list) -> None:
    if len(li) == 0:
        return None
    
    q: queue.Queue = queue.Queue()

    i: int = 0

    root: GenericTreeNode = GenericTreeNode(li[i])

    i += 1

    q.put(root)

    while not q.empty():
        curr_node: GenericTreeNode = q.get()
        children_count: int= li[i]
        i += 1
        for j in range(i, i+children_count):
            child_node: GenericTreeNode = GenericTreeNode(li[j])
            q.put(child_node)
            curr_node.children.append(child_node)

        i += children_count

    return root

## Get Height of Tree
def get_gt_tree_height(root: GenericTreeNode) -> None:
    if root is None:
        return 0
    
    li = [0]
    
    for child in root.children:
        li.append(get_gt_tree_height(child)) 

    return 1 + max(li)

# Get height of Tree
def get_gt_tree_height_improved(root: GenericTreeNode) -> int:
    if root is None:
        return 0
    
    max_height = 0
    for child in root.children:
        child_height = get_gt_tree_height(child)
        
        if child_height > max_height:
            max_height = child_height
    
    return 1 + max_height

li: list = list(map(int, input("Enter List: ").split()))
root: GenericTreeNode = take_level_wise_input_gt(li)
print(get_gt_tree_height(root))
print(get_gt_tree_height_improved(root))