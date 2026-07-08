class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        heap = [(grid[0][0], 0,0)]
        visited = set()

        while heap:
            time, r, c = heapq.heappop(heap)

            if (r,c) in visited:
                continue
            
            visited.add((r,c))

            if r==ROWS-1 and c==COLS-1:
                return time
            

            for dr,dc in directions:
                nr,nc=r+dr, c+dc
                if (nr==ROWS or nc==COLS or nr<0 or nc<0 or (nr,nc) in visited):
                    continue
                heapq.heappush(heap, (max(time, grid[nr][nc]), nr, nc))
