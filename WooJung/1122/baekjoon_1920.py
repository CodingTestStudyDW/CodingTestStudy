N = int(input())
array_n = list(map(int, input().split()))
array_n.sort()
M = int(input())
array_m = list(map(int, input().split()))


for n in array_m:
    if n in array_n:
        print(1)
    else:
        print(0)
        
# 시간: 3684ms

def binary(target):
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if n_list[mid] == target:
            return True

        if target < n_list[mid]:
            right = mid-1
        elif target > n_list[mid]:
            left = mid + 1


for i in range(M):
    if binary(array_m[i]):
        print(1)
    else:
        print(0)
# 시간: 272ms
