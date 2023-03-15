"""https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""

# %%

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answers = []
        opts_up = len(candidates)

        def _combination(cur_comb: List, target, opts_lb):
            if target == 0:
                answers.append(tuple(cur_comb))
            elif target > 0:
                for i in range(opts_lb, opts_up):
                    c = candidates[i]
                    cur_comb.append(c)
                    _combination(cur_comb, target - c, i + 1)
                    cur_comb.pop()

        _combination([], target, 0)
        return answers


# Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
Solution().combinationSum2([2, 5, 2, 1, 2], 5)


# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates.sort()

#         answers = []
#         opts_up = len(candidates)

#         def _combination(cur_comb: List, target, opts_lb):
#             if target == 0:
#                 answers.append(tuple(cur_comb))
#             elif target > 0:
#                 prev_c = 0
#                 for i in range(opts_lb, opts_up):
#                     c = candidates[i]
#                     if c != prev_c:
#                         cur_comb.append(c)
#                         _combination(cur_comb, target - c, i + 1)
#                         cur_comb.pop()
#                     prev_c = c

#         _combination([], target, 0)
#         return answers
