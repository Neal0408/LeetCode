nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

# 1st method.
# while k > 0:
#     nums.insert(0, nums[len(nums) - 1])
#     nums.pop()
#     k -= 1

# 2nd method.
nums[:] = nums[-k % len(nums):] + nums[:-k % len(nums)]

