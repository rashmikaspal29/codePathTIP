class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

# def is_palindrome(head):
#      current = head
#      reverseCur = 
# 	while cur

def is_palindrome(head):
    x = []

    current = head

    while current:
        x.append(current.value)
        current = current.next
    
    reverse = x[::-1]
    return x == reverse

linked_list = Node(1,Node(2,Node(1)))
print(is_palindrome(linked_list))