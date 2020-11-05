
def solution(s):
    # wordlen=len(s)이면 압축문자열 길이 = len(s)
    answer = len(s)
    
    for wordlen in range(1, len(s)-1):  #문자길이가 1~len(s)-1까지 반복.
        wordcnt = len(s)//wordlen   #문자뭉텅이 개수 = 전체문자열길이에서 문자길이 나눈 몫
        comp = False    #False=압축x, True=압축o
        compcnt = 0     #압축되는 문자뭉텅이 개수
        compstr = ''    #압축된 문자열

        #j번째 문자뭉텅이 처리
        for j in range(wordcnt):
            word1 = s[j*wordlen: (j+1)*wordlen]
            word2 = s[(j+1)*wordlen: (j+2)*wordlen]
            if j==wordcnt-1: word2 = s[(j+1)*wordlen:] #마지만 뭉텅이 예외처리
            if word1 == word2:  #앞 문자와 뒤 문자가 같으면
                if not comp: comp, compcnt = True, 1    #압축x였던 경우: 압축설정
                compcnt += 1    #압축되는 문자개수 +1
            else:
                if comp: 
                    compstr += str(compcnt)    #압축o인 경우: 앞에 압축되는 문자 개수 써주기
                    comp, compcnt = False, 0    #압축설정 해제
                compstr += word1    #문자열 더함

        ##마지막 문자 뭉텅이 처리
        if comp: compstr += str(compcnt)    #압축o인 경우: 앞에 압축되는 문자 개수 써주기
        compstr += word2    #문자열 더함

        ##문자열 길이 중 최소인 것 answer에 담기
        if answer > len(compstr):
            answer = len(compstr)
        

    return answer


#solution("aabbaccc")	#7
#solution("ababcdcdababcdcd")	#9
#solution("abcabcdede")	#8
#solution("abcabcabcabcdededededede")	#14
#solution("xababcdcdababcdcd")	#17