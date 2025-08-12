class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        beg = 0
        end = row*col
        while beg<end:
            mid = (beg+end)//2
            i = mid//col
            j = mid%col

            if matrix[i][j] == target:
                return True
            if matrix[i][j] <target:
                beg = mid+1
            else:
                end = mid

        return False