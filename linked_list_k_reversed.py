from linked_list_operations_module import takeInput, printLinkedList

def reverseLinkedList(head, terminate_node):
    """
    Reverses a linked list.
    """

    if head is None:
        return head, head

    prev = next = tail = None
    curr = head

    while curr and curr != terminate_node:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    head.next = None

    return prev, head

def reverseLinkedList(head, terminate_node):
    """
    Reverses a linked list.
    """

    if head is None:
        return head, head

    prev = next = tail = None
    curr = head

    while curr and curr != terminate_node:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    head.next = None

    return prev, head

def kReverse(head, m):
    if head is None or m == 0:
        return head

    node_count = 0
    curr = head
    # Keep track of head for each of M node groups
    present_head = None
    # Keep track of last node of previously modified M grouped node and next node of the un-modified linked list
    prev_tail = next_head = None
    while curr:
        if present_head is None:
            present_head = curr

        node_count += 1
        next_head = curr.next

        if node_count % m == 0:
            # present_tail.next = None
            new_head, new_tail = reverseLinkedList(present_head, next_head)

            if prev_tail is not None:
                prev_tail.next = new_head
                new_tail.next = next_head
            else:
                head = new_head
                new_tail.next = next_head
            
            present_head = None
            prev_tail = new_tail
            curr = new_tail

        curr = curr.next

    if prev_tail:
        new_head, new_tail = reverseLinkedList(present_head, next_head)
        prev_tail.next = new_head

    return head

t = int(input("Enter Test Cases: "))

while t > 0 :
    
    head = takeInput()
    k = int(input("Enter Value of k: "))

    newHead = kReverse(head, k)
    printLinkedList(newHead)

    t -= 1