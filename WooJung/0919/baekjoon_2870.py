import re

N = int(input())
number = []

for i in range(N):
    string = input()
    num = [int(s) for s in re.findall("\d+", string)] #여러자리 숫자 단위
    for j in num:
        number.append(j)
for i in sorted(number, reverse = False):
    print(i)
