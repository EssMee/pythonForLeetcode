# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# s = ListNode(None)
# print(s.val) ==> None
# print(s.next)==> None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head
        while cur != None:
            next = cur.next
             
            cur.next = prev
            prev = cur
            cur = next
        return prev