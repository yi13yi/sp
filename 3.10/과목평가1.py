T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    init_arr = list(map(int, input().split()))

    for _ in range(M):
        a,b,c, = map(int, input().split())

        b -= 1

        for i in range(b, b+c):
            if b+c> N or b < 0:
                break
            else:
                init_arr[i] = (init_arr[i]+1)%2

    print(f"#{tc}", *init_arr)