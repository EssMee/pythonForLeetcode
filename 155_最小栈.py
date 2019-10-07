class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.size = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        self.size += 1
    

    def pop(self):
        """
        :rtype: None
        """
        if self.size == 0:
            return 
        self.stack.pop()
        self.size -= 1


    def top(self):
        """
        :rtype: int
        """
        if self.size == 0:
            return
        return self.stack[-1]
    
    def getMin(self):
        """
        :rtype: int
        """
        for i in range(len(self.stack)):
            return min(self.stack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
minstak = MinStack()
minstak.push(-2)
minstak.push(0)
minstak.push(-3)
print(minstak.size)
print(minstak.getMin())
print(minstak.pop())
print(minstak.top())
print(minstak.getMin())
