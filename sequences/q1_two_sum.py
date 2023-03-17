"""https://leetcode.com/problems/two-sum/
"""
# %%

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    cache = {}
    for i, ni in enumerate(nums):
        d = target - ni
        idx = cache.get(d, [])
        # If the diff is not in cache, add num: index to the cache
        if len(idx) == 0:
            idx.append(i)
            cache[ni] = idx
        # If the diff is in cache, we found the answer
        else:
            return (i, idx[0])
    return []

nums, target = [2, 7, 11, 15], 9
nums, target = [3, 2, 4], 6
nums, target = [3, 3], 6

twoSum(nums, target)
