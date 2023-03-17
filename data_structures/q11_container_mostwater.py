"""https://leetcode.com/problems/container-with-most-water/

Input: heights of vertical lines
Output: the max amount of water a container can store

amount = min(height[i], height[j]) * (j - i)

Opt 1: BF by computing all possible amounts and choose the maximum

Opt 2: The amount of water is mainly contrainted by the lower side and the distance between two lines

When we scan the input, for each i we know (1) the highest bar so far and (2) the distance between i and the highest bar

Say the highest bar is at index Hi, can we formulate the problem to a DP problem like

f(i) 
    = the max amount of water from 0 to i
    = max(f(i - 1), heights[i] * (i - Hi))

This will go wrong when there is a higher bar in the middle.

Opt 3: Moving from two sides

Start with head and tail. 

Because only the smaller side will affect the level of water, each round we 

    Compute the current level of water 
    Keep max level of water in a variable.
    Move the lower side.
    Repeat until the head and tail cross over each other.


"""
# %%
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        max_amt = 0
        hi, ti = 0, len(height) - 1

        while hi < ti:
            if height[hi] > height[ti]:
                amt = height[ti] * (ti - hi)
                ti -= 1
            else:
                amt = height[hi] * (ti - hi)
                hi += 1
            
            max_amt = max(amt, max_amt)

        return max_amt


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
height = [1, 1]

Solution().maxArea(height)
