# Leetcode Problem 1 : Two Sum
# Example nums = [2,5,6,4] target = 11 Output = [1,2] indexing of the number whose sum is present
nums = [2,5,6,4]
target = 11
n = len(nums) # Length of n is 4

for i in range(0,n): # loop inside nums from index 0 to index 3
    for j in range(i+1,n): # loop inside nums from index 1 to index 3
        if nums[i] + nums[j] == target: # nums[i](5) + nums[j](6) == target(11)
            print([i,j]) # print [1,2]