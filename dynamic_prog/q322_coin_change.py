"""https://leetcode.com/problems/coin-change/
"""
# %%
from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    max_amount = 10**4
    # Init a lookup table
    # The upperbound of amount is 10^4, +2 to include 0 and an index offset
    lookup = [-1] * (max_amount + 2)
    # Available coins can reach the amount by 1 coin
    for i in coins:
        if i < len(lookup):
            lookup[i] = 1
    # The amount 0 needs 0 coin to reach
    lookup[0] = 0

    # Lookup function f(amount, coin) that returns 
    # None (if amount - coin is out of bound), or
    # lookup[amount - coin]
    f = lambda a, c: lookup[a - c] if 0 <= a - c < len(lookup) else None

    # Build the lookup table until the target amount
    for i in range(1, amount + 1):
        if lookup[i] != -1:
            continue
        options = []
        for j in coins:
            o = f(i, j)
            if o is not None and o > 0:
                options.append(o)
        if options:
            best = min(options)
            lookup[i] = 1 + best
    
    return lookup[amount]

# %%
coinChange([1,2,5], 100)


