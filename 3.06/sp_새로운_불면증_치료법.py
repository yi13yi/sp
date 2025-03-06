# 5:05 ~

T = int(input())

num_all = set('0123456789') # 0부터 9까지의 숫자를 나타내는 집합
                            # ''를 사용해서 하나하나 분리

# 각 테스트 케이스 처리
for tc in range(1, T + 1):
    N = int(input())  # 양의 번호 N
    seen_num = set()  # 지금까지 본 숫자들을 저장할 집합
                         # 중복이 안되기에 set 사용

    k = 0  # 몇 번째 양을 셀지 추적하는 변수
    
    while seen_num != num_all:  # 모든 숫자를 봤다면 종료
        k += 1
        current_number = k * N  # 현재 세고 있는 양의 번호
        seen_num.update(str(current_number))  # 현재 번호에서 나온 숫자를 추가

    print(f"#{tc} {current_number}")


