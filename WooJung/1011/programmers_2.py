## https://programmers.co.kr/learn/courses/30/lessons/60057
## 문자열 압축

def solution(s):
    result = []
    if len(s) == 1:
        return 1
    for i in range(1, (len(s)//2)+1):
        new = ''
        cnt = 1
        tmp = s[:i]
        for j in range(i, len(s), i):
            if tmp == s[j:i+j]:
                cnt+= 1
            else:
                if cnt!= 1:
                    new = new+str(cnt)+tmp
                else:
                    new = new+tmp
                tmp = s[j:j+i]
                cnt = 1
        print("i: {}, new: {}".format(i, new))
        if cnt!=1:
            new = new+str(cnt) + tmp
        else:
            new = new+tmp
        result.append(len(new))
        print(result)
    return min(result)
  
 #############################
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))
