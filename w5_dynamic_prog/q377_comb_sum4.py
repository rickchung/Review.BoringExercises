"""https://leetcode.com/problems/combination-sum-iv/

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.
"""
# %%

from typing import List


class Solution:

    def combinationSum4(self, nums: List[int], target: int) -> int:
        n_ways = {}

        def _find(target):
            if target in n_ways:
                print(n_ways)
                return n_ways[target]
            elif target > 0:
                for c in nums:
                    if target - c == 0:
                        n_ways[target] = n_ways.get(target, 0) + 1
                    else:
                        n_ways[target] = n_ways.get(target, 0) + _find(target - c)
                return n_ways[target]
            else:
                return 0
        
        return _find(target)

    # def combinationSum4(self, nums: List[int], target: int) -> int:
    #     n_ways = [0] * 1001
    #     for i in range(target + 1):
    #         for j in nums:
    #             if i - j == 0:
    #                 n_ways[i] += 1
    #             elif i - j > 0:
    #                 n_ways[i] += n_ways[i - j]
    #     return n_ways[target]

    # def combinationSum4(self, nums: List[int], target: int) -> int:
    #     self.n_ways = 0

    #     def _combine(target):
    #         if target == 0:
    #             self.n_ways += 1
    #         elif target > 0:
    #             for c in nums:
    #                 _combine(target - c)
        
    #     _combine(target)
    #     return self.n_ways

Solution().combinationSum4([1, 2, 3], 4)
# Solution().combinationSum4([9], 0)
# Solution().combinationSum4([4, 2, 1], 32)
