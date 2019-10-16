class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = ""
        t = ""
        for i in S:
            if i == "#":
                if s:
                    s = s[:-1]
            else:
                s += i
    
        for j in T:
            if j == "#":
                if t:
                    t = t[:-1]
            else:
                t += j
        return s == t

sol = Solution()
print(sol.backspaceCompare("a#b##c","a#c"))
            
