"""
For a given a Binary Tree of type integer, find and return the minimum and the maximum data values.
Return the output as an object of Pair class, which is already created.

Note:
All the node data will be unique and hence there will always exist a minimum and maximum node data.

Sample Input 1:
8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
Sample Output 1:
1 14

"""
from tree_operations_module import take_input_level_wise

#Representation of the Pair Class
class Pair :

    def __init__(self, minimum, maximum) :
        self.minimum = minimum
        self.maximum = maximum


def getMinAndMax(root) :
    if root is None:
        return Pair(float('inf'), float('-inf'))
    
    left_data =  getMinAndMax(root.left)
    right_data = getMinAndMax(root.right)

    minimum =  min(left_data.minimum, right_data.minimum, root.data)
    maximum =  max(left_data.maximum, right_data.maximum, root.data)

    return Pair(minimum, maximum)


# Main
root = take_input_level_wise()

pair = getMinAndMax(root)
print("Min and Max Values are: ", end= " ")
print(str(str(pair.minimum) + " " + str(pair.maximum)))