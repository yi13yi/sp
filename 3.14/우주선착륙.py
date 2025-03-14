T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    height = [list(map(int, input().split())) for _ in range(N)]

    # 8방향 배열 (상, 하, 좌, 우, 좌상, 우상, 좌하, 우하)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    c_count = 0  # 후보지 개수

    # 각 지점에 대해 8방향을 확인
    for i in range(N):
        for j in range(M):
            current_height = height[i][j]
            lower_count = 0

            # 8방향 확인
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M:  # 인덱스 범위 체크
                    if height[ni][nj] < current_height:
                        lower_count += 1

            # 4방향 이상에서 낮은 지형이 있어야 후보지
            if lower_count >= 4:
                c_count += 1

    print(f"#{t} {c_count}")
