from collections import deque
N, K = map(int, input().split())

def bfs(N, K):
    queue = deque([N])
    visit[N] = 0
    map[N] = 0
    while queue:
        x = queue.popleft()
        if x == K:
            break
        for i in (x*2, x-1, x+1):
            if (0 <= i <= MAX) and visit[i] == -1:
                visit[i] = visit[x] + 1
                map[i] = x
                queue.append(i)                

def answer_(cnt, K):
    answer.append(K)
    for i in range(cnt):
        answer.append(map[K])
        K = map[K]
    return answer
            
MAX = 100000
visit = [-1] * (MAX+1)
map = [-1] * (MAX+1)
answer = []


bfs(N, K)
print(visit[K])

answer_(visit[K], K)
print(*answer[::-1])
