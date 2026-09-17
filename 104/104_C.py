d, g = map(int, input().split())

p_list = [] * d
c_list = [] * d
for i in range(d):
    p, c = map(int, input().split())
    p_list.append(p)
    c_list.append(c)

sum = 0
count = 0
min_count = float("inf")
for i in range(2 ** d):
    sum = 0
    count = 0
    for j in range(d):
        if (i >> j) & 1:
            sum += (j + 1) * 100 * p_list[j] + c_list[j]
            count += p_list[j]

    if sum < g:
        for k in reversed(range(d)):
            if sum >= g:
                break

            if not((i >> k) & 1):
                additional = (g - sum + (k + 1) * 100 - 1) // ((k + 1) * 100)

                if additional >= p_list[k]:
                    additional = p_list[k]

                sum += (k + 1) * 100 * additional
                count += additional

    min_count = min(min_count, count)

print(min_count)



