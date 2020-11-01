cntlist = [1000000000]    #이름을 완성했을 때 횟수를 저장하는 배열

## 'A'부터 올려가며/내려가며 문자로의 조작횟수 비교, 작은 것 선택
def count(name, idx):
    return min(ord(name[idx])-ord('A'), ord('Z')-ord(name[idx])+1)

## 조이스틱
def Joystick(name, naming, idx, cnt, rlcnt, rl):
    if rlcnt == len(name): return    # 좌우 조작횟수가 이름의 길이가 되면 불필요한 좌우이동 -> 리턴
    if cnt >= min(cntlist): return    # 현재 cnt보다 적은 횟수로 이름을 완성할 수 있다면 이후 계산이 불필요 -> 리턴
    if name[idx]!=naming[idx]: 
        cnt += count(name, idx)    # 문자변경 조작횟수 count
        naming = naming[:idx] + name[idx] + naming[idx+1:]    # idx의 문자만 고침
    print('naming= ', naming, '\tcnt= ', cnt, '\t',rl)    # for debug

   
    if naming == name:    # naming과 name이 같다면(이름 완성)
        cntlist.append(cnt)    # 현재 조작횟수 저장
        return
    ## 오른쪽으로 이동
    if idx+1 == len(name):    # 인덱스 바깥 처리
       Joystick(name, naming, 0, cnt+1, rlcnt+1, rl+'오')
    elif idx+1 < len(name):
       Joystick(name, naming, idx+1, cnt+1, rlcnt+1, rl+'오')

     ## 왼쪽으로 이동
    if idx-1 < 0:    # 인덱스 바깥 처리
       Joystick(name, naming, len(name)-1, cnt+1, rlcnt+1, rl+'왼')
    elif idx-1 >= 0 :
       Joystick(name, naming, idx-1, cnt+1, rlcnt+1, rl+'왼')
    return

 
def solution(name):

    answer = 0
    idx = 1

    # name의 길이만큼 'A'인 문자열을 가지고 조이스틱 조작 시작
    Joystick(name, 'A' * len(name), 0, 0, 0, '')

    return min(cntlist)