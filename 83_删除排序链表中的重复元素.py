class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #    "rtype" = ListNode
    def deleteDuplicates(self, head:ListNode):
        dummy_head = ListNode(None)
        dummy_head.next = head

        pre = dummy_head
        cur = head

        while cur:
            if pre and cur.val == pre.val:
                pre.next = cur.next
                cur.next = None
                cur = pre.next
                continue

            pre = cur
            cur = cur.next
        return dummy_head.next
