class Solution:
    def count_islands(self, map_grid):
        if not map_grid or not map_grid[0]:
            return 0

        rows, cols = len(map_grid), len(map_grid[0])
        island_count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or map_grid[r][c] == 'W':
                return
            map_grid[r][c] = 'W'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(rows):
            for j in range(cols):
                if map_grid[i][j] == 'L':
                    island_count += 1
                    dfs(i, j)

        return island_count
