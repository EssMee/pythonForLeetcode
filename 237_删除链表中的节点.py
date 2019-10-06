# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
    #  从链表里删除一个节点 node 的最常见方法是修改之前节点的 next 指针，使其指向之后的节点。
    #  因为，我们无法访问我们想要删除的节点 之前 的节点，我们始终不能修改该节点的 next 指针。
    #  相反，我们必须将想要删除的节点的值替换为它后面节点中的值，然后删除它之后的节点。
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        node.val = node.next.val
        node.next = node.next.next
        
    # 附加一个方法， 查找值为x的节点 
    def findNode(self, x):
        if not x: return 

        cur = ListNode(0)
        while cur != None:
            if cur.val == x:
                return cur
            cur = cur.next
        return None
