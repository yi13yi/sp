T = int(input())

for tc in range(1, T+1):
    N = list(map(int, input().split()))
    n = 0
    for i in range(0, 10):
        if N[i]%2 == 1:
            n += N[i]
        else:
            continue

    print(f"#{tc} {n}")