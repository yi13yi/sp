T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_list = [2, 3, 5, 7, 11]
    count = [0] * len(num_list)

    for i in range(len(num_list)):
        while N % num_list[i] == 0:
            N //= num_list[i]
            count[i] += 1

    print(f"#{tc}", *count)