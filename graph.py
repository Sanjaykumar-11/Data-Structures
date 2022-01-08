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
    
    
    



