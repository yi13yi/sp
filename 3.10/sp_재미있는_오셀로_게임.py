# 4:30 ~ 5:40

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # N: 보드의 한변의 길이
    board = [[0] * N for _ in range(N)]     # M: 돌을 놓는 횟수
    mid = N // 2
    board[mid-1][mid-1], board[mid][mid] = 2, 2     # 보드 기준 대각선 
    board[mid-1][mid], board[mid][mid-1] = 1, 1     # 1: 흑돌 2: 백돌 
                                                    # 이건 이미 놓고 시작
    
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    # 중간을 제외한 8방향 탐색
    # (0,0)은 제외된다
    
    for _ in range(M):
        x, y, color = map(int, input().split())
        x, y = x - 1, y - 1     # 인덱스 기준이라 -1 해놓기

        if board[x][y] == 0:    # 돌이 숫자가 없어야 빈칸이라 놓을 수 있음
            opp = 3 - color     # opp는 상대 돌을 의미
            valid = False       # 처음에는 돌을 뒤집을 수 없다 가정
                                # 8방향 탐색하며 돌 뒤집을 수 있는 경우 True로 변경
                                # True일때만 돌 놓기
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy     # 현재위치
                flip = []                   # 뒤집을 돌을 저장할 리스트
                while 0 <= nx < N and 0 <= ny < N and board[nx][ny] == opp:
                    # 보드 범위 안에 있어야 함
                    # 보드 안에 상대 돌이 있을 때만 진행
                    flip.append((nx, ny))       # 현재 위치의 상대 돌을 뒤집을 후보로 저장
                    nx, ny = nx + dx, ny + dy   # 같은 방향으로 계속 이동하여 다음 칸 확인
                if flip and 0 <= nx < N and 0 <= ny < N and board[nx][ny] == color:
                    # filp에 값이 있고 같은 색 돌을 만났는지 확인
                    # 내 돌과 같은 돌로 둘러싸였는지 확인
                    valid = True
                    for fx, fy in flip:
                        board[fx][fy] = color
                        # 상대편의 돌이었던게 내 돌로 변경
            
            if valid:
                board[x][y] = color     # 비어있는 위치에 새롭게 돌을놓는 것
    
    black = 0  # 흑돌의 개수
    white = 0  # 백돌의 개수

    for row in board:
        for block in row:
            if block == 1:  # 흑돌이면
                black += 1
            elif block == 2:  # 백돌이면
                white += 1

    print(f"#{tc} {black} {white} ")
