def solution(citations):

    h=len(citations)
    while h:
        higher = 0
        lower = 0
        for c in citations:
            if c>=h: higher += 1
            else: lower += 1
        if higher>=h:
            return h
        h-=1
    
    return h