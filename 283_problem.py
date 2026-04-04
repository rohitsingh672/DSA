# Leetcode Problem 283 : Move Zeroes at the end
nums = [0,3,2,8,0,0,5,6,9,0]
temp = [] # Stores non zero element
n = len(nums) # Length of nums is 10

for i in range(0,n): #loops runs from indx 0 to index 9
    if nums[i] != 0:
        temp.append(nums[i]) # Inside temp = [3,2,8,5,6,9]

s = len(temp) # Length of temp is 6
for i in range(0,s): # Loop inside the temp from index 0 to index 5
    nums[i] = temp[i] # nums[3,2,8,5,6,9]
for i in range(s,n): # Loop inside the nums from index 7 to index 9 
    nums[i] = 0 # nums[3,2,8,5,6,9,0,0,0,0]
    
print(nums)

