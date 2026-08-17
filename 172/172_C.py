def binary_search(numbers, value):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] <= value:
            left = mid + 1
        else:
            right = mid - 1

    return left


N, M, K = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_sum = [0] * (N + 1)
for i in range(1, N + 1):
    A_sum[i] += A_sum[i - 1] + A_list[i - 1]

B_sum = [0] * (M + 1)
for i in range(1, M + 1):
    B_sum[i] += B_sum[i - 1] + B_list[i - 1]


sum = 0
answer = -1
for A_count in range(N + 1):
    sum = A_sum[A_count]

    if sum > K:
        break

    B_count = binary_search(B_sum, K - sum) - 1
    count = A_count + B_count
    answer = max(answer, count)

print(answer)