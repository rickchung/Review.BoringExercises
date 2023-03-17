"""https://leetcode.com/problems/number-of-islands/
"""

# %%

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        n_row, n_col = len(grid), len(grid[0])

        def _dfs(i, j):
            if 0 <= i < n_row and 0 <= j < n_col:
                if grid[i][j] == '1':
                    grid[i][j] = '#'
                    _dfs(i - 1, j)
                    _dfs(i + 1, j)
                    _dfs(i, j - 1)
                    _dfs(i, j + 1)

        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == '1':
                    count += 1
                    _dfs(i, j)
        
        return count


# Solution().numIslands([
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ])

Solution().numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
])
