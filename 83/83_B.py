N, A, B = map(int, input().split())

nums = []

sum = 0
number = 0
for i in range(min(B + 1, 10)):
    for j in range(min(B + 1, 10)):
        for k in range(min(B + 1, 10)):
            for l in range(min(B + 1, 10)):
                for m in range(min(B - i - j - k - l + 1, 10)):
                    sum = i + j + k + l + m
                    number = 10000 * i + 1000 * j + 100 * k + 10 * l + m
                    if len(str(N)) + 1 <= len(str(number)):
                        break

                    if A <= sum and sum <= B and number <= N:
                        nums.append(number)

ans = 0           
for i in nums:
    ans += i
print(ans)
