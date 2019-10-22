class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) - k]

sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2))
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
