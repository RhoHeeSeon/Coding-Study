
tc = int(input())
for i in range(tc):
    text = input() #문장 입력받기
    cnt = text.count(' ')+1 #문자개수 = 공백 개수+1
    for j in range(cnt):
        print(text.split(' ')[j][::-1] + ' ', end='')
    print()
