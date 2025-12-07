"""
Print Level Wise Tree

Problem statement
Given a generic tree, print the input tree in level wise order.

For printing a node with data N, you need to follow the exact format -

N:x1,x2,x3,...,xn
where, N is data of any node present in the generic tree. x1, x2, x3, ...., xn are the children of node N. Note that there is no space in between.
You need to print all nodes in the level order form in different lines.
"""

from generic_tree_operations_module import take_level_wise_input_via_single_list
import sys
import queue

sys.setrecursionlimit(10**6)

def printLevelWiseTree_1(tree):
    if tree is None:
        return

    q = queue.Queue()

    q.put(tree)

    while not q.empty():
        current_node = q.get()
        print(current_node.data, end=":")

        # print("Current Children: ", current_node.children)

        for child in current_node.children:
            print(child.data, end="")
            if child == current_node.children[-1]:
                print(end="")
            else:
                print(end=",")
            q.put(child)

        print()

def printLevelWiseTree_2(tree):
    if tree is None:
        return

    q = queue.Queue()

    q.put(tree)

    while not q.empty():
        current_node = q.get()

        # print("Current Children: ", current_node.children)

        child_li = []
        for child in current_node.children:
            child_li.append(str(child.data))
            q.put(child)
        
        child_li_str = ",".join(child_li)
        print(f"{current_node.data}:{child_li_str}")

# Main

arr = list(int(x) for x in input().strip().split(' '))
tree = take_level_wise_input_via_single_list(arr)
print("Via Way 1 using if-else:")
printLevelWiseTree_1(tree)
print("Via Way 2 using join method:")
printLevelWiseTree_2(tree)