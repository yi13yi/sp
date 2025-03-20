T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(input())
    total_cnt = 0   # 총 연속한 1의 수
    cnt = 0         # 현재 연속한 1의 수

    for i in range(N):
        if num[i] == "1":   # 현재 숫자가 1일때
            cnt += 1

        else:
            if total_cnt < cnt:     # 총 연속한 개수보다 현재 연속한 개수가 더 많을 때
                total_cnt = cnt
            cnt = 0

        if num[-1] == "1":          # 마지막 숫자가 1이면
            if total_cnt < cnt:     # 숫자 업데이트
                total_cnt = cnt

    print(f"#{tc} {total_cnt}")