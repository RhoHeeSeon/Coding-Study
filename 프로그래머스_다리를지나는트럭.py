def solution(bridge_length, weight, truck_weights):
    answer = 0
    start = 0 # 다음에 건널 트럭 번호
    finish = 0 # 다음에 다 건널 트럭 번호
    on_bridge = 0 # 다리 위 트럭 무게
    time = [] # 트럭이 다리 건너기 시작한 시각
    time_now = 0 # 현재 시각

    # 1초 후
    time_now += 1
    on_bridge = truck_weights[start]
    start += 1
    time.append(time_now)

    # 반복
    while finish != len(truck_weights):
        # 시간 경과
        time_now += 1
        # 다 건넌 트럭 OUT
        if time_now - time[finish] == bridge_length:
            on_bridge -= truck_weights[finish]
            finish += 1
        # 새로 건널 트럭 IN
        if (start < len(truck_weights)) and (on_bridge + truck_weights[start] <= weight):
            on_bridge += truck_weights[start]
            start += 1
            time.append(time_now)
    answer = time_now
    #print(answer)

    return answer