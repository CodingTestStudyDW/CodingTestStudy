N= int(input())
num = [9, 8, 7, 6, 5, 4,3,2]
answer = []
for _ in range(N):
    a = int(input())
    if a == 1:
        answer.append(1)
        continue
    value = []
    for number in num:
        while True:
            if a % number == 0:
                a = a//number
                value.append(number)
            else:
                break
    if a == 1:
        answer.append(len(value))
    else:
        answer.append(-1)

for i in answer:
    print(i)
