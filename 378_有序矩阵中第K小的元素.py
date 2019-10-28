class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        origin_arr = []
        for i in range(len(matrix)):
            for j in matrix[i]:
                origin_arr.append(j)
        
        origin_arr.sort()

        return origin_arr[k-1]
