import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = nums
        self.original = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.array = self.original
        self.original = list(self.original)
        return self.array

        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        duplicate = list(self.array)
        for i in range(len(self.array)):
            random_index = random.randrange(len(duplicate))
            self.array[i] = duplicate.pop(random_index)
        return self.array
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

sol = Solution([1,2,3])
print(sol.shuffle())