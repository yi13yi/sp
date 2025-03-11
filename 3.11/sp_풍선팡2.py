# 5:50 ~ 6:20

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, 1, 0, -1] # 상 우 하 좌
    dc = [-1, 0, 1, 0]
    max_v = 0
 
    for i in range(N):
        flower_sum = 0
        for j in range(M):
            flower_sum = arr[i][j]
            for k in range(4):  # 네 방향 탐색
                nr = j + dr[k]
                nc = i + dc[k]
                if 0 <= nr < M and 0 <= nc < N :
                    flower_sum += arr[nc][nr]
            max_v = max(max_v, flower_sum)
    print(f"#{tc} {max_v}")