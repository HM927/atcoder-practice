N, M = map(int, input().split())

s_list = [] * N
for i in range(N):
    s_list.append(input())
    s_list[i] = s_list[i][-3:]

t_list = [] * M
for i in range(M):
    t_list.append(input())
t_set = set(t_list)

count = 0
for i in range(N):
    for j in t_set:
        if s_list[i] == j:
            count += 1

print(count)
