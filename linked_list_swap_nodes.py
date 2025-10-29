def swapNodes(head, i, j):
    '''
    Swap nodes at position i and j in a linked list by swapping their data.
    '''
	# Count the no. of Node in the Linked List
    count = 0

    if head is None:
        return head 
    
    if i == j:
        return head
    
    ith_node = jth_node = None

    curr = head
    while curr:
        count += 1
        if count == i+1:
            ith_node = curr
        
        if count == j+1:
            jth_node = curr
        
        if ith_node and jth_node:
            break
        
        curr = curr.next
    
    temp = ith_node.data
    ith_node.data = jth_node.data
    jth_node.data = temp

    return head


def swapActualNodes(head, i, j) :
    """
    Swap nodes at position i and j in a linked list by changing links.
    """
    # Count the no. of Node in the Linked List
    index = -1

    if head is None:
        return head 
    
    if i == j:
        return head
    
    FirstNode = SecondNode = None
    FirstPrev = SecondPrev = None
    
    curr = head
    
    while curr:
        index += 1
        if index == i-1:
            FirstPrev = curr
            FirstNode = curr.next

        if index == j-1:
            SecondPrev = curr
            SecondNode = curr.next
        
        if FirstPrev and SecondPrev:
            break
        
        curr = curr.next
    
    if i == 0:
        FirstNode = head
        head = SecondNode
        
        SecondPrev.next = SecondNode.next
        SecondNode.next = FirstNode.next
        
        FirstNode.next = SecondPrev.next
        SecondPrev.next = FirstNode
    elif SecondPrev == FirstNode:
        SecondPrev.next =SecondNode.next
        SecondNode.next = SecondPrev
        
        FirstPrev.next = SecondNode
    else:
        FirstPrev.next = FirstNode.next
        SecondPrev.next = SecondNode.next

        SecondNode.next = FirstPrev.next
        FirstPrev.next = SecondNode

        FirstNode.next = SecondPrev.next
        SecondPrev.next = FirstNode
    
    return head

# Basic structure of Linked List Operations
# Definition for singly-linked list node
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


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


# to take input linked list
def takeInput() : 
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


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
head = takeInput()
clone_head = cloneLinkedList(head)
m, n = map(int, input("Enter M and N: ").split())
print("Swapping data of nodes:")
head = swapNodes(head, m, n)
printLinkedList(head)
print("Swapping actual nodes:")
clone_head = swapActualNodes(clone_head, m, n)
printLinkedList(clone_head)