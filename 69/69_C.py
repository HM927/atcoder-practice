N = int(input())
a = list(map(int, input().split()))

four_num = 0
two_num = 0
for i in range(N):
    if a[i] % 4 == 0:
        four_num += 1
    elif a[i] % 2 == 0:
        two_num += 1

if four_num >= (N // 2):
    print("Yes")
elif four_num >= ((N - (two_num // 2) * 2) // 2):
    print("Yes")
else:
    print("No")