"""https://leetcode.com/problems/climbing-stairs/
"""

def climbStairs(n: int) -> int:
    n_ways = [0, 1, 2]
    for i in range(3, n + 1):
        n_ways.append(n_ways[i - 1] + n_ways[i - 2])
    return n_ways[n]
