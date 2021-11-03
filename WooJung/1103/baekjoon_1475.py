# https://www.acmicpc.net/problem/1475
# 실버 5 - 구현


s = input()

card = [0] * 10
for i in str(s):
    if i == '6' or i == '9':
        if card[6] == card[9]:
            card[6] += 1
        else:
            card[9] += 1
    else:
        card[int(i)] += 1

print(max(card)) 
