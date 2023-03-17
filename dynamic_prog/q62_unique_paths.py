"""https://leetcode.com/problems/unique-paths/
"""

# %%

from pprint import pprint

def uniquePaths(m: int, n: int) -> int:
    n_ways = [[0] * n for _ in range(m)]
    
    # When does the number of ways increase?

    for i in range(0, m):
        for j in range(0, n):
            if i == 0:
                n_ways[i][j] = 1
            elif j == 0:
                n_ways[i][j] = 1
            else:
                n_ways[i][j] = n_ways[i-1][j] + n_ways[i][j-1]
    
    print(n_ways)
    return n_ways[-1][-1]
    

uniquePaths(100, 100)

# %%
