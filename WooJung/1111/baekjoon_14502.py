from collections import deque
import copy
N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
queue = deque()
#bfs는 바이러스가 퍼지는 것을 확인하기 위하여 사용
#벽을 둘 수 있는 모든 경우의 수를 생각한다.
def bfs():
    global ans
    # 그냥 copy()는 배열의 내부 객체까지 깊은 복사를 해주지 않음
    #a = array.copy()
    a = copy.deepcopy(array)
    for i in range(N):
        for j in range(M):
            if a[i][j] == 2: #바이러스가 있다면
                queue.append([i, j])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if a[nx][ny] == 0: #빈방이라면
                    a[nx][ny] = 2 #바이러스로 채우기
                    queue.append([nx, ny])
    cnt = 0
    for i in a:
        cnt += i.count(0)
    ans = max(ans, cnt)

# 벽을 만드는 함수 만들기
def wall(x):
    if x ==3: #3개가 모두 채워지면 시작
        bfs()
        return
    # 벽 채워주기 0; 빈곳, 1; 벽
    for i in range(N):
        for j in range(M):
            if array[i][j] == 0: #빈곳이라면
                array[i][j] = 1 #벽으로 우선 채움
                wall(x+1) #하나 더해 3이 되면 return 해주고 0으로 다시 바꾸기 recursive
                array[i][j] = 0

ans = 0
wall(0)
print(ans)
