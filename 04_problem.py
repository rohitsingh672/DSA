# Leetcode Problem 4 : Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
nums1 = [1, 2]
nums2 = [3, 4]
merge = sorted(nums1 + nums2) # [1, 2, 3, 4]
n = len(merge) # 4
if n % 2 == 0:
    median = ((merge[n//2 - 1] + merge[n//2]) / 2) # (merge[1] + merge[2]) / 2 = (2 + 3) / 2 = 2.5
else:
    median = merge[n//2] # Not applicable in this case
print(median) # median = 2.5

# In python 2 when we perform division between two integer value then it provide me the integer value
# Example: 5/2 = 2 in python 2
# But in python 3 5/2 = 2.5 in the new version of python it changes the behaviour of /(division)