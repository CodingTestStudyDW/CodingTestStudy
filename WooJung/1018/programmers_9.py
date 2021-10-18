# 깊이/너비 우선 탐색(DFS/BFS)
# 타겟 넘버

# BFS
from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque([(0,0)]) # sum, level
    while queue:
        s,l = queue.popleft()
        if l > len(numbers):
            break
        elif l == len(numbers) and s == target:
            answer += 1
        queue.append((s+numbers[l-1], l+1))
        queue.append((s-numbers[l-1], l+1))
    return answer
  
  
  
  
#### 
## Recursive..
# 깊이 우선 탐색을 recursive
def solution(numbers, target):
  if not numbers and target == 0 :
      return 
  elif not numbers:
    return 0
  else:
    return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
      
      
## 파이써닉
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
  
# product
# 데카르트 곱
# 두 개 이상의 리스트의 모든 조합을 구할때
