def search(priorities, next, cnt):
    index = next
    for i in range(cnt-1):
        index += 1
        if index == cnt: index = 0
        if priorities[next] < priorities[index]:
            next = index
    
    return next

def solution(priorities, location):
    answer = 0
    # 변수
    next = 0 # 다음에 프린트할 문서 index
    cnt = len(priorities) # 전체 문서 개수
    
    while True:
        # next 찾기
        next = search(priorities, next, cnt)
        
        # 프린트 하기
        answer += 1
        if next == location:
            #print("최종 = ", answer)
            return answer
        priorities[next] = 0

