def hop(curr, N):
    '''
    Hops N nodes ahead from the current node.
    '''
    count = 0
    while count != N and curr:
        count += 1
        curr = curr.next

    return curr

def skipMdeleteN(head, M, N) :
    '''
    Skips M nodes and deletes N nodes in the linked list.
    '''
    
    if head is None:
        return head

    # If M is 0, we delete the entire list
    if M == 0:
        return None
    
    # If N is 0, we do not delete any nodes
    if N == 0:
        return head

    prev = None
    curr = head
    count = 0

    while curr:
        count += 1
        prev = curr
        curr = curr.next

        if count == M:
            count = 0
            curr = hop(curr, N)
            prev.next = curr

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
head = skipMdeleteN(head, m, n)
printLinkedList(head)