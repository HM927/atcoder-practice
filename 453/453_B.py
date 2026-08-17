T, X = map(int, input().split())
A_list = list(map(int, input().split()))
A = A_list[0]

print("0" + " " + str(A_list[0]))

for i in range(T + 1):
    if(X <= abs(A - A_list[i])):
        A = A_list[i]
        print(str(i) + " " + str(A))
