h, w = map(int, input().split())

grid = [[] * w for i in range(h)]

for i in range(h):
    grid[i] = list(input())

delete_column = []
for i in range(h):
    brank_sum = 0
    for j in range(w):

        if grid[i][j] == ".":
            brank_sum += 1

    if brank_sum == w:
        delete_column.append(i)
        
for i in reversed(delete_column):
    del grid[i]


delete_row = []
for i in range(w):
    brank_sum = 0
    for j in range(len(grid)):

        if grid[j][i] == ".":
            brank_sum += 1

    if brank_sum == len(grid):
        delete_row.append(i)


for i in reversed(delete_row):
    for j in range(len(grid)):
        del grid[j][i]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        print(grid[i][j], end="")

    print()