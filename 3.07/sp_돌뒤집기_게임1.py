# 2:32 ~ 3:12

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())    # i번째, j개 돌

        for k in range(i-1, i+j-1):
            # 인덱스라 시작은 -1로
            # 끝나는 부분은 해당숫자 미포함이라 -1 한번 더 해줄 필요 없음 
            if k >= N:  
                break
            if arr[k] != arr[i-1]: 
                arr[k] = arr[i-1]
            
    print(f"#{tc}", *arr)       