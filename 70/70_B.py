a, b, c, d = map(int, input().split())

start = max(a, c)
fin = min(b, d)
if fin - start <= 0:
    print(0)
else:
    print(fin - start)