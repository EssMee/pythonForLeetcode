class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        sum = 0
        for i in range(len(s) - 1):
            if dict[s[i]] >= dict[s[i+1]]:
                sum = sum + dict[s[i]]
            else:
                sum = sum - dict[s[i]]
        last_num = s[len(s) - 1]
        sum = sum + dict[last_num]

        return sum

sol = Solution()
print(sol.romanToInt("MCMXCIV"))
            
                