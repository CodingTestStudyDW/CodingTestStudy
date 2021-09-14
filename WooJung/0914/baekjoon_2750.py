N = int(input())
numb = [int(input()) for i in range(N)]

numb.sort()
for n in numb:
    print(n)
 
## Bubble sort
for i in range(len(numb)):
  for j in range(len(numb)):
    if numb[i] < numb[j]:
      numb[i], num[j] = num[j], num[i]
      
 
## Insert Sort
for i in range(1, len(numb)):
  while (i>0) & (num[i] < num[i-1]):
    num[i], num[i-1] = num[i-1], num[i]
    
    i -= 1
    
