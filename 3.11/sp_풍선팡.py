# 5:00 ~ 5: 40

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, 1, 0, -1]  # 행
    dc = [1, 0, -1, 0]  # 열
    max_v = 0   # max 0으로 초기화

    for i in range(N):              # i, j는 전체 탐색
        flower_sum = 0
        for j in range(M):
            flower_sum = arr[i][j]
            for k in range(4):      # k, l은 상하좌우 탐색
                for l in range(1, arr[i][j] + 1):
                    nr = j + dr[k] * l
                    nc = i + dc[k] * l
                    if 0 <= nr < M and 0 <= nc < N :
                        flower_sum += arr[nc][nr]
            max_v = max(max_v, flower_sum)
    print(f"#{tc} {max_v}")

