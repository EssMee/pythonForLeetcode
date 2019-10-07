class ListNode(object):
    def __init__(self, val=None, node_next = None):
        self.val = val
        self.next = node_next
class MyLinkedList(object):    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode()
        self.size = 0
        
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index > self.size:
            raise ValueError('Get failed. Illegal index.')
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):           
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
    
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        return self.addAtIndex(self.size, val)
        """************************
        添加的方法好像还有问题
        **********"""
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index >= self.size:
            raise ValueError("invalid index")
        elif index < 0:
            return self.addAtHead(val)
        else:
            prev = self.head
            for i in range(index):
                prev = prev.next
            newNode = ListNode(val)
            newNode.next = prev.next
            prev.next = newNode
            self.size += 1
        
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            raise ValueError('Remove failed. Illegal index.')
        prev = self.head
        for i in range(index):
            prev = prev.next
        remove_node = prev.next
        prev.next = remove_node.next
        remove_node.next = None
        self.size -= 1