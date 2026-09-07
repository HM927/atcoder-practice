def search_all(n):
    if n < 6:
        return n // 1

    a = search_part(n, 9)
    b = search_part(n, 6)

    return min(a, b)

def search_part(n, num):
    i = 0
    while num ** (i + 1) <= n:
        i += 1

    n -= num ** i

    return search_all(n) + 1

    


n = int(input())

count = search_all(n)

print(count)