#https://programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    size_x = 0
    size_y = 0
    for x, y in sizes:
        size_x = max(min(x, y), size_x)
        size_y = max(max(x, y), size_y)
    return size_x * size_y
  
  
### 1
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
 
###2
solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)
