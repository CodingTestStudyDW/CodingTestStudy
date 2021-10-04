from collections import deque
                
N, K = map(int,input().split())
MAX = 100000

queue = deque([N])
dist = [-1] * (MAX+1)
dist[N] = 0
cnt = 0
while queue:
    x = queue.popleft()
    if x == K: #동생이 있는 위치
        cnt += 1
    for i in (x*2, x+1, x-1): 
        if 0<=i<=MAX:
            if dist[i] == -1 or dist[i] >= dist[x] + 1: #방문한 적이 없거나 현재시간 +1인 경우
                dist[i] = dist[x] + 1
                queue.append(i)


print(dist[K])
print(cnt)
