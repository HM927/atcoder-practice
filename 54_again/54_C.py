N, M = map(int, input().split())

e = [] * M
for i in range(M):
    e.append(list(map(int, input().split())))

searched = []
target_v = []

target_v.append(1)
searched.append(1)

count = 0
answer = 0
while target_v:

    cursor = target_v.pop()

    for search_e in e:

        if cursor in search_e:
            next_v = search_e[0] if search_e[0] != cursor else search_e[1]

            if next_v in searched:
                continue

            target_v.append(next_v)
            searched.append(next_v)

    # print(searched)
    print(target_v)


