import collections
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = collections.Counter(nums)
        for key in dict.keys():
            if dict[key] > 1:
                return True
        return False

sol = Solution()
print(sol.containsDuplicate([1,1,2,3]))