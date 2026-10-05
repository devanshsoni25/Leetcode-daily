from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]

        for u,v in prerequisites:
            adjList[u].append(v)
            indegrees[v] += 1

        result=[]
        queue=deque()

        for i in range(numCourses):
            if indegrees[i]==0:
                queue.append(i)

        while len(queue) != 0:
            current_node = queue.popleft()
            result.append(current_node)

            for adjNode in adjList[current_node]:
                indegrees[adjNode] -= 1

                if indegrees[adjNode] ==0:
                    queue.append(adjNode)

        if len(result) == numCourses:
            return True

        return False

        