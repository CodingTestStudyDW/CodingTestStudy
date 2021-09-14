N= int(input())
num = N
cnt = 0
while True:
    a = num//10 # 6
    b = num % 10 # 8
    c = (a + b) % 10
    num =c + (b * 10)
    cnt += 1
    if (num == N):
        break

print(cnt)
