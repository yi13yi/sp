# 테스트 케이스 수 입력
T = int(input())

for t in range(1, T + 1):
    # 농장의 크기 N 입력
    N = int(input())
    
    # 농장의 농작물 가치 입력
    farm = [list(map(int, input().split())) for _ in range(N)]
    
    # 농장의 중심 좌표 (N//2, N//2)
    center = N // 2
    profit = 0
    
    # 마름모 형태로 농작물 가치를 합산
    for i in range(N):
        for j in range(N):
            # 각 좌표 (i, j)가 마름모 형태 안에 있는지 체크
            if abs(center - i) + abs(center - j) <= center:
                profit += farm[i][j]
    
    # 결과 출력
    print(f'#{t} {profit}')
