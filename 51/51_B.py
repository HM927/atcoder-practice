K, S = map(int, input().split())

count = 0
for X in range(K + 1):
    for Y in range(K + 1):
        if X + Y + K < S:
            continue

        Z = S - X - Y

        if Z <= K and 0 <= Z:
            count += 1

print(count)