class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        res[0] = self.arrProduct(nums[1:])
        res[len(nums)-1] = self.arrProduct(nums[:len(nums)-1])
        for i in range(1, len(nums) -1 ):
            res[i] = self.arrProduct(nums[:i]) * self.arrProduct(nums[i+1:])
        return res
    def arrProduct(self, nums):
        product = 1
        for i in range(len(nums)):
            product *=  nums[i]
        return product

sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))