class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res = []

        for rowIter, row in enumerate(grid):
            res.extend(row if rowIter % 2 == 0 else row[::-1])

        return res[::2]