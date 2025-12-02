"""
Elements Between K1 and K2

Problem statement
Given a Binary Search Tree and two integers k1 and k2, find and print the elements which are in range k1 and k2 (both inclusive).

Print the elements in increasing order.

Sample Input 1:
8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
6 10
Sample Output 1:
6 7 8 10
"""
from tree_operations_module import take_input_level_wise, print_level_wise

def elementsInRangeK1K2(root, k1, k2):
    if root is None:
        return
    
    if root.data < k1:
        elementsInRangeK1K2(root.right, k1, k2)
    elif root.data > k2:
        elementsInRangeK1K2(root.left, k1, k2)
    else:
        elementsInRangeK1K2(root.left, k1, k2)
        print(root.data, end=" ")
        elementsInRangeK1K2(root.right, k1, k2)

# Main
root = take_input_level_wise()
k1, k2= list(map(int, input("Enter k1 and k2: ").split()))
print_level_wise(root)
print("Elements b/w k1 and k2:")
elementsInRangeK1K2(root, k1, k2)