import numpy as np
N = int(input())
L = list(map(int, input().split()))
location = 0.5
count = 0
sign_past = 1
num = 0

def move(location, num, sign_past, count):
    if(num == N + 1):
        return
    sub(location, num, sign_past, count)
    sum(location, num, sign_past)

    
def sub(location, num, sign_past, oount):
    location -= L[num]
    num += 1
    sign_now = np.sign(location)
    if(sign_now != sign_past):
        count += 1
    sign_now = sign_past   

    move(location, num, sign_past, count)

def sum(location, num, sign_past, count):
    location += L[num]
    num += 1
    sign_now = np.sign(location)
    if(sign_now != sign_past):
        count += 1
    sign_now = sign_past  

    move(location, num, sign_past, count)

move(location, num, sign_past, count)
print(count) 


# def solve():
#       N = int(input())
#       L = list(map(int, input().split()))

#       ans = 0
#       def dfs(i, pos, count):
#           nonlocal ans
#           if i == N:
#               ans = max(ans, count)
#               return
#           for d in [1, -1]:
#               new_pos = pos + d * L[i]
#               cross = 1 if pos * new_pos < 0 else 0  #
#   符号が変われば通過
#               dfs(i + 1, new_pos, count + cross)

#       dfs(0, 0.5, 0)
#       print(ans)

#   solve()