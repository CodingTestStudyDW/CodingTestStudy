## https://programmers.co.kr/learn/courses/30/lessons/17677

# 비교하고 삭제하지 않아서 오류

def solution(str1, str2):
    # 하나씩 쪼개기
    list1 = [str for str in str1.lower()]
    list2 = [str for str in str2.lower()]

    # 둘씩 묶기
    A = [list1[i] + list1[i+1] for i in range(len(list1) - 1)]
    B = [list2[i] + list2[i+1] for i in range(len(list2) - 1)]

    # aplha
    a = [string for string in A if string.isalpha() == True]
    b = [string for string in B if string.isalpha() == True]

    cnt = 0
    for string in a:
        if string in b:
            cnt+= 1
            b[b.index(string)] = 0


    if (len(a) + len(b) - cnt) == 0:
        answer = 65536
    else:
        answer = int(float(cnt/(len(a) + len(b) - cnt))*65536)

    return answer
  
### 1
########
# set의 &(and) 와 |(or) 사용해서 만듦
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)
