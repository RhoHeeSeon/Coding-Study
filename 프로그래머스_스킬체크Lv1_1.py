
def solution(a, b):
    answer = 0
    big = max(a,b)
    small = min(a,b)
    
    for i in range(small,big+1):
        answer += i
        
    return answer