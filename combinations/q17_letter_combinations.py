"""https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

# %%

from typing import List


class Solution:
    def __init__(self):
        self.keyboard = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        self.answers = []

        def _combine(cur_ans, opts_lb):
            if len(cur_ans) == len(digits):
                self.answers.append("".join(cur_ans))
            else:
                for i in range(opts_lb, len(digits)):
                    for c in self.keyboard[digits[i]]:
                        cur_ans.append(c)
                        _combine(cur_ans, i+1)
                        cur_ans.pop()

        _combine([], 0)
        return self.answers


# Solution().letterCombinations("23")
# Solution().letterCombinations("")
Solution().letterCombinations("2")
