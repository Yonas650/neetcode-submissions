class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS=len(grid), len(grid[0])
        rotten=set()
        queue=deque()
        time=0


        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    rotten.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0

        
        neighbors=[[0,1],[0,-1],[1,0],[-1,0]]
        while queue:
            progressed = False
            for i in range(len(queue)):
                r,c=queue.popleft()
                for dr,dc in neighbors:
                    if (min(r+dr,c+dc)<0 or r+dr==ROWS or c+dc==COLS or (r+dr,c+dc) in rotten or grid[r+dr][c+dc]==0 or grid[r+dr][c+dc]==2):
                        continue
                    grid[r+dr][c+dc] = 2
                    fresh -= 1
                    queue.append((r+dr,c+dc))
                    rotten.add((r+dr,c+dc))
                    progressed = True
            if progressed:
                time+=1
        return -1 if fresh>0 else time