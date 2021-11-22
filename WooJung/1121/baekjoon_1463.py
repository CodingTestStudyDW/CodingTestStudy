N = int(input())

d = [0] * (N+1)
for i in range(2, N+1):
    # 1을 더함
    d[i]= d[i-1] + 1
    # 3으로 나눴을때 나누어지면 min 값 저장
    if i%3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    # 2로 나눴을때 나누어지면 min 값 저장
    if i%2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
print(d[N])
