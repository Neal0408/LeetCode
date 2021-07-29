nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]

i = 0
j = 1
while i < j & j < len(nums) - 1:
    if nums[i] == nums[j]:
        if nums[i] == nums[j + 1]:
            nums.pop(j + 1)
            i -= 1
            j -= 1
    i += 1
    j += 1

print(nums)



