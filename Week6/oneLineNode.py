# make 3 objects
#Problem 1
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
linked_list = Node(4,Node(3,Node(2)))

print(linked_list.value)
print(linked_list.next.value)
print(linked_list.next.next.value)

#just do f stieing for 1 line
