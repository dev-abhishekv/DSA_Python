# Approach 1: Here we are traversing to tail everytime and then assigning the next to head TC: O(n^2) 
def reverseLinkedList_1(head):
    if head is None or head.next is None:
        return head

    new_head = reverseLinkedList_1(head.next)

    tail = new_head

    while tail.next:
        tail = tail.next
     
    tail.next = head
    head.next = None

    return new_head

# Here we always have reference to tail so no more traversing at each step TC: O(n)
def reverseLinkedList_2(head):
    if head is None or head.next is None:
        return head

    tail = head.next

    new_head = reverseLinkedList_2(head.next)

    tail.next = head # Can reduce on no. of variables by using head.next.next instead of tail
    head.next = None

    return new_head


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

# Check via Way 1
head = takeInput()
new_head = reverseLinkedList_1(head)

print("Reversed LinkedList 1")
printLinkedList(new_head)


# Check via Way 2
head = takeInput()

new_head_2 = reverseLinkedList_2(head)
print("Reversed LinkedList 2")
printLinkedList(new_head_2)