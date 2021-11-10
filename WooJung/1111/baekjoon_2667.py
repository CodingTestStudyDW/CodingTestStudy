from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    count = 0
    while queue:
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and visit[nx][ny] == 0: #한번도 방문하지않음
                if array[nx][ny] == 1: #집이 있는 곳
                    visit[nx][ny] = 1 #방문 표시
                    array[nx][ny] = 2 #집이 아니라 표시
                    count += 1
                    queue.append((nx, ny))
    answer.append(count)

N = int(input())
array = [list(map(int, input())) for _ in range(N)]
answer = []
dx, dy = [-1,1, 0,0], [0, 0, -1, 1]
visit = [[0] *N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if array[i][j] == 1:
            bfs(i, j)
            cnt += 1
print(cnt)
for ans in answer:
    print(ans)
