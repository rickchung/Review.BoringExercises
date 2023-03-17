"""https://leetcode.com/problems/longest-increasing-subsequence/
"""
# %%
from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    # Array of len(LISS) that ends at ni
    sub_lens = [1 for _ in nums]

    for next_item_index, next_item in enumerate(nums):
        ops = []
        # If the next item is greater than the tail of subsequence
        # it will have a chance to expand an existing LISS (fi = fj + 1)
        for sub_tail_index, sub_tail in enumerate(nums[:next_item_index]):
            if next_item > sub_tail:
                ops.append(sub_lens[sub_tail_index])
        # Find the longest LISS from the existing LISS if available
        if ops:
            sub_lens[next_item_index] = max(ops) + 1
    return max(sub_lens)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
# nums = [0, 1, 0, 3, 2, 3]
# nums = [7, 7, 7, 7, 7, 7, 7]
print(lengthOfLIS(nums))
