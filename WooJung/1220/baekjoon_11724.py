from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
 
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
    
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

cnt = 0
for i in range(1, N+1):
    if not visited[i]: # False면
        bfs(graph, i, visited)
        cnt += 1
print(cnt)
        
