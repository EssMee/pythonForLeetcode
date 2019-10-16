import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = collections.Counter(s)
        i = 0 
        for char in s:
            if c[char] == 1:
                return i
            else:
                i += 1
        return -1

sol = Solution()
print(sol.firstUniqChar("loveleetcode"))
