# https://www.acmicpc.net/problem/1065
## 실버 4 - 브루트포스 알고리즘

N = int(input())
result = 0

for n in range(1, N +1) :
    if n <= 99 :
        result += 1 
    
    else :     
        nums = list(map(int, str(n))) 
        if nums[0] - nums[1] == nums[1] - nums[2] : 
            result+=1
print(result)
