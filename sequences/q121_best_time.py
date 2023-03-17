"""https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
# %%
from typing import List

def max_profit(prices: List[int]) -> int:
    pmin = prices[0]
    dmax = 0

    for i in range(1, len(prices)):
        diff = prices[i] - pmin
        print(prices[i], diff, pmin, dmax)
        if diff > dmax:
            dmax = diff
        if prices[i] < pmin:
            pmin = prices[i]
    
    return dmax

# max_profit([7, 1, 5, 3, 6, 4])
# max_profit([7, 6, 4, 3, 1])
max_profit([7, 6, 4, 3, 100, 10, 1000, 8])
