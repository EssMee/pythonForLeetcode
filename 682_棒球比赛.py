class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        
        stack = []
        for op in ops:
            if op == "+":
                stack.append((stack[-1] + stack[-2]))
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()

            else:
                stack.append(int(op))
        return sum(stack)
sol = Solution()
print(sol.calPoints(["5","2","C","D","+"]))
