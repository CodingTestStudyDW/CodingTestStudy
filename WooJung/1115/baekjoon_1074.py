N, r, c = map(int, input().split())
cnt = 0

while N > 1:
    size = (2 ** N) // 2
    if r < size and c < size: # 2사분면
        pass
    elif r < size and c >= size: # 1사분면
        cnt += size ** 2
        c -= size
    elif r >= size and c < size: # 3사분면
        cnt += size ** 2 * 2
        r -= size
    elif r >= size and c >= size: # 4사분면
        cnt += size ** 2 * 3
        r -= size
        c -= size
    N -= 1

if r == 0 and c == 0:
    print(cnt)
if r == 0 and c == 1:
    print(cnt + 1)
if r == 1 and c == 0:
    print(cnt + 2)
if r == 1 and c == 1:
    print(cnt + 3)

    #######################
    
 



def solve(n,r,c):
    global result
    if r==R and c == C:
        print(int(result))
        exit(0)
    # 탐색중인 사각형의 좌표안에 찾는 좌표가 없으면
    # 사각형의 크기만큼 숫자를 더함
    if not (r<=R<r+n and c <= C <c+n):
        result += n*n
        return
    
    solve(n/2, r, c)
    solve(n/2, r, c+ n/2)
    solve(n/2, r+ n/2, c)
    solve(n/2, r+n/2, c+n/2)

    
    
result = 0
N, R, C = map(int(input().split())
solve(2**N, 0, 0)
