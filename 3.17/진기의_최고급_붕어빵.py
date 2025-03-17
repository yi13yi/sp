# 12:05 ~ 12:40
# 17:00 ~ 17:20

# sort와 sorted

# sort() 원본 리스트 자체를 정렬
# a.sort()

# sorted() 정렬된 새로운 리스트 생성
# a_sorted = sorted(a)


T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # N명, M초만에, K개
    people = list(map(int, input().split()))

    people.sort()
    # 순서대로 정렬해 앞에서부터 되는지를 확인

    for i in range(len(people)):
        bread = (people[i] // M) * K

        if bread < i+1:     # i는 0부터 시작하기에 +1
            print(f"#{tc} Impossible")
            break

    else:
        print(f"#{tc} Possible")
    # else가 for문의 안에 있다면 break를 만나 else까지 오지 못함
    # 중복 호출