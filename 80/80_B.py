s = input()

count = 0
for i in range(1, len(s)):
    if s[i] == "-":
        count += 1

    if s[i] == "|":
        print(count, end=" ")
        count = 0
