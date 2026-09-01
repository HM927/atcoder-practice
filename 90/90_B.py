import sys
n = int(input())
a_list = list(map(int, input().split()))

for i in range(1, n):

    if a_list[i] * a_list[0] ** (i - 1) != a_list[1] ** i:
        print("No")
        sys.exit()

print("Yes")