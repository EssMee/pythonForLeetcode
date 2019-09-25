# Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = fast = head
        for i in range(n):          # 先让fast走n步
            fast = fast.next
        if fast == None:            # 若走了n步后为None，则表明删除的为head节点
            return head.next
        
        while fast.next != None:    # slow和fast同时往前走
            slow = slow.next        # 当fast走到头时，second即是要删除节点的前一个节点位置
            fast = fast.next
        slow.next = slow.next.next  # 删除该节点
        return head
sol = Solution()
print(sol.removeNthFromEnd([1,2,3,4,5], 2))