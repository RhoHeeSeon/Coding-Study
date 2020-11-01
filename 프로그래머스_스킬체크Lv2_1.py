## 결과 : 50.0 / 50.0

def solution(n, words):
    answer = []
    wordlist = [words[0]]

    id, turn = 2, 1 # 사람번호, 순서
    lastword = words[0] # 이전 단어
    for i in range(1, len(words)):
        lastword, newword = words[i-1], words[i]   #이전 단어, 현재 단어
        
        # 이미 사용한 단어인 경우
        if newword in wordlist:
            return [id, turn]            
        wordlist.append(newword)
        
        # 단어가 이어지지 않는 경우
        if newword[0] != lastword[-1]:
            return [id, turn]
        id += 1
        if id > n: 
            id = 1
            turn += 1
        

    return [0, 0]