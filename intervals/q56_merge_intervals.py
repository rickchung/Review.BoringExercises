"""https://leetcode.com/problems/merge-intervals/
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

# %%

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [1, 3] + [2, 6] => [1, 6]
        [1, 3] + [5, 6] => [[1, 3], [5, 6]]

        Whether two intervals I1 and I2 are overlapping can be seen by checking
        their heads and tails. To make it simpler, always treat the one with
        the left-most head as I1.

        To avoid searching everywhere, we can try to sort the input to 
        make sure every next item has H >= Hi

        Then, there are only two cases to work with:

            1. If the current interval I overlaps with the next I',
            merge I and I'
            
            2. Otherwise, add the merged interval so far to the result,
            and then use the non-ovarlapping I' to continue

        """

        # When there are not enough intervals to run the business
        if len(intervals) <= 1:
            return intervals

        # Sort the intervals in ascending order
        intervals = sorted(intervals, key=lambda x: x[0])

        rt = []
        mi = intervals[0]
        
        for i in range(1, len(intervals)):
            (h1, t1), (h2, t2) = mi, intervals[i]
            """
            [1, 2, 3, 4, 5, 6, 7] t1
                     [4, 5, 6, 7, 8, 9, 10] t1 > h2
                              [7, 8, 9, 10] t1 == h2
                                 [8, 9, 10] t1 < h2
            """
            if t1 >= h2:
                mi[1] = max(t1, t2)
            else:
                rt.append(mi)
                mi = intervals[i]

            # If we're reaching the end, add the last merged/new interval
            if i == len(intervals) - 1:
                rt.append(mi)

        return rt

s = Solution()

intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
s.merge(intervals)

