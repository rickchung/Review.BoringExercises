"""https://leetcode.com/problems/contains-duplicate/
"""
# %%

from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    cache = {}
    for i in nums:
        if cache.get(i, 0) == 1:
            return True
        cache[i] = 1
    return False


nums = [1, 2, 3, 1]
nums = [1, 2, 3, 4]
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
containsDuplicate(nums)
