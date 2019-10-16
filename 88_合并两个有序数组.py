class Solution(object):
<<<<<<< HEAD
    def merge(self, nums1,m, nums2,n):
=======
    def merge1(self, nums1, m, nums2, n):
>>>>>>> 9845326d6aa92f2b824d9c714d0e054fa7861017
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
<<<<<<< HEAD
        """     
        nums1[:] = sorted(nums1[:m] + nums2)
        
=======
        """
        nums1[:] = sorted(nums1[:m] + nums2)
        
    def merge2(self, nums1, m, nums2, n):
        # Time: O(m+n)
        # Space: O(m)
        p1 = 0
        p2 = 0
        
        another_nums1 = nums1[:m]
        nums1[:] = []
        while p1 < m and p2 < n:
            if another_nums1[p1] < nums2[p2]:
                nums1.append(another_nums1[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        
        if p1 < m:
            nums1[p1+p2:] = another_nums1[p1:]
        if p2 < n:
            nums1[p1+p2:] = nums2[p2:]
>>>>>>> 9845326d6aa92f2b824d9c714d0e054fa7861017
