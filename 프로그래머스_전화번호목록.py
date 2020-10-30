
def solution(phone_book):
    answer = True

    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            I, J = str(phone_book[i]), str(phone_book[j])
            lenI, lenJ = len(I), len(J)
            if lenI > lenJ:
                if I[:lenJ] == J : return False
            else:
                if I == J[:lenI] : return False
            
    return answer