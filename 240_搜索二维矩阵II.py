class Solution(object):
    def searchMatrix1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Time:O(mn)
        # Space: O(1)
        for row in matrix:
            if target in row:
                return True
        return False
        
        
