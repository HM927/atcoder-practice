N = int(input())
S = input()

W_nums = [0] * (N + 1)
E_nums = [0] * (N + 1)
for i in range(1, N + 1):

    W_nums[i] = W_nums[i - 1]
    E_nums[i] = E_nums[i - 1]

    if S[i - 1] == "W":
        W_nums[i] += 1
    else:
        E_nums[i] += 1

sum = 0
result = N
for i in range(1, N + 1):
    sum = W_nums[i - 1] + E_nums[N] - E_nums[i]

    result = min(result, sum)

print(result)