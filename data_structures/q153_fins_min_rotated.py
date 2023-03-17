"""https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Input: list of numbers in ascending order which are rotated between 1-n times
Output: the minimum element in the list

Obs:
* the list is sorted in ascending order
* the list is always rotated to the right

Opt1:
    An input may looks like

    head [..., min, ...] tail
    
    We do not know how many items are before and after the minimu min. But for any
    item i in the sequence, it must be part of an ascending sequence

    [asc1, max, min, asc2]
    
    If we pick up an M in the middle, it may be in asc1-max, exactly max or min, or min-asc2.

    [H, ..., M, ..., T]

    if H < M < T, the min must be in [H:M] (perfect ascending list)
    if H > M < T, the min must be in [H:M] (rotated ascending list)
    if H < M > T, the min must be in [M:T] (rotated ascending list)
    if H > M > T, the input is invalid (that's descending list)
"""
# %%

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        n_min = 5001
        head, tail = 0, len(nums) - 1
        while head < tail:
            middle = (head + tail) // 2
            nh, nm, nt = nums[head], nums[middle], nums[tail]
            n_min = min(nh, nt, nm, n_min)
            
            print(f"{head}:{nh}, {middle}:{nm}, {tail}:{nt}")

            if (nh <= nm < nt) or (nh > nm and nm < nt):
                print("in [H:M]")
                tail = middle - 1
            elif nh <= nm and nm >= nt:
                print("in [M:T]")
                head = middle + 1

        return n_min


# nums = [3, 4, 5, 1, 2]
# nums = [4, 5, 6, 7, 0, 1, 2]
# nums = [11, 13, 15, 17]
nums = [0, 1]
Solution().findMin(nums)
