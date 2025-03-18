N = int(input())
N_list = list(int(input()) for _ in range(N))

cnt = 1     # 가장 뒤에 있는 막대는 바로 볼수 있어 cnt 하나 추가하고 시작
see_stick = N_list[-1]     # 가장 뒤에 있는 막대

for i in range(N-2, -1, -1):    # 가장 뒤에 있는 막대 제외
    if see_stick < N_list[i]:
        cnt += 1
        see_stick = N_list[i]

print(cnt)