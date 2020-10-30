
def solution(number, k):
    answer = ''
    number = list(number)
    stack = []

    for n in number:
        while stack and stack[-1] < n and k:
            stack.pop()
            k -= 1
        stack.append(n)

    if k:
        stack = stack[:-k]
        
    return ''.join(stack)
