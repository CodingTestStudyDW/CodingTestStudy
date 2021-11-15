# https://www.acmicpc.net/problem/1051
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

check = min(N, M)
answer = 0
for i in range(N):
    for j in range(M):
        for k in range(check):
            if ((i + k) < N) and ((j + k) < M) and (arr[i][j] == arr[i][j + k] == arr[i + k][j] == arr[i + k][j + k]):
                answer = max(answer, (k + 1)**2)
                
print(answer)
