def check_slope(row):
    cnt = 1
    # 경사로를 놓을 수 있는 길이 카운트 (최소 1칸부터 시작)
    # 첫 번째 칸을 포함하는 연속된 칸들의 개수를 추적하는 변수
    # 첫 번째 칸은 연속한다 생각하고 1로 설정
    for i in range(1, N):
        # 두 번째 칸부터 마지막 칸까지 검사
        if row[i] == row[i-1]:
            cnt += 1
            # i가 그 전 칸과 같은 높이라면
            # 경사로를 놓을 수 있는 길이를 늘림
        elif row[i] - row[i-1] == 1 and cnt >= X:   # 높이 1 높아지면
            cnt = 1
            # 같은 길이가 이어지다가 높이가 1 높아짐
            # 활주로 확정
        elif row[i-1] - row[i] == 1 and cnt >= 0:   # 높이 1 낮아지면
            cnt = -X + 1
            # 높이가 낮아진다면 cnt는 -X + 1해서 반복 후 만약 0인 된다면 활주로 확정
        else:   # 높이 2 이상 차이나면
            return 0
    if cnt >= 0:
        return 1
    return 0


T = int(input())
for tc in range(T):
    N, X = map(int, input().split())
    A = []
    result = 0
    for i in range(N):
        A.append(list(map(int, input().split())))
        result += check_slope(A[i])

    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(A[j][i])
        result += check_slope(temp)

    print(f"#{tc+1} {result}")