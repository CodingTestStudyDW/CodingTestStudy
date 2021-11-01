#https://www.acmicpc.net/problem/11508
#실버 4

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse = True)
total = 0
for i in range(N):
    if (i%3!=2):
        total += arr[i]
print(total)
