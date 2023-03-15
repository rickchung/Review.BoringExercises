"""https://leetcode.com/problems/longest-repeating-character-replacement/

Input: a string s and int k
Ops: change one char to anohter
Output: the length of the longest substring containing the same letter after the replacement

Examples:

    ABAB, 2 => AAAA or BBBB => 4
    AABABBA, 1 => AABBBBA => 4

Observations:

    * When we scan the input string from end to end, we know the count of each alphabet
    * In the range we scan (window), there must be one longest substring X which conains the same letter
"""

# %%

from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        win_alph_counter = Counter()
        max_count = 0
        win_start = 0
        for win_end, a in enumerate(s):
            win_alph_counter[a] += 1
            max_count = max(max_count, win_alph_counter[a])
            win_size = win_end - win_start + 1
            if win_size - max_count > k:
                win_alph_counter[s[win_start]] -= 1
                win_start += 1

        return win_end - win_start + 1
        
# Solution().characterReplacement("ABAB", 2)
# Solution().characterReplacement("AABABBA", 1)
# Solution().characterReplacement("AABA", 0)
# Solution().characterReplacement("BAAAB", 2)
