def isEven(num, list):
    for i in range(num):
        if list[i] % 2 != 0:
            return False
    return True

N = int(input())
A = list(map(int, input().split()))

count = 0
while True:
    if (isEven(N, A)):
        for i in range(N):
            A[i] /= 2
            
        count+=1
    else:
        break

print(count)
