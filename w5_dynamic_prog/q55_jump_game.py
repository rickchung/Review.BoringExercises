"""https://leetcode.com/problems/jump-game/
"""

# %%

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        [2, 3, 1, 1, 4]

        Option 1: BF procedure

            At i = 0,
                Go to +1 (i = 1)
                    Go to +1 (i = 2)
                    Go to +2 (i = 3)
                    Go to +3 (i = 4) (Win)
                Go to +2 (i = 2)
                    ...

            Alternative representation:

            [2, 3, 1, 1, 4], last_i = 4
                [(*1, 2), (1, 2, *3), (1, ), (1, ), (NA)]
                (s1 = 1) + (s2 = 3) = 4

            This is costly because for each index i, 
            there may be M elements to test. If there are
            N indices to scan, we end up with O(M^N)

        Option 2:

            To know whether the last index L can be reached from
            index 0, do we really need to scan all paths?

            Relevant information:

            L is reachable from index 0 if 
                * any index L-i before it has enough jumps that covers L
                * any index L-i is also reachable from index 0

            f(i) = 
                0 if it i is not reachable from index 0
                K if i is reachable from index 0 and K is the
                furthest index we can go from i

            [2, 3, 1, 1, 4]

            f(0) = 2
            f(1) = 0 if f(0) < 1 else max(f(0), 1 + 3) = 4
            f(2) = 0 if f(1) < 2 else max(f(1), 2 + 1) = 4
            f(3) = 0 if f(2) < 3 else max(f(2), 3 + 1) = 4
            STOP

            [3, 2, 1, 0, 4]

            f(0) = 3
            f(1) = 0 if f(0) < 1 else max(f(0), 1 + 2) = 3
            f(2) = 0 if f(1) < 2 else max(f(1), 2 + 1) = 3
            f(3) = 0 if f(2) < 3 else max(f(2), 3 + 0) = 3

            [1, 0, 2, 1, 4]

            f(0) = 1
            f(1) = 0 if f(0) < 1 else max(f(0), 1 + 0) = 1
            f(2) = 0 if f(1) < 2 else max(f(1), 2 + 2) = 0
            f(3) = 0 if f(2) < 3 else max(f(2), 3 + 1) = 0

            f(i) = 0 if f(i - 1) < i else max(f(i - 1), i + nums[i])
        """

        if len(nums) == 1:
            return True

        cache = [0] * len(nums)
        cache[0] = nums[0]

        for i in range(1, len(nums)):
            cache[i] = (
                0 if cache[i - 1] < i else 
                max(cache[i - 1], i + nums[i]))

        return cache[-1] > 0


s = Solution()

cases = [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
]

for nums, ans in cases:
    print(f"Input={nums} Output={s.canJump(nums)} Ans={ans}")
