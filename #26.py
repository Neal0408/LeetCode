nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# 1st method
i = 0
j = 1
k = len(nums)-1
while i < k:
    if nums[i] != nums[j]:
        i += 1
        j += 1
    else:
        nums.pop(i)
        k -= 1

print(nums)

