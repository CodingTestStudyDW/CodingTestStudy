# 통화 횟수
call_count = int(input())
# 통화별 통화 시간
call_time = list(map(int, input().split()))
# 영식, 민식 최종 요금
y_call = 0
m_call = 0

# 시간별 요금 정산
for call in call_time:
    # // 연산자를 통해 정수 부분만 가져옴
    # 입력 조건에 '자연수'라는 조건이 있어서 0이나 음수가 나올경우는 배제
    y_call += call // 30 * 10 + 10
    m_call += call // 60 * 15 + 15
    
# y_call, m_call 중에 싼거 출력 가격 같으면 Y M 후 가격 표시
if y_call == m_call:
    print("Y M {0}".format(y_call))
elif y_call < m_call:
    print("Y {0}".format(y_call))
else:
    print("M {0}".format(m_call))