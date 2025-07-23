class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row Checker
        for i in range(9):
            row = [0] * 10
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    if row[num] == 1:
                        return False
                    row[num] = 1

        # Column Checker
        for i in range(9):
            col = [0] * 10
            for j in range(9):
                if board[j][i] != '.':
                    num = int(board[j][i])
                    if col[num] == 1:
                        return False
                    col[num] = 1

        # Subgrid Checker
        for block in range(9):
            subgrid = [0] * 10
            for i in range((block // 3) * 3, (block // 3) * 3 + 3):
                for j in range((block % 3) * 3, (block % 3) * 3 + 3):
                    if board[i][j] != '.':
                        num = int(board[i][j])
                        if subgrid[num] == 1:
                            return False
                        subgrid[num] = 1

        return True