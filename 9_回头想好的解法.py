class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 如果正反的ascii一样是不是就是回文了？
        # 粗略解法： 整数转换字符串
        # test = str(x)
        # if len(test) <= 1:
        #     return True
        # str_len = len(test)
        # rev = test[::-1]
        # for i in range(str_len):
        #     if test[i] == rev[i]:
        #         return True
        #     return False
        
        # or
        return str(x) == str(x)[::-1]
            

        