import sys

t = list(map(int, input().split()))
n = int(input())



r_list = []
g_list = []
b_list = []
for i in range(n):
    r, g, b = map(int, input().split())
    r_list.append(r)
    g_list.append(g)
    b_list.append(b)


for i in range(1,2 ** n):
    r_ans, g_ans, b_ans = False, False, False
    r_sum, g_sum, b_sum = 0, 0, 0
    denominator = 0
    for j in range(n):
        denominator += (i >> j & 1)
        if i  >> j & 1:
            r_sum += r_list[j]
            g_sum += g_list[j]
            b_sum += b_list[j]

    if r_sum // denominator == t[0]:
        r_ans = True

    if g_sum // denominator == t[1]:
        g_ans = True

    if b_sum // denominator == t[2]:
        b_ans = True

    if r_ans and g_ans and b_ans:
        print("Yes")
        sys.exit()

print("No")



