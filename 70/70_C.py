import math

n = int(input())

T_list = []
for i in range(n):
    T_list.append(int(input()))

ans = math.lcm(*T_list)
print(ans)