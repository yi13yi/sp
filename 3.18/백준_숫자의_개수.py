A = int(input())
B = int(input())
C = int(input())

result = list(str(A * B * C))
# int로는 탐색하는데 한계
# 문자열로 탐색

for i in range(10):
    print(result.count(str(i)))
    # result사 문자열이므로 i 또한 문자로 사용


'''
150
266
427
'''
