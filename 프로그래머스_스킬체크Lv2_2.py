## 결과 : 50.0 / 50.0

def Check(s, skill, check):
    
    if s in skill:
        check[skill.index(s)] = 1
    print(check)
    for i in range(len(check)-1):
        if check[i] < check[i+1]:
            return False
    return True


def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees:
        print(st)
        check = [0 for i in range(len(skill))]
        cnt = 0
        for s in st:
            if Check(s, skill, check) : cnt += 1
            else : break
        #print(cnt, len(st))
        if cnt == len(st):
            answer += 1

    print(answer)
    return answer

solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])  #2