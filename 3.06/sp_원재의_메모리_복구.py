# 5:00 ~ 5:30
T = int(input())

for tc in range(1, T+1):
    memory = input() # int로 받으면 맨 앞이 0일 때 0이 사라짐
                     # 그러므로 문자열로 받아 비교 대상도 문자열로 설정
    count = 0
    f_value = '0'   # memory도 문자열의 형태라 f_value 문자열 형태로 만들기

    for i in memory:
        if i != f_value:
            count += 1
        f_value = i     # 다를 때만 업데이트를 해줘도 좋지만 
                        # 오류 발생할 수 있으므로 매번 업데이트 해주기

    print(f"#{tc} {count}")