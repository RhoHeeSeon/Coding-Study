import math

def solution(progresses, speeds):
    answer = []
    today = 0
    tomorrow = 0
    daysleft = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    print(daysleft)

    while tomorrow!=len(progresses):
        today = tomorrow
        tomorrow += 1
        count = 1
        for i in range(today+1, len(progresses)):
            if daysleft[today] >= daysleft[i]:
                count += 1
                tomorrow += 1
            else:
                break
        answer.append(count)

    return answer