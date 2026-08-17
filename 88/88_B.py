N = int(input())
a_list = list(map(int, input().split()))
a_list.sort()

sum = 0
flag = True
for i in range(N):
    if flag:
        sum += a_list.pop(-1)
        flag = False
    else:
        sum -= a_list.pop(-1)
        flag = True

print(sum)