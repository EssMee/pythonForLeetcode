class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.size = 0
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.stack.append(num)
        self.size += 1

    def findMedian(self):
        """
        :rtype: float
        """
        res = 0
        self.stack.sort()
        if self.size <= 0: return
        elif self.size == 1: return self.stack[0]
        elif self.size % 2 == 1: 
            # 奇数个
            res = self.stack[int((self.size - 1) / 2)]
        else:
            # 偶数个
            res = (self.stack[int(self.size / 2 - 1)] + self.stack[int(self.size / 2)]) / 2
        return res        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

mef = MedianFinder()
mef.addNum(1)
mef.addNum(2)
# mef.addNum(3)
# mef.addNum(4)
print(mef.findMedian())
