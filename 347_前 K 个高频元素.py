from collections import _heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: inta
        :rtype: List[int]
        """
        num_dict = {}
        for num in nums:
            num_dict[num] = num_dict[num] + 1 if num in num_dict else 1
        
        return _heapq.nlargest(k, num_dict.keys(), key = num_dict.get)
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))
        
        
        
