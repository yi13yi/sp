# 전위 순회 (Preorder) 함수
def preorder(tree, index):
    if index >= len(tree):  # 트리의 범위를 벗어나면 종료
        return ""
    # 현재 노드를 방문한 후, 왼쪽 자식, 오른쪽 자식 순으로 재귀 호출
    left = preorder(tree, 2 * index + 1)
    right = preorder(tree, 2 * index + 2)
    return str(tree[index]) + left + right  # 현재 노드 값 + 왼쪽 + 오른쪽 순서로 결과 반환


# 중위 순회 (Inorder) 함수
def inorder(tree, index):
    if index >= len(tree):  # 트리의 범위를 벗어나면 종료
        return ""
    # 왼쪽 자식, 현재 노드, 오른쪽 자식 순으로 재귀 호출
    left = inorder(tree, 2 * index + 1)
    right = inorder(tree, 2 * index + 2)
    return left + str(tree[index]) + right  # 왼쪽 + 현재 노드 + 오른쪽 순서로 결과 반환


# 후위 순회 (Postorder) 함수
def postorder(tree, index):
    if index >= len(tree):  # 트리의 범위를 벗어나면 종료
        return ""
    # 왼쪽 자식, 오른쪽 자식, 현재 노드 순으로 재귀 호출
    left = postorder(tree, 2 * index + 1)
    right = postorder(tree, 2 * index + 2)
    return left + right + str(tree[index])  # 왼쪽 + 오른쪽 + 현재 노드 순서로 결과 반환


# 이진수 문자열을 십진수로 변환하는 함수
def binary_to_decimal(binary_str):
    return int(binary_str, 2)  # 이진수를 십진수로 변환


# 테스트 케이스 처리
T = int(input())  # 테스트 케이스 개수
for t in range(1, T + 1):
    N = int(input())  # 정점의 개수
    tree = list(map(int, input().split()))  # 트리의 값들 (1 또는 0)

    # 전위, 중위, 후위 순회를 통해 이진수 문자열을 얻음
    preorder_result = preorder(tree, 0)
    inorder_result = inorder(tree, 0)
    postorder_result = postorder(tree, 0)

    # 각각의 이진수를 십진수로 변환
    results = [
        binary_to_decimal(preorder_result),
        binary_to_decimal(inorder_result),
        binary_to_decimal(postorder_result)
    ]

    # 변환된 십진수 값들 중 최댓값을 구함
    max_value = max(results)

    # 출력 형식에 맞게 결과 출력
    print(f"#{t} {max_value}")
