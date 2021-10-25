# https://programmers.co.kr/learn/courses/30/lessons/72411
import itertools

def solution(orders, course):
    answer = []
    for p in course: # course
        list_ = []
        for order in orders: 
            # combination을 위한 pool에 나열
            pool = [str(j) for j in order]
            # combination 만들기
            list_.extend(list(map(''.join, itertools.combinations(pool, p))))
        count = {}
        for i in list_:
            string = ''.join(sorted(i))
            try: count[string] += 1
            except: count[string] = 1
        inverse = [[value, key] for key, value in count.items()]
        res_list = [user[1] for user in inverse if user[0] == max(inverse)[0] and max(inverse)[0] > 1]
        answer.extend(res_list)

    return sorted(answer)
  
  
  ### 1
# Counter 사용

import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]
  
  
