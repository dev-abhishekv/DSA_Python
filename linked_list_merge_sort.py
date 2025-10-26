class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def mergeTwoSortedLinkedLists(head1, head2):
    head = tail = None

    if head1 is None:
        return head2
    
    if head2 is None:
        return head1

    while head1 and head2:
        if head1.data <= head2.data:
            if head is None:
                head = tail = head1
            else:
                tail.next = head1
                tail = head1
            
            head1 = head1.next
        else:
            if head is None:
                head = tail = head2
            else:
                tail.next = head2
                tail = head2
            
            head2 = head2.next

    if head1:
        tail.next = head1
    
    if head2:
        tail.next = head2
    

    return head

def getMidNode(head):
    slow = fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


def mergeSort(head) :
	# Return when only one node is left
    if head is None or head.next is None:
        return head

    mid_node = getMidNode(head)

    mid_next = mid_node.next
    mid_node.next = None

    ll_1 = mergeSort(head)
    ll_2 = mergeSort(mid_next)

    new_head = mergeTwoSortedLinkedLists(ll_1, ll_2)

    return new_head

#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, input("Enter List: ").split(" ")))

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




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


# Main
t = int(input("Enter Test Cases: "))

while t > 0 :
    
    head = takeInput()

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1