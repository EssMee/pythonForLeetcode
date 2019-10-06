# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        hashIDs = {}
        while headA:
            hashIDs[id(headA)] = 1
            headA = headA.next
        
        while headB:
            if (id(headB) in hashIDs):
                return headB
            headB = headB.next
        