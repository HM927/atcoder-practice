n = int(input())
k = int(input())
x_list = list(map(int, input().split()))

sum = 0
for i in range(n):
    sum += 2 * min(x_list[i], abs(x_list[i] - k))

print(sum)