T = int(input())  # 테스트 케이스 개수
for t in range(1, T + 1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    max_sum = -float('inf')  # 최댓값을 찾기 위한 초기값
                             # 가장 작은 음수의 수 라는 의미
                             
    if N <= M:
        for i in range(M - N + 1):  # Bj에서 Ai와 맞춰서 슬라이딩
            m_sum = 0
            for j in range(N):  # Ai와 Bj의 곱의 합을 직접 구함
                m_sum += Ai[j] * Bj[i + j]
            if m_sum > max_sum:  # 최댓값 갱신
                max_sum = m_sum

    # if와 else문 둘 다 내용은 거의 같지만 길이를 어떤걸 기준으로 하나의 다름 

    else:
        for i in range(N - M + 1):  # Ai에서 Bj와 맞춰서 슬라이딩
            m_sum = 0
            for j in range(M):  # Bj와 Ai의 곱의 합을 직접 구함
                m_sum += Bj[j] * Ai[i + j]
            if m_sum > max_sum:  # 최댓값 갱신
                max_sum = m_sum

    print(f'#{t} {max_sum}')
