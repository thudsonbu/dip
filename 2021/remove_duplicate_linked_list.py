# given a sorted linked list of integers, remove ll the duplicate elments in
# the linked list so that all elements in the linked list are unique.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next    

    def __repr__(self):
        return f"({self.value}, {self.next})"


def remove_dup(lst):

    while lst.next:
        if lst.next.value == lst.value:
            if lst.next.next:
                lst.next = lst.next.next
            else:
                lst.next = None
                break
        
        lst = lst.next


lst = Node(1, Node(2, Node(2, Node(3, Node(3)))))

remove_dup(lst)
print(lst)
# (1, (2, (3, None)))
