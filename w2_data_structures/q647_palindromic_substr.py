"""https://leetcode.com/problems/palindromic-substrings/

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

s = "abc"
[a], [b], [c]

s = "aaa"
[a0] [a0, a1], [a1] [a0, a1, a2], [a1, a2], [a2]

Every char and space between two chars can be a center of palindromes.
There are 2*N - 1 possible centers. 

For each center c, we expand and check if (c-1, c, c+1) is a palindrome. 
Continue until it is not or we go beyond the boundary.


"""

# %%


class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        # Every char and space between two chars can be a center of palindromes
        n_centers = 2 * len(s) - 1

        for i in range(n_centers):
            left = i // 2
            right = left + i % 2
            
            # check to (c-1, c, c+1) until reaching the boundary
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1

        return cnt



Solution().countSubstrings("abc")  # 3
Solution().countSubstrings("aaa")  # 6
