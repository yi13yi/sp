T = int(input())  # 테스트 케이스 개수

# 학점 등급 리스트
grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for t in range(1, T + 1):
    N, K = map(int, input().split())  # 학생 수 N, 학점을 알고 싶은 학생 K
    scores = []
    
    for i in range(N):
        mid, final, hw = map(int, input().split())
        total = mid * 0.35 + final * 0.45 + hw * 0.2
        scores.append((total, i + 1))   # 총점과 학생 번호 저장 / 인덱스보다 +1
                                        # 리스트 안에 각 원소가 튜플로 저장
    
    scores.sort(reverse=True, key=lambda x: x[0])  # 총점 기준 내림차순 정렬
                                                   # 총점 큰 곳에서 낮은 곳으로 흘러간다
                                                   # reverse를 그냥 사용한다면 기본이 reverse = False 기본은 오름차순
                                                   # 튜플은 딕셔너리와는 다름, 리스트와 비슷하지만 변경불가
                                                   # key=lambda x: x[0] 이 부분은 각 튜플에서 첫번째 원소를 기준으로 정렬
    # 학점 부여 기준: N/10 명씩 동일 학점 부여
    per_grade = N // 10  # 각 학점당 학생 수
    student_rank = {scores[i][1]: grades[i // per_grade] for i in range(N)}
    # scores[i][1] 이 부분은 튜플에서 학생 번호를 의미
    # grades[i // per_grade]를 사용해서 정렬된 자리 나누기 학점당 학생 수해서 몫만큼 등급 부여
    # student_rank는 딕셔너리로 저장
    # 출력할 때 K가 키로 적용

    print(f"#{t} {student_rank[K]}")