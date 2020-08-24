
def check_cycle(head):
    if not head or not head.next:
        return False
    reverse_head = reverse_list(head)
    if reverse_head is head:
        return True
    else: 
        return False

def reverse_list(current):
    previous = None
    while(current):
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt
    return previous

def reverseList(head):
    new_head = None
    while head:
      tmp = head.next
      head.next = new_head
      new_head = head
      head = tmp
    return new_head
        
def print_list(root):
    if not root:
        return
    else:
        while(root):
            print(root.val)
            if not root.next:
                break
            root = root.next

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(3)
node2.next = node3

print_list(reverse_list(node1))
print(check_cycle(node1))