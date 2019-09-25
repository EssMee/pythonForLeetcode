class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if len(nums) <3 :
            return None
        nums.sort()
        temp = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            l = i + 1 
            r = len(nums) - 1 
            while l < r :
                sum = nums[i] + nums[l] + nums[r]
                if abs(target - sum) < abs(target - temp):
                    temp = sum
                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    return temp
        return temp
sol = Solution()
print(sol.threeSumClosest([-1,2,1,-4], 1)) 