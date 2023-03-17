"""https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

for each interval I, we consider whether it overlaps with other. If so, we need to remove it

We can understand this question as to find the minimum number of "overlapping" intervals to remove because any non-overlapping interval will not contribute to the number.

There is no need to consider the content in the result intervals as long as they do not overlap with each other.

When two intervals I1 and I2 overlap with each other, we consider removing I1 or I2 (2 cases). If we are using a search method (e.g., DFS), we need a branch here

Observe

Intervals are easier to process when they are sorted.

123
  345
    56
   4567

"""

# %%
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda i: i[1])

        # The minimum number of intervals to remove to make the reset non-overlap
        # === size - the max number of non-overlapping intervals

        # Count starts from 1 because there is at least one interval
        count = 1
        cur_max_end = sorted_intervals[0][1]
        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i][0] >= cur_max_end:
                cur_max_end = sorted_intervals[i][1]
                count += 1

        return len(sorted_intervals) - count

        # sorted_intervals = sorted(intervals, key=lambda i: i[0])

        # # the upperbound of the number of intervals + 1
        # self.min_removed = 10**5+1

        # def _test(cur_i, most_recent_iv, cur_r):
        #     # Reaching beyond the end of input, stop
        #     if cur_i >= len(sorted_intervals):
        #         self.min_removed = min(self.min_removed, cur_r)

        #     # If the current number of removed has exceed the minimum, stop early
        #     if cur_r >= self.min_removed:
        #         return

        #     # The current interval
        #     cur_iv = sorted_intervals[cur_i]

        #     # Always test removing the current interval
        #     _test(cur_i + 1, most_recent_iv, cur_r + 1)

        #     # Only test keeping the current interval if no overlapping
        #     if most_recent_iv is None or most_recent_iv[1] <= cur_iv[0]:
        #         _test(cur_i + 1, cur_iv, cur_r)

        # _test(0, None, 0)

        # return self.min_removed


# Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])
# Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]])
# Solution().eraseOverlapIntervals([[1, 2], [2, 3]])
Solution().eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]])
