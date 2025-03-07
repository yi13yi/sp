# 15:35 ~

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())
        i = i-1

        for k in range(1, j+1):
            if arr[i-1] == arr[i+1]:
                arr[i-1] = (arr[i-1]+1)%2
                arr[i+1] = (arr[i+1]+1)%2

            if k < 0 and k > N:
                break

    print(f"# {tc} {arr}")

