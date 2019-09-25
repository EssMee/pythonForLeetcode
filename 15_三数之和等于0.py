# 思路
# 标签：数组遍历
# 首先对数组进行排序，排序后固定一个数 nums[i]nums[i]，再使用左右指针指向 nums[i]nums[i]后面的两端，数字分别为 nums[L]nums[L] 和 nums[R]nums[R]，计算三个数的和 sumsum 判断是否满足为 00，满足则添加进结果集
# 如果 nums[i]nums[i]大于 00，则三数之和必然无法等于 00，结束循环
# 如果 nums[i]nums[i] == nums[i-1]nums[i−1]，则说明该数字重复，会导致结果重复，所以应该跳过
# 当 sumsum == 00 时，nums[L]nums[L] == nums[L+1]nums[L+1] 则会导致结果重复，应该跳过，L++L++
# 当 sumsum == 00 时，nums[R]nums[R] == nums[R-1]nums[R−1] 则会导致结果重复，应该跳过，R--R−−
# 时间复杂度：O(n^2)O(n^2 )，nn 为数组长度
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        i = 0

        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                l = i + 1
                r = len(nums) - 1 
                while l < r :
                    s = nums[i] + nums[l] + nums[r]
                    if s == 0:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]: #去重
                            l += 1
                        while l+1 < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif s > 0:
                        r -= 1 
                    else:
                        l += 1
        return res

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
                
        
                