class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def count_element(head, val):
	current = head
	counter = 0
	while current:
		if current.value == val:
			counter += 1
		current = current.next
	return counter

# Input List: 3 -> 1 -> 2 -> 1
# Input: head = 3, val = 1
# 2

linked_list = Node(3,Node(1,Node(2,Node(1))))
print(count_element(linked_list, 1))