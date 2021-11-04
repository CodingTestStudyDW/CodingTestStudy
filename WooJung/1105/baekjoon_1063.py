# https://www.acmicpc.net/problem/1063
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]
move = ['R', 'L', 'B', 'T', 'RT', 'LT','RB','LB']

king, stone, N = map(str, input().split())

king_x, king_y = ord(king[0]) - ord('A'), int(king[1])-1
stone_x, stone_y = ord(stone[0]) - ord('A'), int(stone[1])-1

for _ in range(int(N)):
    d = move.index(input())
    nx, ny = king_x + dx[d], king_y + dy[d]
    
    if nx < 0 or ny < 0 or nx > 7 or ny>7:
        continue
    if nx == stone_x and ny == stone_y:
        stone_nx, stone_ny = stone_x + dx[d], stone_y + dy[d]
        if stone_nx < 0 or stone_ny < 0 or stone_nx > 7 or stone_ny >7:
            continue
        stone_x, stone_y = stone_nx, stone_ny
    king_x, king_y = nx, ny
print(chr(ord("A")+king_x)+str(king_y + 1))
print(chr(ord("A")+stone_x)+str(stone_y +1))
