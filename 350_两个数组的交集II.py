class Solution(object):
    # def intersect(self, nums1, nums2):
    #     """
        # :type nums1: List[int]
        # :type nums2: List[int]
        # :rtype: List[int]
        # """
        # # res = []
        # inter = set(nums1) & set(nums2)
        # for i in inter:
        #     res += [i] * min(nums1.count(i), nums2.count(i))
        # return res
    
    def intersect2(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        res = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res
sol = Solution()
print(sol.intersect2([1,2,2,1], [2,2]))
        
                