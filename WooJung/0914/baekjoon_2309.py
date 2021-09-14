# 아홉명의 키 - (두명의 키) = 100
## 완전 탐색
a = [int(input()) for i in range(9)]
total = sum(a)

for i in range(9):
    for j in range(i+1, 9):
        if (total -a[i] - a[j])==100:
            num1 = a[i]
            num2 = a[j]
a.remove(num1)
a.remove(num2)
for i in sorted(a):
    print(i)
