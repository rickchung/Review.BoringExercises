"""https://leetcode.com/problems/house-robber/
"""
# %%

nums = [1, 2, 3, 1]
nums = [2, 7, 9, 3, 1]

best_robs = [-1] * len(nums)
best_robs[0] = nums[0]
best_robs[1] = max(best_robs[0], nums[1])

for i in range(2, len(nums)):
    best_robs[i] = max(best_robs[i - 2] + nums[i], best_robs[i - 1])

print(best_robs)
