class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat
        
        row, col = len(mat), len(mat[0])

        distMat = [[float('inf') for _ in range(col)] for _ in range(row)]
        
        queue = deque()

        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    distMat[r][c] = 0
                    queue.append((r, c))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0<=nx<row and 0<=ny<col:
                    if distMat[nx][ny] > distMat[x][y] + 1:
                        distMat[nx][ny] = distMat[x][y] + 1
                        queue.append((nx, ny))

        return distMat        