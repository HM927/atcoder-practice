import heapq
Q = int(input())
tree_list = []
for i in range(Q):
    query, hight = map(int, input().split())
    if(query == 1):
        heapq.heappush(tree_list, hight)
    else:
        while 0 < len(tree_list):
            if(tree_list[0] <= hight):
                heapq.heappop(tree_list)
            else:
                break
    print(len(tree_list))
