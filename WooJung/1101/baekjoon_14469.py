# https://www.acmicpc.net/problem/14469
# 실버 5

N = int(input())
arr = sorted([[*map(int, input().split())] for _ in range(N)])

time = 0
for i in range(N):
    x, y = arr[i]
    if time < x:
        time = x
    time += y
print(time)
