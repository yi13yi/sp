# for문 range 자리에 리스트를 넣으면 i가 리스트의 요소를 직접적으로 받기에
# index 번호를 알고 싶으면 range 쓰고 밑에서 리스트 받기

num = list(int(input()) for _ in range(9))

max_number = 0
max_index = 0
for i in range(9):
    if num[i] > max_number:
        max_number = num[i]
        max_index = i + 1

print(max_number, max_index)


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