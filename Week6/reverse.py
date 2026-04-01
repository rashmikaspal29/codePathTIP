

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def reverse(head):
    x = []
    current = head

    while current:
        x.append(current.value)
        current = current.next
    
    reverse = x[::-1]
    print(reverse)
    return current 

linked_list = Node(1,Node(2,Node(3,Node(4))))


 
 

# Input List: 1 -> 2 -> 3 -> 4
# Input: head = 1

# Expected Return Value: 4
# Expected Result List: 4 -> 3 -> 2 -> 1