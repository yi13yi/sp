N = int(input())
num_list = list(map(int, input().split()))

num_min = float('inf')
num_max = float('-inf')

for i in range(len(num_list)):
    if num_list[i] < num_min:
        num_min = num_list[i]

    if num_list[i] > num_max:
        num_max = num_list[i]

print(num_min, num_max)