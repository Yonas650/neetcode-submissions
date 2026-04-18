class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS=len(grid), len(grid[0])
        visit=set()

        neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=='1' and (r,c) not in visit:
                    count+=1
                    queue = deque()
                    queue.append((r,c))
                    visit.add((r,c))
                    while queue:
                            cr,cc=queue.popleft()
                            for dr,dc in neighbors:
                                if (min(cr+dr,cc+dc)<0 or cr+dr==ROWS or cc+dc==COLS or (cr+dr,cc+dc) in visit or grid[cr+dr][cc+dc]=='0'):
                                    continue
                                queue.append((cr+dr,cc+dc))
                                visit.add((cr+dr,cc+dc))
        return count
