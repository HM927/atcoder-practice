import sys

N, Y = map(int, input().split())

for ten_thousand in range(N + 1):
    for five_thousand in range(N - ten_thousand + 1):
            thousand = N - ten_thousand - five_thousand

            if 10000 * ten_thousand + 5000 * five_thousand + 1000 * thousand == Y:
                print(str(ten_thousand) + " " + str(five_thousand) + " " + str(thousand))
                sys.exit()
                
print("-1 -1 -1")