## https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    # matrix 만들기
    matrix = [[row * columns + col + 1 for col in range(columns)] for row in range(rows)]
    answer = []
    # queries 확인
    for x1, y1, x2, y2 in queries:
        tmp = matrix[x1-1][y1-1]
        mini = tmp

        for k in range(x1-1, x2-1):
            test = matrix[k+1][y1 -1]
            matrix[k][y1-1] = test
            mini = min(mini, test)

        for k in range(y1 -1, y2 - 1):
            test = matrix[x2-1][k+1]
            matrix[x2-1][k] = test
            mini = min(mini, test)

        for k in range(x2-1, x1-1, -1):
            test = matrix[k-1][y2-1]
            matrix[k][y2-1] = test
            mini = min(mini, test)

        for k in range(y2-1, y1-1, -1):
            test = matrix[x1-1][k-1]
            matrix[x1-1][k] = test
            mini = min(mini, test)

        matrix[x1-1][y1] = tmp
        answer.append(mini)

    return answer
  
 
