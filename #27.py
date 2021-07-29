nums = [3, 2, 2, 3]
val = 3

# 1st method
for i in range(len(nums)-1, -1, -1):
    print(list(range(len(nums)-1, -1, -1)))
    if nums[i] == val:
        nums.remove(nums[i])

# 2nd method
i = 0
for j in range(0, len(nums)):
    if nums[j] != val:
        nums[i] = nums[j]
        i += 1



