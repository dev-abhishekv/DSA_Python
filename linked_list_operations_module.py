# Definition for singly-linked list node
class Node :
    """
    Node class for singly linked list.
    Each node contains data and a pointer to the next node.
    """
    def __init__(self, data) :
        self.data = data
        self.next = None


# to take input for linked list
def takeInput() : 
    """
    Take input from the user to create a linked list.
    Input ends when user enters -1.
    Returns the head of the linked list.
    """
    head = None
    tail = None

    datas = list(map(int, input("Enter the List: ").split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


# to print the linked list
def printLinkedList(head) :
    """
    Print the linked list starting from head.
    """
    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


def cloneLinkedList(head):
    """
    Return a deep copy of the linked list starting at head.
    """
    if head is None:
        return None
    new_head = Node(head.data)
    new_tail = new_head
    curr = head.next
    while curr:
        new_node = Node(curr.data)
        new_tail.next = new_node
        new_tail = new_node
        curr = curr.next
    return new_head
