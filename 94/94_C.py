n = int(input())
x_list = list(map(int, input().split()))

if n % 2 == 0:
    med = n // 2 - 1
else:
    med = (n + 1) // 2 - 1

sorted_x_list = x_list.copy()
sorted_x_list.sort(reverse=False)
for i in range(n):
    if x_list[i] <= sorted_x_list[med]:
        print(sorted_x_list[med + 1])
    else:
        print(sorted_x_list[med])
