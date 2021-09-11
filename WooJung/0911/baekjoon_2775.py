## https://www.acmicpc.net/problem/2775

# 재귀활용
def person(k,n):
    if k==0:
        return n
    s=0
    for i in range(1, n+1):
        s += person(k-1, i)
    return s

for i in range(int(input())):
    k=int(input()) #층
    n=int(input()) #호
    print(person(k, n))
    
# 반복문 사용
for _ in range(int(input)):
    k = int(input()) #층
    n = int(input()) #호
    people = [i for i in range(1, n+1)] #0층 사람
    for x in range(k):
        for y in range(1, n):
            people[y] += people[y-1]
    print(people[-1])

# 백준의 경우 큰 숫자를 사용하기 때문에 재귀함수를 사용할 경우 시간초과가 남
# 가끔 pypy3로 재귀를 풀면 맞출 수 있음
# 근데 똑같은 코드여도 안될때가 있긴하더라
