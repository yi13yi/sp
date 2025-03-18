# map은 반복 가능한 객체의 각 요소에 지정한 함수를 적용하는 역할

num = list(int(input()) for _ in range(9))

max_num = max(num)
max_id = num.index(max_num) +1
print(max_num, max_id)


'''
3
29
38
12
57
74
40
85
61
'''