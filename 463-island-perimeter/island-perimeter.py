from collections import deque
class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        queue=deque()
        count=0
        visited=[[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    queue.append((r,c))
                    visited[r][c]=1
                    break

            if queue:
                break

        directions=[(0,1),(0,-1),(1,0),(-1,0)]

        while queue:
            r,c=queue.popleft()
            for dr,dc in directions:
                new_r=r+dr
                new_c=c+dc

                if new_r<0 or new_r>=rows or new_c<0 or new_c>=cols:
                    count+=1

                elif grid[new_r][new_c]==0:
                    count+=1

                elif visited[new_r][new_c]==0:
                    visited[new_r][new_c]=1
                    queue.append((new_r,new_c))

        return count        