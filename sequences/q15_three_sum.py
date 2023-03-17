"""https://leetcode.com/problems/3sum/

Input: [-1, 0, 1, 2, -1, -4]
"""

# %%

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    pos, neg, zero = [], [], []
    for n in nums:
        if n > 0:
            pos.append(n)
        elif n < 0:
            neg.append(n)
        else:
            zero.append(n)

    set_pos = set(pos)
    set_neg = set(neg)

    res = set()

    if zero:
        if len(zero) >= 3:
            res.add(tuple(sorted((0, 0, 0))))
        for p in pos:
            if -p in set_neg:
                res.add(tuple(sorted((p, 0, -p))))
        for n in neg:
            if -n in set_pos:
                res.add(tuple(sorted((n, 0, -n))))
    
    for p1i, p1 in enumerate(pos):
        for p2i, p2 in enumerate(pos):
            if p1i == p2i:
                continue
            if -(p1 + p2) in set_neg:
                res.add(tuple(sorted((p1, p2, -(p1 + p2)))))

    for n1i, n1 in enumerate(neg):
        for n2i, n2 in enumerate(neg):
            if n1i == n2i:
                continue
            if -(n1 + n2) in set_pos:
                res.add(tuple(sorted((n1, n2, -(n1 + n2)))))

    return res


threeSum([-1, 0, 1, 2, -1, -4])
# threeSum([0, 0, 0])
# threeSum([0, 1, 1])

# %%
