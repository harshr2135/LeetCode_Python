class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        freshOrange = 0

        queue = deque()

        time = 0

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    freshOrange += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        while queue and freshOrange>0:
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1:
                        grid[nx][ny] = 2

                        queue.append((nx, ny))
                        freshOrange -= 1

            time += 1


        return time if freshOrange == 0 else -1