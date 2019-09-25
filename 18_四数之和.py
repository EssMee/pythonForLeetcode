# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
# 使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 链接：https://leetcode-cn.com/problems/4sum
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = set()
        for i in range(len(nums)-3):
            for j in range(i + 1 , len(nums) -2 ):
                l = j + 1 
                r = len(nums) - 1 
                while l < r :
                    temp = nums[i] + nums[j] + nums[l] + nums[r]
                    if temp == target:
                        ans.add((nums[i],nums[j], nums[l],nums[r]))
                        l += 1
                        r -= 1
                    elif temp > target:
                        r -= 1
                    else:
                        l += 1
        res = []
        for i in ans:
            res.append(list(i))                  
        return res

sol = Solution()
print(sol.fourSum([1,0,-1,0,-2,2], 0))

        