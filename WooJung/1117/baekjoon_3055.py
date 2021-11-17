import sys
from _collections import deque
input = sys.stdin.readline
r,c = map(int, input().split())
maps = [list(input().strip()) for _ in range(r)]
visit=[[0]*c for _ in range(r)]
dx, dy=[1,0,-1,0], [0,-1,0,1]
queue=deque()

#물,고슴도치 위치 queue에 담기
#굴의 위치는 target에 저장
for i in range(r):
    for j in range(c):
        # 물있는 구역
        if maps[i][j]=='*':
            queue.append([i,j])
        # 고슴도치는 왼쪽에 담기
        elif maps[i][j]=='S':
            queue.appendleft([i,j])
        # 도착지점
        elif maps[i][j]=='D':
            target_r=i
            target_c=j

flag=False
#물과 고슴도치 위치에서 BFS
while queue:
    # 굴에 도착하고 나면 while문 탈출
    if flag:
        break
    x, y = queue.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx<0 or nx>=r or ny<0 or ny>=c:
            continue

        #물이 있는 곳인데
        if maps[x][y]=='*':       
            # 빈칸이거나 고슴도치가 있다면
            if maps[nx][ny]=='.' or maps[nx][ny]=='S':
                # 물 차오름
                maps[nx][ny]='*'
                queue.append([nx,ny])

        #고슴도치 이동할라고 하는데
        elif maps[x][y] == 'S':
            # 빈칸이면 이동
            if maps[nx][ny] == '.':
                maps[nx][ny] = 'S'
                visit[nx][ny] = visit[x][y] + 1
                queue.append([nx,ny])
            #굴에 도착하면 탈출
            elif maps[nx][ny] == 'D':
                flag=True
                visit[nx][ny]=visit[x][y]+1
                break

#굴에 도착하지 못하면 visit[굴]이 0이므로
if visit[target_r][target_c]==0:
    print('KAKTUS')
else: print(visit[target_r][target_c])
