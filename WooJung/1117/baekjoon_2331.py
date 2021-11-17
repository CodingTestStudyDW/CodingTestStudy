A, P = map(int, input().split())
d = []

while A not in d:
    d.append(A)
    A = sum([int(i)**P for i in str(A)])

print(d.index(A))
