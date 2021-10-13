## 기능개발

import math
def solution(progresses, speeds):
    answer = []
    num = 1
    # 걸리는 시간 계산
    time = math.ceil((100-progresses[0])/speeds[0])
    for i in range(1, len(progresses)):
        if time >= math.ceil((100-progresses[i])/speeds[i]): #계산했을때 적다면, num + 1
            num += 1
        else:
            # 작지않으면 1을 안더해줌
            answer.append(num)
            num = 1
            time = math.ceil((100-progresses[i])/speeds[i])
    answer.append(num)
    return answer
#################
# 큐활용
# ceil을 안스고 p-100으로 작성
def solution(progresses, speeds):
    Q=[]
    ## zip 사용해서 두개 다 한꺼번에 사용할 수 있도록 함
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    ## list Q에는 [필요한 일수, 기능수 = 1]의 형태로 추가
    return [q[1] for q in Q]
