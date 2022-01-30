# from collections import deque

# def getRelated(town, node, N):
#     nodes = []
#     nodeRow = node//N
#     nodeCol = node%N
    
#     # Left nodes 
#     for i in range(nodeCol-1, -1, -1):
#         if town[nodeRow][i]==1:
#             nodes.append(nodeRow*N+i)
#         else:
#             break
        
#     #Right nodes
#     for i in range(nodeCol+1, N):
#         if town[nodeRow][i]==1:
#             nodes.append(nodeRow*N+i)
#         else:
#             break
    
#     #top nodes
#     for i in range(nodeRow-1, -1, -1):
#         if town[i][nodeCol]==1:
#             nodes.append(i*N+nodeCol)
#         else:
#             break
    
#     for i in range(nodeRow+1, N):
#         if town[i][nodeCol]==1:
#             nodes.append(i*N+nodeCol)
#         else:
#             break
    
#     return nodes


# queue = deque()

# N = int(input())

# #getting matrix town
# town = []
# for i in range(N):
#     l = list(map(int, input().split()))
#     town.append(l)

# #getting source and destination
# source_row, source_col = map(int, input().split())
# destination_row, destination_col = map(int, input().split())

# #converting 2D to 1D position

# [[9 6 2], 
# [8 5 4],
# [6 7 2],
# [3,3,3]]
# 2D array can be transformed to [9, 6, 2, 8, 5, 4, 6, 7, 2, 3, 3, 3]
# Index can be achieved by 1d_index = row*(total number of col) + col
# arr[2][1] => 2*3 + 1 = 9



# source = source_row*N + source_col
# destination = destination_row*N + destination_col

# visited = [False for i in range(N*N)]

# streets = [0 for i in range(N*N)]

# queue.append(source)
# visited[source] = True
# streets[source] = 0
# flag = 0

# while len(queue)!=0:
#     node = queue.popleft()
#     related = getRelated(town, node, N)
#     for i in related:
#         if not visited[i]:
#             queue.append(i)
#             visited[i] = True
#             streets[i] = 1+streets[node]
#             if i==destination:
#                 flag = 1
#                 print(streets[i])
#                 break
# if flag==0:
#     print(streets[destination])



# CORONA VIRUS

# from collections import deque

# R, C = map(int, input().split())
# matrix = []

# healthy = 0
# queue = deque()
# days = 0

# for i in range(R):
#     l = list(map(int, input().split()))
#     for j in range(C):
#         if l[j]==1:
#             healthy+=1
#         if l[j]==2:
#             queue.append(i*C+j)
#     matrix.append(l)


# queue.append(-1)

# while len(queue) != 0:
#     node = queue.popleft()
#     if node==-1:
#         if len(queue)==0:
#             continue
#         else:
#             days += 1
#             queue.append(-1)
    
#     else:    
#         row = node//C
#         col = node%C
#         if col!=0 and matrix[row][col-1]==1:
#             matrix[row][col-1] = 2
#             queue.append(row*C+col-1)
#             healthy -=1
        
#         if col!=C-1 and matrix[row][col+1]==1:
#             matrix[row][col+1]=2
#             queue.append(row*C+col+1)
#             healthy -= 1
        
#         if row!=0 and matrix[row-1][col]==1:
#             matrix[row-1][col]=2
#             queue.append((row-1)*C+col)
#             healthy -= 1
            
#         if row!=R-1 and matrix[row+1][col]==1:
#             matrix[row+1][col]=2
#             queue.append((row+1)*C+col)
#             healthy -= 1
            
        
    
# print(days if healthy==0 else -1)
    
    
# import sys
# sys.setrecursionlimit(10**8)


# def maximum_revenue(wine_prices, maximum, left, right, year):
#     if maximum[left][right] != 0:
#         return maximum[left][right]
    
#     if left==right:
#         return wine_prices[left]*year
    
#     left_revenue = wine_prices[left]*year + maximum_revenue(wine_prices, maximum, left+1, right, year+1)
    
#     right_revenue = wine_prices[right]*year + maximum_revenue(wine_prices, maximum, left, right-1, year+1)
    
#     maximum[left][right] = max(left_revenue, right_revenue)
    
#     return maximum[left][right]

# n = int(input())

# wine_prices = list(map(int, input().split()))

# maximum = [[0 for i in range(n)] for j in range(n)]

# print(maximum_revenue(wine_prices, maximum, 0, n-1, 1))



# N, R = map(int, input().split())

# people = [0 for i in range(N+1)]

# for i in range(R):
#     p, follow = map(int, input().split())
#     people[p] -= 1
#     people[follow] += 1

# flag = 0
# for i in range(1, N+1):
#     if people[i]==N-1:
#         flag = 1
#         print(i)
#         break
#     else:
#         continue

# if flag==0:
#     print(-1)

# from collections import OrderedDict

# foodorder = []
# fooditems = OrderedDict()

# n = int(input())

# for i in range(n):
#     l = list(input().split())
#     foodorder.append(l)
#     for j in l:
#         if j not in fooditems:
#             fooditems[j]=list([])

# # print(fooditems)
# # print(foodorder)

# for index, items in enumerate(foodorder):
#     for item in items:
#         fooditems[item].append(index)
# print(fooditems)

# items = sorted(fooditems.values(), reverse=True, key=len)
# print(items)


# for i in range(1,len(items)):
#     t = []
#     for j in items[i]:
#         if j not in items[0]:
#             t.append(j)
#     items[i] = t
# print(items)

# items = sorted(items, reverse=True, key=len)

# count = 1
# val = 1
# while len(items[0])<n and val<len(items):
#     items[0] = items[0] + items[val]
#     val += 1
#     count += 1

# print(items)
# print(count)


from collections import OrderedDict

foodorder = []
fooditems = OrderedDict()

n = int(input())

for i in range(n):
    l = list(input().split())
    foodorder.append(l)
    for j in l:
        if j not in fooditems:
            fooditems[j]=list([])

for index, items in enumerate(foodorder):
    for item in items:
        fooditems[item].append(index)

items = sorted(fooditems.values(), reverse=True, key=len)

for i in range(1, len(items)):
    t = []
    for j in items[i]:
        if j not in items[0]:
            t.append(j)
    items[i] = t

items = sorted(items, reverse=True, key=len)
count = 1
val = 1
while len(items[0])<n and val<len(items):
    items[0] = items[0] + items[val]
    val += 1
    count += 1
    
print(count)
        

