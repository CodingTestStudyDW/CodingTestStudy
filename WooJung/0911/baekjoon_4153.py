while True:
    a = list(map(int, input().split()))
    a.sort()
    # 000 출력하면 멈추기(while 활용)
    if sum(a) == 0:
        break
    # 직각삼각형 계산하기
    if a[0]**2 + a[1]**2 == a[2]**2: 
        print("right")
    else:
        print("wrong")
