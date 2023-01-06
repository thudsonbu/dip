# You are given an array of k linked-lists lists, each linked-list is sorted in
# ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        if len(lists) == 2:
            return self.mergeLists(lists[0], lists[1])

        if len(lists) > 2:
            split_pt = len(lists) // 2

            l1 = self.mergeKLists(lists[0:split_pt])
            l2 = self.mergeKLists(lists[split_pt:])

            return self.mergeLists(l1, l2)

        return lists

    def mergeLists(self, l1, l2):
        head = ListNode()
        ref = head

        while l1 and l2:
            if l1.val < l2.val:
                ref.next = l1
                ref = ref.next
                l1 = l1.next
            else:
                ref.next = l2
                ref = ref.next
                l2 = l2.next

        if l1:
            ref.next = l1
        else:
            ref.next = l2

        return head.next
