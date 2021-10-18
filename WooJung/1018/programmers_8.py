## Heap(힙)사용
## 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626

def solution(scoville, K):
    scoville.sort()
    cnt = 0
    while scoville[0] < K:
        scoville[1] = scoville[0] + (scoville[1] * 2)
        del scoville[0]
        cnt += 1
        scoville.sort()
        
        if len(scoville) == 1:
            return -1
        
    return cnt
solution([1,2,3], 11)

## 맨날 sort을 하면 안됨
## heap사용해야됨

import heapq
def solution(scoville, K):
    scoville.sort()
    cnt = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+2*b)
        cnt += 1
    return cnt
        #scoville.sort()
    
    
    
    ### 힙의 경우
    # 데이터를 정렬된 상태로 저장하기 위해서 사용하는 파이썬 heapq(힙큐) 내장 모듈
    # heapq모듈은 이진트리기반의 최소 힙 자료구조를 제공
    # 최대, 최소값을 가져올 때 많이 사용
    
    haep = [] #힙생성
    heapq.heappush(heap, 4)  #원소 추가
    heapq.heappop(heap) # 가장 작은 원소 삭제 후 그 값 리턴
    heap[0] #삭제하지 않고 가져오기
    heap.heapify(heap) #기존 리스트를 힙으로 변환
