S = input()
K = int(input())

answer = -1
right = 0
num = 0
for left in range(len(S)):

    while right < len(S):
        if S[right] == ".":
            if num == K:
                break

            num += 1
        right += 1
    answer = max(answer, right - left)

    if S[left] == ".":
        num -= 1

print(answer)