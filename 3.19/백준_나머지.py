N = list(int(input()) for _ in range(10))
remain = []
cnt = 0

for i in N:
    remain += [i % 42]

set_remain = set(remain)    # 중복 없게 set으로 저장

for i in set_remain:
    cnt += 1

print(cnt)
# print(len(set_remain))     # set은 count를 쓰지못해 len으로 쓰기
