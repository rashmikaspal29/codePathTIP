# a -> b
# insert c

# result using add_first(a. c)

# c
# a -> b

# c -> a

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
		
def add_first(head, new_node):
	new_node.next = head
	return new_node

# c
# a -> b

# c -> a

node_2 = Node("Wigglypuff", next=None)
node_1 = Node("Jigglypuff", next=node_2)

# Using the Linked List from Problem 2
print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)

# output:
# Jigglypuff -> Wigglypuff
# Ditto -> Jigglypuff
#node_1.next = node_2
#node_3.next = node_1?