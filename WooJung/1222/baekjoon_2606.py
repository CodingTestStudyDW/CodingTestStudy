N = int(input())
M = int(input())

cnt = 0
visit = [0]*(N+1)

graph = [[] * N for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    global cnt
    visit[v] = 1
    for i in graph[v]:
        if visit[i] == 0: 
            bfs(i)
            cnt+=1
bfs(1)
print(cnt)
