# i는 정수라 i만 적으면 안되고 리스트에 저장하기 위해서는 [i] 같은 형태 가능

N, X = map(int, input().split())
A = list(map(int, input().split()))
min_num = []

for i in A:
    if i < X:
        min_num += [i]

print(*min_num)

'''
10 5
1 10 4 9 2 3 8 5 7 6
'''