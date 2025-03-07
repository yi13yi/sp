# 2:32 ~ 3:12

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())

        for k in range(i-1, i+j-1):
            if k >= N:
                break
            if arr[k] != arr[i-1]:
                arr[k] = arr[i-1]
            


    print(f"#{tc}", *arr)       
