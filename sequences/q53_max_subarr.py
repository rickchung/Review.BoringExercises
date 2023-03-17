"""https://leetcode.com/problems/maximum-subarray/
"""

# %%

from typing import List


class Solution:
    def _maxSubArray(self, nums: List[int]) -> int:
        # Look for the best values for subarrays ending at index i
        sum_max_i = [0] * len(nums)
        sum_max_i[0] = nums[0]
        sum_global = sum_max_i[0]

        # For each new index i, we consider disposing the previous sum or not
        # If so, f(i) = nums[i] + 0 because f(i-1) is not worth keeping
        # Otherwise, f(i) = nums[i] + f(i-1)
        for i in range(1, len(nums)):
            sum_max_i[i] = nums[i] + max(sum_max_i[i - 1], 0)
            sum_global = max(sum_global, sum_max_i[i])

        return sum_global


s = Solution()

test_cases = [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([5, 4, -1, 7, 8], 23),
    ([1, 2], 3),
    ([31, -41, 59, 26, -53, 58, 97, -93, -23, 84], 187),
    ([-1, 0, -2], 0),
    ([-1, 1, 2, 1], 4)
]

for t, a in test_cases:
    print("Ans", s._maxSubArray(t), "\n")
