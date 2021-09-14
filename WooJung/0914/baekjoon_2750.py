N = int(input())
numb = [int(input()) for i in range(N)]

numb.sort()
for n in numb:
    print(n)
 
## Bubble sort
for i in range(len(numb)):
  for j in range(len(numb)):
    if numb[i] < numb[j]:
      numb[i], numb[j] = numb[j], numb[i]
      
 
## Insert Sort
for i in range(1, len(numb)):
  while (i>0) & (numb[i] < numb[i-1]):
    numb[i], numb[i-1] = numb[i-1], numb[i]
    
    i -= 1
    
