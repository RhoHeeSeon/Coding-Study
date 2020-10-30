import math

def solution(brown, yellow):
    answer = []
    all = brown + yellow
    for col in range(3, int(math.sqrt(all))+1):
        if all % col: continue
        row = all // col
        print('row=', row, '  col=', col)
        if (row-2) * (col-2) == yellow:
            return [row, col]
