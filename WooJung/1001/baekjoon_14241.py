N= int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)

result = 0
for i in range(N-1): 
    score = a[i] * a[i+1] 
    a[i+1] = a[i] + a[i+1] 
    result = result+score
    
print(result)
