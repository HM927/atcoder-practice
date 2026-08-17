A, B, X = map(int, input().split())

max = 10 ** 9 + 1
min = 0
mid = (min + max) // 2
while max - min > 1:
    mid = (min + max) // 2

    if A * mid + B * len(str(mid)) <= X:
        min = mid
    
    else:
        max = mid

N = min
print(N)
