# 15:35 ~ 16:31

T = int(input())
 
for tc in range(1, T+1):    
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
 
    for _ in range(M):
        i, j = map(int, input().split())
        i -= 1     # 인덱스 기준이라 -1
 
        for k in range(1, j+1):     # j번 반복의 필요
            if i-k < 0 or i+k >=N:  # 범위에서 벗어나는 수 처리
                break
     
            if arr[i-k] == arr[i+k]:        
                arr[i-k] = (arr[i-k]+1)%2   # 0이면 1, 1이면 0으로 바꿈
                arr[i+k] = (arr[i+k]+1)%2
 
    print(f'#{tc}', *arr)