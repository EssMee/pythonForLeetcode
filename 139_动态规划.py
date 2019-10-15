class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s == '':
            return True
        if len(wordDict) == 1:
            if s == wordDict[0]:
                return True
            else:
                return False
 
        dp = [0 for _ in range(len(s)+1)]
        dp [0] = 1
        for i in range(len(s)):
            str_ = s[:i+1]
            for j in range (i+1):
                if str_ in wordDict and dp[j]:
                    dp[i+1] = 1
                str_ = str_[1:]
        return dp[len(s)] == 1
