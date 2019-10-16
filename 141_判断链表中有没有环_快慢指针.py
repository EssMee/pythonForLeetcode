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
    """
    （1）求环长：第二次相遇的时候，慢指针走过的距离就是环长。
    （2）求入环点： 把慢指针停在第一次相遇的地方，快指针回到头节点，两个指针每次向前走动一步，相遇的地方就是入
    """
                
        
