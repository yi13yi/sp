def check_s(arr_s):
    valid_set = set(range(1, 10))

    for row in arr_s:
        if set(row) != valid_set:
            return 0

    for col_idx in range(9):
        col = []
        for row_idx in range(9):            # 풀어 쓴 방식
            num = arr_s[row_idx][col_idx]
            col.append(num)

        if set(col) != valid_set:
            return 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):    
            box = []
            for x in range(3):
                for y in range(3):
                    num = arr_s[i + x][j + y]
                    box.append(num)

            if set(box) != valid_set:
                return 0
    return 1


T = int(input())

for tc in range(1, T + 1):
    arr_s = [list(map(int, input().split())) for _ in range(9)]
    result = check_s(arr_s)

    print(f"# {tc} {result}")
