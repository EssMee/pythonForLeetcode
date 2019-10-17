# from collections import defaultdict
# dict = defaultdict()
# dict[1] =2 
# dict[2]= 3 
# dict[3] = 4
# a = [0,0,1,2,3]
# a.remove(0)
# a.sort()
# sorted(a)

def is_Sorted(nums):
    for i in range(len(nums)):
        if nums[i+1] == nums[i] + 1:
            return True
        return False

print(is_Sorted([1,2,3,4]))