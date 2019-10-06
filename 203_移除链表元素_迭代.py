# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        cur = prev.next
        
        while cur:
            if cur.val == val:
                prev.next = cur.next
                cur = prev.next
            else:
                prev = prev.next
                cur = prev.next
        return dummy.next

            