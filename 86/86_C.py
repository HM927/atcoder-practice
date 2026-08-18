import sys
N = int(input())

x = 0
y = 0
j = 0
t = 0
for i in range(N):
    t, x_g, y_g = map(int, input().split())

    while j < t:
        if x < x_g:
            x += 1
        elif x > x_g:
            x -= 1
        elif y < y_g:
            y += 1
        elif y > y_g:
            y -= 1
        elif x == x_g and y == y_g:
            x += 1
        j += 1

    if x != x_g or y != y_g:
        print("No")
        sys.exit()

print("Yes")