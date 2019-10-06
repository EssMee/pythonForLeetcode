class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def generation( A = []):
            if len(A) == 2 * n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append("(")
                generation(A)
                A.pop()
                A.append(")")
                generation(A)
                A.pop()

        def valid(A):
            balance = 0
            for m in A:
                if m == "(": balance += 1
                else: balance -= 1
                if balance < 0:
                    return False
            return balance == 0
        
        
        generation()
        return ans
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))
    