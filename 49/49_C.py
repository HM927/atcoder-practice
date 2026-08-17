import sys

S = list(input())

while S:
    if 7 <= len(S) and S[-7] == "d" and S[-6] == "r" and S[-5] == "e" and S[-4] == "a" and S[-3] == "m" and S[-2] == "e" and S[-1] == "r":
        del S[-7:]
    elif 5 <= len(S) and S[-5] == "d" and S[-4] == "r" and S[-3] == "e" and S[-2] == "a" and S[-1] == "m":
        del S[-5:]
    elif 6 <= len(S) and S[-6] == "e" and S[-5] == "r" and S[-4] == "a" and S[-3] == "s" and S[-2] == "e" and S[-1] == "r":
        del S[-6:]
    elif 5 <= len(S) and S[-5] == "e" and S[-4] == "r" and S[-3] == "a" and S[-2] == "s" and S[-1] == "e":
        del S[-5:]
    else:
        print("NO")
        sys.exit(0)

print("YES")