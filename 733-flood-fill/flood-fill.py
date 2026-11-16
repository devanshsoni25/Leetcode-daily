from collections import deque
from copy import deepcopy
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        rows = len(image)
        cols = len(image[0])

        grid_copy = deepcopy(image)
        initial_color = grid_copy[sr][sc]
        

        if initial_color == color:
            return grid_copy

        queue = deque()
        queue.append((sr,sc))
        grid_copy[sr][sc] = color

        while len(queue)!=0 :
            i,j = queue.popleft()

            

            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_i,new_j = i+dx,j+dy

                if new_i<0 or new_j<0 or new_i>=rows or new_j>=cols:
                    continue

                if grid_copy[new_i][new_j] != initial_color:
                    continue

                grid_copy[new_i][new_j] = color
                queue.append((new_i,new_j))

        return grid_copy

                