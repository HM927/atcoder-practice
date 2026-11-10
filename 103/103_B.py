import sys

s = list(input())
t = list(input())

for i in range(len(s)):
    
    if s == t:
        print("Yes")
        sys.exit()

    temp = s[0]
    
    for j in range(len(s) - 1):
        s[j] = s[j + 1]
    
    s[len(s) - 1] = temp

print("No")