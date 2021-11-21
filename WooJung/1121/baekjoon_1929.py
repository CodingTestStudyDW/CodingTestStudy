# 에라토스테네스의 체
N, M = map(int, input().split())
a = [False,False] + [True]*(M-1)
primes=[]

for i in range(2,M+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, M+1, i):
        a[j] = False
for i in primes:
    if i >= N:
        print(i)
