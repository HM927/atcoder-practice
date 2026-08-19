A, B, C, X, Y = map(int, input().split())

S = 0
while 0 < X or 0 < Y:
    if 2 * C <= A + B and X >= 1 and Y >= 1:
        X -= 1
        Y -= 1
        S += 2 * C

    elif A >= 2 * C and X >= 1:
        X -= 1
        S += 2 * C

    elif B >= 2 * C and Y >= 1:
        Y -= 1
        S += 2 * C

    elif 0 < X:
        X -= 1
        S += A

    elif 0 < Y:
        Y -= 1
        S += B

print(S)