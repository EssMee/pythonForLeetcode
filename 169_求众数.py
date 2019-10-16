class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # overtime
        # st = len(nums) // 2
        # count = 0
        # for num in nums:
        #     count = sum(1 for ele in nums if ele == num)
        #     if count > st: 
        #         return num
        nums.sort()
        max_length = len(nums)
        return nums[len(nums)//2]
sol = Solution()
print(sol.majorityElement([3,2,3,2,2]))
print(sol.majorityElement([3,2,3,2,2]))

