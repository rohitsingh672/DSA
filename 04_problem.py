# Leetcode Problem 4 : Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
nums1 = [1, 2]
nums2 = [3, 4]
merge = sorted(nums1 + nums2) # [1, 2, 3, 4]
n = len(merge) # 4
if n % 2 == 0:
    median = (merge[n//2 - 1] + merge[n//2]) / 2 # (merge[1] + merge[2]) / 2 = (2 + 3) / 2 = 2.5
else:
    median = merge[n//2] # Not applicable in this case
print(median) # median = 2.5