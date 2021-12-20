from collections import deque
dx, dy = [0,0,1,-1],[1, -1, 0, 0]
t = int(input())

def bfs(a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

for i in range(t):
    n, m, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    cnt = 0
    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(a, b)
                cnt += 1
    print(cnt)
