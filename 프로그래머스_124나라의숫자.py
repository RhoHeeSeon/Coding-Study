
def calc(r, answer):
    if r==0 : answer = '1' + answer
    elif r==1 : answer = '2' + answer
    else : answer = '4' + answer
    print('answer: ' , answer)


def solution():
    n = int(input())
    answer = ''
    q, r = divmod(n-1, 3) #(n-1)/3의 몫, 나머지
    print('q, r = ', q, ' ', r)
    
    while q != 0 : #몫=0이면 종료
        print('q, r = ', q, ' ', r)
        calc(r, answer)
        q, r = divmod(q-1, 3)
    
    calc(r, answer)
    print('최종 answer: ' , answer)

    return answer

solution()