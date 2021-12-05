#처음 시작하고 0 부터
#빠르게 끝나는 순서대로 회의배정

N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]
time = sorted(time, key = lambda a: a[0]) #시작시간 기준
time = sorted(time, key = lambda a: a[1]) #끝시간 기준

end = 0
cnt = 0
for i, j in time:
    if i >= end:
        cnt += 1
        end = j
print(cnt)
