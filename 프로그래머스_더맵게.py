import heapq 

def solution(scoville, K): 
    answer = 0 
    heapq.heapify(scoville) # scoville을 min heap으로 만들기
    
    while True: 
        first = heapq.heappop(scoville) # 가장 작은 원소 pop
        if first >= K: # 가장 작은 원소의 스코빌지수 >= K이면 문제 종료
            #print("answer= ", answer) 
            return answer 
        if not scoville: # scoville이 비었으면 더 이상 못 함
            return -1  # -1 리턴
        second = heapq.heappop(scoville) # 두번째로 작은 원소 pop

        new = first + 2*second # 섞은 음식 스코빌 = 가장 작은 스코빌 + 2* 두번째로 작은 스코빌
        heapq.heappush(scoville, new) # 섞은 음식 스코빌지수 넣기
        answer += 1 # 섞은 횟수 count
        #print(first, ' + ', second, ' => ', new) 
         
    return answer 
