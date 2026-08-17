s = list(input())

count = 0
result = 0
for i in range(len(s)):
    if s[i] in "ACGT":
        count += 1
    else:
        result = max(result, count)
        count = 0
    result = max(result, count)

print(result)