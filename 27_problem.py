# Leetcode Problem 27 : Remove Elements
nums = [1,2,3,4]
val = 3

k = 0  # pointer for valid elements

for i in range(len(nums)):
    if nums[i] != val:
        nums[k] = nums[i]
        k += 1

print("New length:", k)
print("Array after removing element:", nums[:k])