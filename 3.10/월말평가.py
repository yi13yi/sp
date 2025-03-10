T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        a,b,c = map(int, input().split())
        b -= 1

        for k in range(1, c+1):
            if b-k < 0 or b+k>= N:
                break

            if arr[b+k] == arr[b-k]:
                arr[b+k] = (arr[b+k]+1)%2
                arr[b-k] = (arr[b-k]+1)%2

    print(f"#{tc}", *arr)