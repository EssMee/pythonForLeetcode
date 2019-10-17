class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        
        # if nums.is_Sorted():
        for i in range(len(nums) -2 ):
            j = i + 1
            k = j + 1 
            if nums[j] == (nums[i] + nums[k]) / 2:
                if nums[k] > nums[j] and nums[j] > nums[i]:
                    return True
                else:
                    i += 1
        return False

    # else:
        #     pass

    # def is_Sorted(self, nums):
    #     for i in range(len(nums)):
    #         if nums[i+1] == nums[i] + 1:
    #             return True
    #         return False
sol = Solution()
print(sol.increasingTriplet([2,1,5,0,4,6]))
print("这为啥返回是True啊， 我理解错题意了？ \n [0,1,2],[4,5,6]这也可以算递增子序列么？ ")
        
        