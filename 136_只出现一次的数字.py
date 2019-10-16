class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(n)
        new_list = []
        for num in nums:
            if num not in new_list:
                new_list.append(num)
            else:
                new_list.remove(num)
        
        return new_list.pop()

        # # Time: O(n)
        # # Space: O(1)
        # a = 0
        # for num in nums:
        #     a ^= num
        # return a

sol = Solution()
<<<<<<< HEAD
print(sol.singleNumber([1,2,2,1,4]))
=======
print(sol.singleNumber([1,2,2,1,4]))
>>>>>>> 9845326d6aa92f2b824d9c714d0e054fa7861017
