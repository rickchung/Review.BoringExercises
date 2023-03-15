"""https://leetcode.com/problems/combination-sum-iii/

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

    Only numbers 1 through 9 are used.
    Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
"""

# %%

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answers = []

        def _combine(cur_ans, target, left_steps, opts_lb, opts_ub=9+1):
            if target == 0 and left_steps == 0:
                answers.append(tuple(cur_ans))
            elif target > 0 and left_steps > 0:
                for i in range(opts_lb, opts_ub):
                    cur_ans.append(i)
                    _combine(cur_ans, target - i, left_steps-1, i+1)
                    cur_ans.pop()

        _combine([], n, k, 1)
        return answers


# Solution().combinationSum3(3, 7)
# Solution().combinationSum3(3, 9)
Solution().combinationSum3(4, 1)
