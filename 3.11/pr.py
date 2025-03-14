T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        a,b,c = map(int, input().split())
        b -= 1

        for k in range(b, b+c):
            if b+c> N or b<0:
                break
            else:
                arr[]k          
