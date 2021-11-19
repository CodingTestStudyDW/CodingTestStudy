R,C = map(int, input().split())
board = [list(map(lambda x: ord(x) - 65, input())) for _ in range(R)]
check = [0] * 26 #알파벳 갯수

dx, dy = [-1, 1, 0, 0], [0, 0, -1,1]
def dfs(x, y, z):
    global answer
    answer = max(answer, z)
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<R and 0<=ny<C and check[board[nx][ny]] == 0:
            check[board[nx][ny]] = 1
            dfs(nx, ny, z+1)
            check[board[nx][ny]] = 0
answer = 1
check[board[0][0]] = 1
dfs(0, 0, answer)
print(answer)
