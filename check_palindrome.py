# You are given a doubly linked list. Determine if it is a palindrome.

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next

def is_palindrome(node):
    first_node = node
    last_node = node
    length = 0

    while last_node.next:
        last_node = last_node.next
        length += 1
    
    while length >= 0:
        if first_node.val != last_node.val:
            return False
        first_node = first_node.next
        last_node = last_node.prev
        length -=1

    return True


print(is_palindrome(node))