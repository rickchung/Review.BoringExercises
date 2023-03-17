"""https://leetcode.com/problems/house-robber-ii/
"""

# %%
nums = [1, 2, 3, 1]
nums = [10, 2, 3, 3, 2, 4]
nums = [1, 2, 3]
nums = [1, 2, 1, 1]
nums = [8, 4, 8, 5, 9, 6, 5, 4, 4, 10]


def _rob(nums):
    print("Input", nums)

    bv_hin = [False] * len(nums)
    bvs = [0] * len(nums)

    bv_hin[0] = True
    bvs[0] = nums[0]

    if bvs[0] > nums[1]:
        bvs[1] = bvs[0]
        bv_hin[1] = True
    else:
        bvs[1] = nums[1]
        bv_hin[1] = False

    for i in range(2, len(nums) - 1):
        cur = nums[i]
        bv1 = bvs[i-1]
        bv2 = bvs[i-2]
        print(f"Proc {cur} bv1 {bv1} bv2 {bv2}")
        if cur + bv2 > bv1:
            bvs[i] = cur + bv2
            if bv_hin[i-2]:
                bv_hin[i] = True
        else:
            bvs[i] = bv1
            if bv_hin[i-1]:
                bv_hin[i] = True

    bv1, bv2 = bvs[-1-1], bvs[-1-2]
    p1hi, p2hi = bv_hin[-1-1], bv_hin[-1-2]
    if p1hi and not p2hi:
        bvs[-1] = bv2 + nums[-1]
    elif not p1hi and p2hi:
        bvs[-1] = bv1
    elif p1hi and p2hi:
        bvs[-1] = nums[-1]
    else:
        bvs[-1] = max(bv1, bv2 + nums[-1])

    print("Output", list(zip(bvs, bv_hin)))
    print()

_rob(nums)
_rob(nums[::-1])