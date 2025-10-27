def evenAfterOdd(head) :
    '''
    Rearranges the linked list such that all odd indexed nodes are
    followed by all even indexed nodes, maintaining the relative order of both odd and even nodes.
    '''
    if head is None:
        return head
    
    # odd head, odd tail, even_head, even_tail
    oh = ot = eh = et = None

    curr = head
    
    while curr:
        # pointer to next node of curr
        next = curr.next

        if curr.data % 2 == 0:
            if eh is None:
                eh = et = curr
            else:
                et.next = curr
                et = curr
        else:
            if oh is None:
                oh = ot = curr
            else:
                ot.next = curr
                ot = curr
        curr = next

    if et:
        et.next = None
    if ot:
        ot.next = None
    
    if oh:
        ot.next = eh
        return oh
    else:
        return eh

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
head = evenAfterOdd(head)
printLinkedList(head)