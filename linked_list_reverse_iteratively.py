# Definition for singly-linked list node
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

# Reverses the linked list iteratively
def reverse_linked_list(head):
    prev = next_ = None

    while head:
        next_ = head.next
        head.next = prev
        prev = head
        if next_ is not None:
            head = next_
        else:
            return head
    
    return head

#to take input linked list
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, input().split(" ")))

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

new_head = reverse_linked_list(head)

print("Reversed LinkedList")
while new_head:
    print(new_head.data, end= " ")
    new_head = new_head.next