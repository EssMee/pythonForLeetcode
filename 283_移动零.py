class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        遇到0的时候把第一个0移掉，并且末尾再加一个0即可。
        """
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(0)

        
sol = Solution()
print(sol.moveZeroes([0,2,0,4,8,0,12]))
