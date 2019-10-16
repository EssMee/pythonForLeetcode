class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        hashmap = {}
        # 倒序地放入一个栈中
        for i in nums2:
            while len(stack) != 0 and stack[-1] < i:
                hashmap[stack.pop()] = i
            stack.append(i)
        
        return [hashmap.get(i, -1) for i in nums1]

sol = Solution()
print(sol.nextGreaterElement([4,1,2], [1,3,4,2]))
        
