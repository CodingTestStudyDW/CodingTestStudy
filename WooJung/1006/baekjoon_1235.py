N = int(input())
numbers = [input() for _ in range(N)]
length = len(numbers[0])
for i in reversed(range(length)):
    num = [one[i:] for one in numbers]
    if len(num) == len(set(num)):
        print(length-i)
        break
    else:
        continue
