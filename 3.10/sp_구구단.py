TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    c = set()       # 중복불가

    for a in range(1, 10):          # a는 1~9까지의 수
        for b in range(1, 10):      # b는 1~9까지의 수
            c.add(a*b)              # set에 추가

    if N in c:                      # c 안에 N이 있다면 출력
        print(f"#{tc} Yes")

    else:
        print(f"#{tc} No")