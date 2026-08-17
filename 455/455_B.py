H, W = map(int, input().split())
gride =  []

for i in range(H):
    row = input()
    gride.append(row)

count = 0
for h_1 in range(H):
    for h_2 in range(h_1, H):
        for w_1 in range(W):
            for w_2 in range(w_1, W):
                for i in range(h_1, h_2):
                    for j in range(w_1, w_2):
                        if(gride[i][j] == gride[h_1 + h_2 - i][w_1 + w_2 - j]):
                            print("i" + " " + str(i))
                            print("j" + " " + str(j))
                            print("h_1 + h_2 - i" + " " + str(h_1 + h_2 - i))
                            print("w_1 + w_2 - j" + " " + str(w_1 + w_2 - j))
                            count += 1

print("count" + " " + str(count))

