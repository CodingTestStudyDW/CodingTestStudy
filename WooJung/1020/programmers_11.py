# 약수의 개수와 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/77884

def count(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i ==0:
            cnt += 1
    return cnt

def solution(left, right):
    number = left
    answer = 0
    while number <= right:
        if count(number) % 2 == 0:
            answer+= number
        else:
            answer-= number
        number +=1
        
    return answer
