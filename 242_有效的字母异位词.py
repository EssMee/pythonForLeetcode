import collections
class Solution(object):
    # def isAnagram1(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     if len(s) != len(t):
    #         return False
    #     else:
    #         dict1 = collections.Counter(s)
    #         dict2 = collections.Counter(t)
    #         if dict1 == dict2:
    #             return True
    #         else:
    #             return False
    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        else: return False


sol = Solution()
print(sol.isAnagram2("anagram","nagaram"))