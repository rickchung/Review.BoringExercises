"""https://leetcode.com/problems/product-of-array-except-self/
"""

# %%

from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    """
    n1: prod(n2, n3, n4, n5)
    n2: prod(n1, n3, n4, n5)
    n3: prod(n1, n2, n4, n5)
    n4: prod(n1, n2, n3, n5)
    n5: prod(n1, n2, n3, n4)

    Opt 1: BF
        f(ni) = prod(N - {ni})  # O(n^2)

    Opt 2: divide & conquer
        Cache products such as (n1, n2), (n1, n2, n5)

    Opt 3:

        f(n1) = prod({n2, n3, n4, n5})
        to compute f(n1) only, it's easy

        prod = 1
        for i in {n2, n3, n4, n5}, 
            prod *= i

        In this process, we can also get these from the two sides
            prod(n1) | prod(n2, n3, n4)
            prod(n1, n2) | prod(n3, n4)
            prod(n1, n2, n3) | prod(n4)
            prod(n1, n2, n3, n4)

            i = 0, 1, 2, 3
            A [1 p(n1), 2 p(n1:n2), 6 p(n1:n3), 1]

            j = 3, 2, 1, 0
            B [4 p(n4), 12 p(n3:n4), 24 p(n2:n4), 1]

            [          i       j
                rt[0]: A[-1] * B[2]
                rt[1]: A[0]  * B[1]
                rt[2]: A[1]  * B[0]
                rt[3]: A[2]  * B[-1]
            ]

            rt[i + 1] *= A[i]
            rt[j - len(nums) + 1] *= B[j]

    Special case: 0
        f(i) = prod(N / {ni}) where ni = 0
        f(j) = 0 where nj != 0
    """

    zeros = []
    A, B = [], []
    pnz = 1
    pa, pb = 1, 1
    for i in range(len(nums)):
        j = len(nums) - 1 - i

        if nums[i] != 0:
            pnz *= nums[i]

        if i == len(nums) - 1:
            if nums[i] == 0:
                zeros.append(i)
            pa = pb = 1
        else:
            if nums[i] == 0:
                zeros.append(i)
            else:
                pa *= nums[i]

            if nums[j] != 0:
                pb *= nums[j]

        A.append(pa)
        B.append(pb)

    if len(zeros) > 1:
        rt = [0] * len(nums)
    elif len(zeros) == 1:
        rt = [0] * len(nums)
        rt[zeros[0]] = pnz
    else:
        rt = [1] * len(nums)
        for r in range(len(rt)):
            print(f"rt[{r}] = A[{r-1}] * B[{len(rt) - 1 - r - 1}]")
            rt[r] = A[r-1] * B[len(rt) - 1 - r - 1]

    return rt


nums = [1, 2, 3, 4]
nums = [-1, 1, 0, -3, 3]
nums = [0, 0]
productExceptSelf(nums)

# %%
