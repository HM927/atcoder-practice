a, b, c = map(int, input().split())

max_num = max(a, b, c)
min_ans = max_num * 3

sum = a + b + c

while True:
    if (min_ans - sum) % 2 != 0:
        min_ans += 3
    else:
        break

ans = (min_ans - sum) / 2
print(int(ans))