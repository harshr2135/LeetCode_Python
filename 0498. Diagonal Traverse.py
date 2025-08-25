class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        res = []
        row, col = 0,0

        for i in range(m*n):
            res.append(mat[row][col])

            if (row+col)%2==0:
                if col == n-1:
                    row += 1
                elif row == 0:
                    col += 1
                else:
                    row -= 1
                    col += 1

            else:
                if row == m-1:
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    row += 1
                    col -= 1

        return res