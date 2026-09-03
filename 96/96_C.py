import sys
h, w = map(int, input().split())

s = [[] * w] * h
for i in range(h):
    s[i] = input()

for i in range(h):
    for j in range(w):

        if s[i][j] == "#":

            if i - 1 >= 0 and s[i - 1][j] == "#":
                continue

            elif j - 1 >= 0 and s[i][j - 1] == "#":
                continue

            elif i + 1 < h and s[i + 1][j] == "#":
                continue

            elif j + 1 < w and s[i][j + 1] == "#":
                continue

            else:
                print("No")
                sys.exit()

print("Yes")

