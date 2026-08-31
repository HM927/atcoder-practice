n, r = map(int, input().split())

ans = r
for i in range(n):
    d, a = map(int, input().split())

    if d == 1:
        if 1600 <= ans and ans <= 2799:
            ans += a

    if d == 2:
        if 1200 <= ans and ans <= 2399:
            ans += a

print(ans)