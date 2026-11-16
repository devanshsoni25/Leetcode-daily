from collections import deque
class Solution:
    def containsCycle(self, grid: list[list[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0]*cols for _ in range(rows)]

        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if visited[i][j] == 1:
                    continue
                queue.append((i,j,-1,-1))
                visited[i][j] = 1

                while len(queue)!=0 :
                    i,j,parent_i,parent_j = queue.popleft()
                    letter = grid[i][j]

                    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                        new_i,new_j = i+dx,j+dy

                        if new_i<0 or new_j<0 or new_i>=rows or new_j>=cols:
                            continue

                        if grid[new_i][new_j]!=letter:
                            continue
                        
                        if visited[new_i][new_j] == 0:
                            visited[new_i][new_j] = 1
                            queue.append((new_i,new_j,i,j))

                        else:
                            if new_i==parent_i and new_j==parent_j:
                                continue

                            return True

        return False


