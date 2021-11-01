#https://www.acmicpc.net/problem/13417
#실버 3

N = int(input())
for _ in range(N):
    num = int(input())
    A = list(map(str, input().split()))
    
    ans = [A[0]]
    for i in range(1, len(A)):
        left = ans[0]
        if A[i] <= left:
            ans.insert(0, A[i])
        else:
            ans.append(A[i])
    print(''.join(ans))
