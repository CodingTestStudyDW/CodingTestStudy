#다이나믹 프로그래밍, 앞의 정답값으로 이후 정답값 내기
N = int(input())
answer =[0,1,2]
for i in range(3, 1001):
    answer.append(answer[i-2] + answer[i-1])

print(answer[N] % 10007)
