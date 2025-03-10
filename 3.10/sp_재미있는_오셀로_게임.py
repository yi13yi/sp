t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    mid = n // 2
    board[mid-1][mid-1], board[mid][mid] = 2, 2
    board[mid-1][mid], board[mid][mid-1] = 1, 1
    
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    for _ in range(m):
        x, y, color = map(int, input().split())
        x, y = x - 1, y - 1
        if board[x][y] == 0:
            opp = 3 - color
            valid = False
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                flip = []
                while 0 <= nx < n and 0 <= ny < n and board[nx][ny] == opp:
                    flip.append((nx, ny))
                    nx, ny = nx + dx, ny + dy
                if flip and 0 <= nx < n and 0 <= ny < n and board[nx][ny] == color:
                    valid = True
                    for fx, fy in flip:
                        board[fx][fy] = color
            
            if valid:
                board[x][y] = color
    
    black = sum(row.count(1) for row in board)
    white = sum(row.count(2) for row in board)
    print(f"# {t} {black} {white} ")
