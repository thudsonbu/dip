# Hi, here's your problem today. This problem was recently asked by AirBNB:

# Given a linked list and a number k, rotate the linked list by k places.

# Here's some starter code and an example:

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    current = self
    ret = ''
    while current:
      ret += str(current.value)
      current = current.next
    return ret

# First solution (16 minutes)
def rotate_list(llist, k):
    pos = 1
    pos_node = llist
    while pos_node.next:
        pos_node = pos_node.next
        pos += 1
    pos_node.next = llist
    k = k % pos
    pos = 1
    pos_node = llist
    while pos < k:
        pos_node = pos_node.next
        pos += 1
    new_start = pos_node.next
    pos_node.next = None
    return new_start

# Order is 1, 2, 3, 4
llist = Node(1, Node(2, Node(3, Node(4))))

# Order should now be 3, 4, 1, 2
print(rotate_list(llist, 2))
# 3412