from dataclasses import dataclass
from collections import deque

@dataclass
class loc:
   x: int
   y: int
   count: int
   
def is_way(c, x, y):
    if x < 1 or C < x or y < 1 or R < y:
      return False
    
    if c[y - 1][x - 1] == "#":
        return False
    return True

R, C = map(int, input().split())
s_y, s_x = map(int, input().split())
g_y, g_x = map(int, input().split())

c = [] * R
for i in range(R):
 c.append(input())

target = deque()
searched = [[0] * C for i in range(R)]

target.append(loc(s_x, s_y, 0))
searched[s_y - 1][s_x - 1] = 1

while target:
   cursor = target.popleft()

   x = cursor.x
   y = cursor.y

   if x == g_x and y == g_y:
        print(cursor.count)
        break

   if is_way(c, x, y + 1) and searched[y][x - 1] == 0:
    target.append(loc(x, y + 1, cursor.count + 1))
    searched[y][x - 1] = 1

   if is_way(c, x + 1, y) and searched[y - 1][x] == 0:
    target.append(loc(x + 1, y, cursor.count + 1))
    searched[y - 1][x] = 1

   if is_way(c, x, y -1) and searched[y - 2][x - 1] == 0:
    target.append(loc(x, y - 1, cursor.count + 1))
    searched[y - 2][x - 1] = 1

   if is_way(c, x - 1, y) and searched[y - 1][x - 2] == 0:
    target.append(loc(x - 1, y, cursor.count + 1))
    searched[y - 1][x - 2] = 1


