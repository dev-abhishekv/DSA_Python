"""
Check if a linked list is a palindrome using O(1) space and O(n) time.

-> The apprroach involves fast and slow pointer technique to find the middle of the list,
reversing the second half of the list in place, and then comparing the two halves.
"""

# Definition for singly-linked list node
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def isPalindrome(head) :
    # 1st Iteration got middle term in O(n/2)
    if head is None:
        return True

    slower = faster_2x = head

    while faster_2x.next and faster_2x.next.next:
        slower = slower.next
        faster_2x = faster_2x.next.next
    
    middle = slower

    # 2nd Iteration got second half reversed
    prev_node = None
    new_head = middle.next

    while new_head:
        next_node = new_head.next
        new_head.next = prev_node
        prev_node = new_head
        new_head =next_node
    
    middle.next = prev_node
    new_head = prev_node
    
    # 3rd Iteration compare the 1st half with 2nd half
    while new_head:
        if head.data == new_head.data:
            head = head.next
            new_head = new_head.next
        else:
            return False
    
    return True

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

#main
head = takeInput()

# check for palindrome
if isPalindrome(head) :
    print('true')
else :
    print('false')