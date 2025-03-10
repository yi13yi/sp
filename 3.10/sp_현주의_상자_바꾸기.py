T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0] * N

    for i in range(1, Q+1):
        L, R = map(int, input().split())    # L: 자리 시작, R: 자리 끝

        for j in range(L-1, R):     # 코드에서 자리수를 사용해야할때는
            box[j] = i              # 몇번 받을지 결정하는 변수에
                                    # _ 아닌 실제 변수를 넣어 밑에서 사용
    print(f"#{tc}", *box)