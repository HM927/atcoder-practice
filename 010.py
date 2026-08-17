N = int(input())

class1 = [0] * (N + 1)
class2 = [0] * (N + 1)

for i in range(1, N + 1):
    c, p = map(int, input().split())

    class1[i] = class1[i - 1]
    class2[i] = class2[i - 1]

    if c == 1:
        class1[i] += p
    else:
        class2[i] += p

Q = int(input())

class1_sum = [0] * (Q + 1) 
class2_sum = [0] * (Q + 1)
for i in range(Q):
    L, R = map(int, input().split())

    class1_sum[i] = class1[R] - class1[L - 1]
    class2_sum[i] = class2[R] - class2[L - 1]

for i in range(Q):
    print(str(class1_sum[i]) + " " + str(class2_sum[i]))