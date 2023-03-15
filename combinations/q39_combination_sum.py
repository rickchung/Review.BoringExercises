"""https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""

# %%

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answers = []
        def _comb_sum(cur_ans, opts_lb, target):
            if target < 0:
                return
            elif target == 0:
                answers.append(tuple(cur_ans))
            else:
                for i in range(opts_lb, len(candidates)):
                    item = candidates[i]
                    cur_ans.append(item)
                    _comb_sum(cur_ans, i, target - item)
                    cur_ans.pop()

        _comb_sum([], 0, target)
        return answers
    
Solution().combinationSum([2, 3, 5], 8)
# Solution().combinationSum([2], 1)
