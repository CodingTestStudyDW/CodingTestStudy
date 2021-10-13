##  https://programmers.co.kr/learn/courses/30/lessons/86051
def solution(numbers):
    answer = 0
    num = [1,2,3,4,5,6,7,8,9]
    for n in num:
        if n not in numbers:
            answer += n
        else:
            pass
    return answer
  
  ##########################
 
def solution(numbers):
    return 45 - sum(numbers)
