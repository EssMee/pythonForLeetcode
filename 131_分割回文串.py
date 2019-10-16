class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
            return [[]]
        if len(s) == 1:
            return [[s]]

        res = []
        for i in range(1,len(s)+1):
            left = s[:i]
            right = s[i:]
            if left == left[::-1]: # 如果左边是回文的话，继续查看右边是不是回文
                right = self.partition(right) #递归地查看右边
                for i in range(len(right)):
                    res.append([left]+right[i])
        return res
<<<<<<< HEAD

    
#     def ishuiwen(self,s):
#         "rtype: bool"
#         i = 0
#         j = len(s) - 1 
#         while i < j:
#             if s[i] == s[j]:
#                 return True
#             else:
#                 i += 1
#                 j -= 1
#         return False

sol = Solution()
print(sol.partition("aab"))
# print(sol.ishuiwen("abbac"))
=======
>>>>>>> b1586ea9535a3a7a0a5a8538497bcb34b8e03c4c
