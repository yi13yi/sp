# 1. 슬라이싱
N = int(input())
N_list = []

for i in range(1, N+1):
    N_list += [i]       # 1부터 N까지의 숫자 리스트 생성

while len(N_list) > 1:      # 리스트의 길이가 1보다 크다면
    N_list = N_list[1::2]   # 1번부터 2칸씩 건너뛰고 인덱스 선택
                            # [시작 : 끝 : 건너뛰는 크기]

print(*N_list)


# 2. 반복문
N = int(input())
N_list = []

for i in range(1, N+1):
    N_list += [i]

while len(N_list) > 1:
    new_list = []      # 빈 리스트 생성
    for i in range(len(N_list)):
        if i % 2 != 0:                      # 짝수 인덱스가 아니라면
            new_list.append(N_list[i])      # 새로운 리스트에 추가
    N_list = new_list

print(*N_list)
