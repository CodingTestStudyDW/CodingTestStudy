N = int(input())
#dp[[자리수][앞에 오는 숫자]]
dp = [[0 for i in range(10)] for j in range(N+1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[N]) % 1000000000)

'''
앞에 오는 숫자 = 0
-> 0 다음은 1

앞에 오는 숫자 = 1~8
>dp[n][i] = dp[n][i-1] + dp
-> 앞 뒤 다

앞에 오는 숫자 = 9
dp[자리수][9] = dp[자리수-1][8]
-> 9다음은 8
'''
