# 여러줄에 걸쳐서 n과 k가 주어진다
while True:
    try:
        cupon, k = map(int, input().split())
    except:
        # EoFError를 방지하기위해 try except문 추가
        break
    # 최초 치킨 n개 시켜서 도장 n개 받음
    chicken = 0
    chicken += cupon
    # 치킨 시킬수있을때
    while cupon // k:
        # 가능한 만큼 치킨 시키고
        chicken += cupon // k
        # 남은 쿠폰은 치킨 시킨거 + 쓰고 남은거
        cupon = (cupon // k) + cupon % k

    print(chicken)
    
# 계속 EoFError가 발생...
# 입력이 없는데 입력값을 받으려고해서 에러 발생
# while True가 문제인거같다