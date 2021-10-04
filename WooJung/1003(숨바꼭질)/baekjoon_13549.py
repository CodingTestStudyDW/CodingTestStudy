from collections import deque

def bfs(N, K):
    queue = deque([N])
    visit[N] = 0
    while queue:
        x = queue.popleft()
        if x == K:
            break
        for i in (x*2, x-1, x+1):
            if (0 <= i <= MAX) and visit[i] == -1:
                visit[i] = visit[x] + (0 if i == x*2 else 1)
                queue.append(i)
            
N, K = map(int, input().split())
MAX = 100000
visit = [-1] * (MAX+1)
bfs(N, K)
print(visit[K])
