# N을 밟음(마지막)
## N-1 밟으면
# 그 이전의 계단(N-2)은 밝지않고 N-3을 밟아야됨
## N-1 안밟으면
# 그 이전 N-2을 밟고 N-3을 안밟던가
# dp(N) = max((arr[N] + arr[N-1] + dp[N-3]), (arr[N]+dp[N-2]))
N = int(input())
arr = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N+1)

if N ==1:
    print(arr[1])

elif N ==2:
    print(arr[1] + arr[2])

else:
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]
    for i in range(3, N+1):
        dp[i] =  max((arr[i] + arr[i-1]  + dp[i-3]), (arr[i] + dp[i-2]))
    print(dp[N])
