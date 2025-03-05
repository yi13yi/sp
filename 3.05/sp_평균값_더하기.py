T = int(input())

for tc in range(1, T+1):
    N = list(map(int, input().split()))
    n = 0
    b = 0

    for i in range(0, 10):
        n += N[i]

    a = n // 10

    if n % 10 > 5:
        b = 1

    num = a + b

    print(f"#{tc} {num}")

