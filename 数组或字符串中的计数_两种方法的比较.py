import collections
nums = [1,1,2,3]
dict1 = collections.Counter(nums)
dict2 = {}
for num in nums:
    dict2[num] = dict2[num] + 1 if num in dict2 else 1

	
# dict1
# Counter({1: 2, 2: 1, 3: 1})
# dict2
# {1: 2, 2: 1, 3: 1}
# >>> dict1[0]
# 0
# >>> dict1[1]
# 2
# >>> dict2[1]
# 2