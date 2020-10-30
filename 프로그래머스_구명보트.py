

def solution(people, limit):
    answer = len(people)
    HeavyIndex = 0
    LightIndex = len(people) - 1

    people.sort(reverse = True)
    while HeavyIndex <= LightIndex:
        if HeavyIndex == LightIndex:
            return answer
        if people[HeavyIndex] + people[LightIndex] <= limit:
            LightIndex -= 1
            answer -= 1
        HeavyIndex += 1
        #print(answer)
    return answer
