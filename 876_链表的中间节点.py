# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        list = [head]
        while list[-1].next:
            list.append(list[-1].next)
        return list[len(list) /2 ]
        