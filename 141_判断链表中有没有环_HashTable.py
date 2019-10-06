# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head:ListNode):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head and not head.next:
            return False
        
        p = head
        st = set()
        while p:
            if p in st:
                return True
            st.add(p)
            p = p.next
        return False
        
        
                
        