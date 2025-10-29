from linked_list_operations_module import takeInput, printLinkedList

def bubbleSort(head) :
    """
    Sorts a linked list using bubble sort algorithm.
    """
    if head is None:
        return None

    count = 0

    curr = head

    while curr:
        curr_next = curr.next
        while curr_next:
            if curr.data > curr_next.data:
                curr_next.data, curr.data = curr.data, curr_next.data
            curr_next =curr_next.next
        curr = curr.next

    return head

#main
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)
