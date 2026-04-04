# Leetcode Problem 1365 : How Many Numbers Are Smaller Than the Current Number
nums = [8,5,3,6,7]
ans = []
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] > nums[j]:
            count += 1
    ans.append(count)
print(ans)