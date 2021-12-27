N = int(input())

for _ in range(N):
    T = input()
    str = []

    for VPS in T:
        if VPS == "(":
            str.append(VPS)
        elif VPS == ")":
            if len(str) != 0 and str[-1] == "(":
                str.pop()
            else:
                str.append(")")
                break

    if len(str) == 0:
        print("YES")
    else:
        print("NO")
