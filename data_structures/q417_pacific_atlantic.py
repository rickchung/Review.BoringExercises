"""https://leetcode.com/problems/pacific-atlantic-water-flow/

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

        
"""

# %%

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nrows, ncols = len(heights), len(heights[0])

        flow_po = [[1 if  i - 1 < 0 or j - 1 < 0 else -1 for j in range(ncols)]
                   for i in range(nrows)]
        flow_ao = [[1 if i + 1 >= nrows or j + 1 >= ncols else -1 for j in range(ncols)]
                   for i in range(nrows)]

        def _fill_neighbors(i, j, flow_map):
            if flow_map[i][j] != 1:
                return
            neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            for ci, cj in neighbors:
                if 0 <= ci < nrows and 0 <= cj < ncols:
                    if heights[ci][cj] >= heights[i][j] and flow_map[ci][cj] == -1:
                        flow_map[ci][cj] = 1
                        _fill_neighbors(ci, cj, flow_map)

        for i in range(nrows):
            for j in range(ncols):
                _fill_neighbors(i, j, flow_po)
                _fill_neighbors(i, j, flow_ao)

        answers = []
        for i in range(nrows):
            for j in range(ncols):
                if flow_ao[i][j] == 1 and flow_po[i][j] == 1:
                    answers.append((i, j))

        return answers


Solution().pacificAtlantic([
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
])

# Solution().pacificAtlantic([[1]])
