n = int(input())
ans = []

while True:
    quotient = (n - 2 + 1) // (-2)
    remainder = n - (quotient * (-2))

    ans.append(remainder)

    if not(quotient):
        break

    n = quotient


for i in range(len(ans)):
    a = ans.pop()
    print(a, end="")