string = input()
alpha = list(range(97,123))  # 아스키코드 숫자 범위

for x in alpha :
    print(string.find(chr(x))) 
