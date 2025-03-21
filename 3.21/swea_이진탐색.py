# 트리의 모양이 중위순회

def inorder(t):
    global num

    if t > N:
        return

    else:
        inorder(2 * t)  # 루트가 1이라 왼쪽 노드는 2*t가 된다

        tree[t] = num   # 중위순회라 여기서 정산
        num += 1        # 1씩 커져야 중위순회 순서대로 숫자배치 가능

        inorder(2 * t + 1)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    tree = [0] * (N + 1)
    num = 1  # 0부터가 아닌 1부터 시작하기에

    inorder(1)  # 1을 넣어 함수 호출

    root = tree[1]      # 중위순회를 한다고 해서 루트가 1번이 아닌것은 아니다
    node = tree[N // 2]

    print(f"#{tc} {root} {node}")