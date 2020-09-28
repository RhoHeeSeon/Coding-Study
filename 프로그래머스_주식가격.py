
def solution(prices):
    answer = []
    
    for i in range(len(prices)-1): # i=0~마지막-1
        cnt = 1
        for j in range(i+1, len(prices)-1): #j=i+1~마지막
            if prices[i] <= prices[j]: cnt += 1
            else : break
        answer.append(cnt)
        print(i, answer)

    answer.append(0)
    return answer

solution([1,2,3,2,3])