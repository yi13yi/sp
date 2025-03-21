def preorder(tree, index):      # 전위
    if index >= len(tree):
        return ""
    left = preorder(tree, 2 * index + 1)
    right = preorder(tree, 2 * index + 2)
    return str(tree[index]) + left + right


def inorder(tree, index):       # 중위
    if index >= len(tree):
        return ""
    left = inorder(tree, 2 * index + 1)
    right = inorder(tree, 2 * index + 2)
    return left + str(tree[index]) + right


def postorder(tree, index):     # 후위
    if index >= len(tree):
        return ""
    left = postorder(tree, 2 * index + 1)
    right = postorder(tree, 2 * index + 2)
    return left + right + str(tree[index])


def binary_to_decimal(binary_str):
    return int(binary_str, 2)


T = int(input())
for t in range(1, T + 1):
    N = int(input())  # 정점의 개수
    tree = list(map(int, input().split()))  # 트리의 값들

    # 전위 순회, 중위 순회, 후위 순회
    preorder_result = preorder(tree, 0)
    inorder_result = inorder(tree, 0)
    postorder_result = postorder(tree, 0)

    # 각각을 이진수로 변환 후 십진수로 계산
    results = [
        binary_to_decimal(preorder_result),
        binary_to_decimal(inorder_result),
        binary_to_decimal(postorder_result)
    ]

    # 가장 큰 값을 구함
    max_value = max(results)

    # 출력 형식에 맞게 출력
    print(f"#{t} {max_value}")