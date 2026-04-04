# Leetcode 26 : Remove Duplicates from Sorted Array
nums = [0,0,1,1,1,2,2,3,3,4]

if nums:
    i = 0  # pointer for unique elements
    
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    k = i + 1
else:
    k = 0

print("New length:", k)
print("Array after removing duplicates:", nums[:k])