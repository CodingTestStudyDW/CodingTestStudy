dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dirL = [2, 3, 1, 0]
dirR = [3, 2, 0, 1]

T = int(input())
for _ in range(T):
    A = input()
    
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    x, y, d = 0, 0, 0		# 현재 위치/방향
    
    for cmd in A:
        if cmd == "L":		# 방향만 전환
            d = dirL[d]
            continue
        elif cmd == "R":
            d = dirR[d]
            continue
        elif cmd == "F":	# 현재 방향으로 한 칸 이동
            x += dx[d]
            y += dy[d]
        elif cmd == "B":
            x -= dx[d]
            y -= dy[d]
            
        # 최소 행/열, 최대 행/열 값 갱신
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    print(abs(max_y - min_y) * abs(max_x - min_x))
