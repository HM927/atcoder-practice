N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

flag = True
for i in range(N):
    if(i + 1 != B_list[A_list[i] - 1]):
        flag = False

if (flag):
    print("Yes")
else:
    print("No")