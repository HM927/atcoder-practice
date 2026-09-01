n, m = map(int, input().split())
a_list = list(map(int, input().split()))
a_set = set(a_list)

nums = set()
for i in range(n):
    nums.add(i + 1)

ans = nums - a_set
print(len(ans))

for i in sorted(ans):
    print(i, end=" ")