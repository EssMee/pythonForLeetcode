# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head.next
        while (slow != fast):
            if (fast == None or fast.next == None):
                return False
            
            slow = slow.next
            fast = fast.next
        return True
    
        slow = head
        fast = head
    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
                
