# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        tmp = [] # 用于存储链表
        while head:
            tmp.append(head.val)
            head = head.next
            
        l = 0
        r = len(tmp) - 1
        while l < r:
            if tmp[l] != tmp[r]:
                return False
            l += 1
            r -= 1
        return True