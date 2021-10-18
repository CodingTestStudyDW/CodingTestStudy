# 124나라

def solution(n):
    answer = ''
    while n:
        # 나누어 떨어지면 하나 빼주고 4 대입
        if n%3 == 0:
            n = n-1
            answer += str('4')
        # 나눠줄땐 똑같이
        else:
            answer += str(n%3)
       n = n//3
     answer.replace('3', '4')
    # Reversed 해주기 위한 코드
    return (''.join(reversed(answer)))
  
  
  
  
