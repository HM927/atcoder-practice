n = int(input())
a_list = list(map(int, input().split()))

dif = 0
max_dif = 0
for i in range(n):
    for j in range(i,n):
        dif = abs(a_list[i] - a_list[j])
        max_dif = max(dif, max_dif)

print(max_dif)