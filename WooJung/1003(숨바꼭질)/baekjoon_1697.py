from collections import deque

def BFS():
    queue = deque([N])
    while queue:
        x = queue.popleft()
        if x == K: #동생이 있는 위치
            print(dist[x])
            break
        for i in (x+1, x-1, x*2):
            if 0<=i<=MAX and not dist[i]:
                dist[i] = dist[x] + 1
                queue.append(i)
                
N, K = map(int,input().split())
MAX = 100000
dist = [0] * (MAX+1)
BFS()


#####################################
# dist = 최단거리, visit = 방문 여부  #
#####################################

def bfs(n, k):
    queue = deque([n])
    visited[n] = True
    while queue:
        now = queue.popleft()
        for move in [now+1, now-1, now*2]:
            if 0<= move <= MAX and not visited[move]:
                visited[move] = True
                queue.append(move)
                dist[move] = dist[now]+1
    return dist[k]
