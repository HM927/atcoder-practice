N, M = map(int, input().split())

A_num = [0]*M
B_num = [0]*M

for i in range(N):
    A, B = map(int, input().split())
    A_num[A - 1] += 1
    B_num[B - 1] += 1

for j in range(M):
    print(B_num[j] - A_num[j])