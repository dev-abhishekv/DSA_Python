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

# Basic structure of Linked List Operations
# Definition for singly-linked list node
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

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
m, n = map(int, input("Enter M and N: ").split())
head = swapNodes(head, m, n)
printLinkedList(head)