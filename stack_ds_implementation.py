# Stack implementation using Array
class StackArr:
    def __init__(self):
        self.__arr = []
    
    def push(self, value):
        self.__arr.append(value)

    def pop(self):
        if self.size() == 0:
            print("Stack is Empty")
            return 
        
        return self.__arr.pop()

    def top(self):
        if self.size() == 0:
            print("Stack is Empty")
            return 
        
        return self.__arr[len(self.__arr) - 1]

    def size(self):
        return len(self.__arr)

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def printStack(self):
        for i in self.__arr[self.size()::-1]:
            print(i)

# Stack implementation using LinkedList
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class StackLL:
    def __init__(self):
        self.__head = None
        self.__node_count = 0

    def push(self, value):
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node
        
        self.__node_count += 1

    def pop(self):
        if self.size() == 0:
            print("Stack is Empty")
            return 
        
        # Take the data of node popped for printing
        data =  self.__head.data

        # Move head to next
        self.__head = self.__head.next
        
        # Reduce the count since one node is popped
        self.__node_count -= 1

        # return the data popped
        return data

    def top(self):
        if self.size() == 0:
            print("Stack is Empty")
            return 
        
        return self.__head.data

    def size(self):
        return self.__node_count

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def printStack(self):
        curr = self.__head
        while curr:
            print(curr.data)
            curr = curr.next

# TEST OPERATIONS
    # stack = StackLL() # Or StackArr() for Array Implementation
    # stack.push(5)
    # stack.push(10)
    # stack.push(30)
    # print("----")
    # stack.printStack()
    # print("----")
    # stack.pop()
    # stack.printStack()
    # print("----")
    # stack.pop()
    # stack.pop()
    # print(stack.top())
    # print(stack.size())
    # print(stack.isEmpty())

