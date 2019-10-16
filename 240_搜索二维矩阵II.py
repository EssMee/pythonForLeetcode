class Solution(object):
    def searchMatrix1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
<<<<<<< HEAD
        # Time: O(mn)
=======
        # Time:O(mn)
>>>>>>> 9845326d6aa92f2b824d9c714d0e054fa7861017
        # Space: O(1)
        for row in matrix:
            if target in row:
                return True
        return False
        
    def searchMatrix2(self, matrix, target):
<<<<<<< HEAD
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        H = len(matrix)
        W = len(matrix[0])
        
        start_row = H - 1
        start_col = 0
        
        while start_col < W and start_row >= 0:
            if matrix[start_row][start_col] < target:
                start_col += 1
            elif matrix[start_row][start_col] > target:
                start_row -=1
            else:
                return True
        
        
        return False
        
    def searchMatrix3(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """   
        # 如果没有排序特性的话呢？
        # 把二位矩阵压成一维数组可以吗？
=======
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    H = len(matrix)
    W = len(matrix[0])

    start_row = H - 1
    start_col = 0

    while start_col < W and start_row >= 0:
        if matrix[start_row][start_col] < target:
            start_col += 1
        elif matrix[start_row][start_col] > target:
            start_row -=1
        else:
            return True


    return False
        
    def searchMatrix3(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """   
    # 如果没有排序特性的话呢？
    # 把二位矩阵压成一维数组可以吗？
>>>>>>> 9845326d6aa92f2b824d9c714d0e054fa7861017
        l = []
        for a in range(len(matrix)):
            for num in matrix[a]:
                l.append(num)
        if target in l:
            return True
        else:
            return False

<<<<<<< HEAD
            
        
    
    
=======
                
>>>>>>> 9845326d6aa92f2b824d9c714d0e054fa7861017

sol = Solution()
print(sol.searchMatrix1([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 40))

print(sol.searchMatrix2([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
<<<<<<< HEAD
], 40))
=======
], 4))
>>>>>>> 9845326d6aa92f2b824d9c714d0e054fa7861017

print(sol.searchMatrix3([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
<<<<<<< HEAD
], 50))
=======
], 4))
        
>>>>>>> 9845326d6aa92f2b824d9c714d0e054fa7861017
