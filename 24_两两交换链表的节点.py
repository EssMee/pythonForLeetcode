class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head:ListNode):
        if not head or not head.next:
            return head
        m = head.next
        head.next = self.swapPairs(m.next)
        m.next = head
        
        return next

if __name__ == "__main__":
    sol = Solution()
    sol.swapPairs([1,2,3,4,5])