# 12:00 ~ 13:20

def check_sudoku(sudoku):
    valid_set = set(range(1, 10))  # 1부터 9까지의 집합 {1,2,3,4,5,6,7,8,9}
    
    # 가로(행) 검사
    for row in sudoku:
        if set(row) != valid_set:   # set 특성상 순서 상관없이 같은가? 같지 않은가?만 확인
            return 0  # 유효하지 않으면 0 반환
    
    # 세로(열) 검사
    for col_idx in range(9):
        col = [sudoku[row_idx][col_idx] for row_idx in range(9)]
        # 가로 행과 달리 세로 행에서 이 부분이 추가된것은 
        # 가로 행은 이미 리스트 안에 완성 되어 있지만 세로 행은 완성된게 없어서 만들어줘야함
        if set(col) != valid_set:
            return 0  # 유효하지 않으면 0 반환
    
    # 3x3 박스 검사
    for i in range(0, 9, 3):    # 0,3,6에서 확인
        for j in range(0, 9, 3):
            box = []
            for x in range(3):
                for y in range(3):
                    box.append(sudoku[i + x][j + y])
            if set(box) != valid_set:
                return 0  # 유효하지 않으면 0 반환
    
    return 1  # 모든 검사를 통과하면 유효함


T = int(input())  # 테스트 케이스 수 입력
for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]  # 9x9 스도쿠 판 입력
    
    result = check_sudoku(sudoku)  
    print(f"#{tc} {result}")  
