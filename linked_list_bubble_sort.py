from linked_list_operations_module import takeInput, printLinkedList

def bubbleSort(head) :
    """
    Sorts a linked list using bubble sort algorithm.
    """
    if head is None:
        return None

    swap_flag = False

    curr = head

    while curr:
        curr_next = curr
        while curr_next and curr_next.next:
            if curr_next.data > curr_next.next.data:
                curr_next.data, curr_next.next.data = curr_next.next.data, curr_next.data
                if not swap_flag:
                    swap_flag = True
            curr_next =curr_next.next
        if not swap_flag:
            break
        curr = curr.next

    return head

#main
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)
