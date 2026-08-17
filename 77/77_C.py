def binary_search(numbers, value):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] <= value:
            left = mid + 1
        elif numbers[mid] > value:
            right = mid - 1
        
    return left

N = int(input())

A_list = [] * 3
sorted_A_list = [] * 3
for i in range(3):
    A_list.append(list(map(int, input().split())))
    sorted_A_list.append(sorted(A_list[i]))

count = 0
a_count = 0
c_count = 0
for i in sorted_A_list[1]:
    a_count = binary_search(sorted_A_list[0], i - 1)
    value = binary_search(sorted_A_list[2], i)
    c_count = N - value
    count += a_count * c_count

print(count)