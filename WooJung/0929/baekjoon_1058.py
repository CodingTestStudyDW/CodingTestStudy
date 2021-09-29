# 경우의 수
N = int(input())
# 친구인지 아닌지에 대한 입력 값
friend = [list(input()) for _ in range(N)]

# 2-친구인 경우도 포함시키기 위한 graph
block = [[0 for _ in range(N)] for _ in range(N)]

## 플로이드-워셜 문제
for i in range(N):
    for j in range(N):
        for k in range(N):
            if j==k: #동일인물일때는 세지 않는다
                continue
            # 직접적인 친구이거나, 아는 사람이 친구일 경우 1로 표기
            if friend[j][k] == 'Y' or (friend[j][i] == 'Y' and friend[i][k] == 'Y'):
                block[j][k] = 1
# 가장 많은 수의 친구인 것을 구하기
result = 0
for i in block:
    result = max(result, sum(i))
print(result)
