"""https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n]. You may return the answer in any order.

We can see that a BF approach will lead to many duplications, e.g., [1, 2] and [2, 1]. I think the key is to avoid such duplications when possible.

Strategy:
* Choose one valut at i
* Add nums[i] to the current combination
* Limit next possible choices to values after i
* Repeat until we have no more choices OR we have had k elements
"""

# %%

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answers = []
        choice_upper = n + 1

        def _combine(cur_comb, opts_lb, remaining):
            if remaining == 0:
                answers.append(tuple(cur_comb))
            for i in range(opts_lb, choice_upper):
                cur_comb.append(i)
                _combine(cur_comb, opts_lb=i+1, remaining=remaining-1)
                cur_comb.pop()

        _combine([], 1, k)

        return answers


Solution().combine(4, 2)
Solution().combine(1, 1)
