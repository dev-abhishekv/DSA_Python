# Definition for singly-linked list node
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

# Reverses the linked list recursively and returns the new head and tail
def reverse_linked_list(head, new_head = None):
    if head == None:
        return head, None
    
    new_head, tail = reverse_linked_list(head.next)
    
    if new_head is None:
        new_head = Node(head.data)
        tail = new_head
    else:
        tail.next = Node(head.data)
        tail = tail.next
        
    return new_head, tail

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

new_head, tail = reverse_linked_list(head)

print("Reversed LinkedList")
while new_head:
    print(new_head.data, end= " ")
    new_head = new_head.next