# # import math
# # def isPronic(n):
# #     n = int(n)
# #     if n==0:
# #         return True
# #     for i in range(1, int(math.sqrt(n))+1):
# #         if(i*(i+1)==n):
# #             return True
# #     return False

# # l = []
# # for i in range(1000):
# #     l.append(i*(i+1))
# # N = input().strip()
# # right = 0
# # left = 0
# # size = len(N)
# # #print(size)
# # while(left<size):
# #     right = left
# #     while(right<size):
# #         if int(N[left:right+1]) in l:
# #             print(int(N[left:right+1]), end=" ")
# #             if(N[left]=="0"):
# #                 break
# #             right+=1
# #         elif isPronic(N[left:right+1]):
# #             print(int(N[left:right+1]), end=" ")
# #             if(N[left]=="0"):
# #                 break
# #             right+=1
# #         else:
# #             right+=1
# #     left += 1

# from math import sqrt
# def isPronic(n):
#     global l
#     n = int(n)
#     if n in l:
#         return True
#     if n==0:
#         return True
#     for i in range(1, int(sqrt(n))+1):
#         if (i*(i+1)==n):
#             return True
#     return False

# l = []
# for i in range(1000):
#     l.append(i*(i+1))
# N = input().strip()
# right = 0
# left = 0
# size = len(N)
# while(left<size):
#     right = left
#     while(right<size):
#         if isPronic(N[left:right+1]):
#             print(int(N[left:right+1]), end=" ")
#             if N[left]=="0":
#                 break
#             right += 1
#         else:
#             right += 1
#     left += 1


# S = input()
# C = 0
# l = []
# l.insert(0,0)
# for i in S:
#     if i.isalpha():
#         continue
#     elif i.isalnum():
#         l.append(int(i))
#     else:
#         C += 1

# flag = 1 if C%2==1 else 0
# ctr = 1
# temp = []
# while ctr<len(l):
#     if len(temp)!=0 and temp[0]%2==flag:
#         print(temp[0], end=" ")
#         del temp[0]
#         flag= 0 if flag==1 else 1
#     elif l[ctr]%2==flag:
#         print(l[ctr], end=" ")
#         flag= 0 if flag==1 else 1
#         ctr += 1
#     else:
#         temp.append(l[ctr])
#         ctr += 1
# if len(temp)!=0:
#     for i in temp:
#         print(i, end=" ")
        

# S = input()
# C = 0
# l = []
# l.insert(0,0)
# for i in S:
#     if i.isalpha():
#         continue
#     elif i.isalnum():
#         l.append(int(i))
#     else:
#         C += 1
# flag = 1 if C%2==1 else 0
# ctr = 1
# temp = []
# while ctr<len(l):
#     if len(temp)!=0 and temp[0]%2==flag:
#         print(temp[0], end=" ")
#         del temp[0]
#         flag = 0 if flag==1 else 1
#     elif l[ctr]%2==flag:
#         print(l[ctr], end=" ")
#         flag=0 if flag==1 else 1
#         ctr+=1
#     else:
#         temp.append(l[ctr])
#         ctr += 1
# if len(temp)!=0:
#     for i in temp:
#         print(i, end=" ")

# SODOKU VALIDATION    

# row = col = box = [1 for i in range(9)]

# matrix = []
# for i in range(9):
#     l = list(map(int, input().split()))
#     matrix.append(l)
# for i in range(9):
#     for j in range(9):
#         n = matrix[i][j]
#         row[i] |= (1<<n)
#         col[i] |= (1<<n)
#         box[(i//3)*3 + j//3] |= (1<<n)
        
# val = (1<<10)-1
# flag = 0
# for i in range(9):
#     if row[i] != val or col[i]!= val or box[i] != val:
#         print("INVALID")
#         flag = 1
#         break
# print(row, col, box, sep="   ")
# if flag==0:
#     print("VALID")


# R, C = map(int, input().split())
# rowSum = [[0 for j in range(C+1)] for i in range(R)]
# curr = 0
# for i in range(R):
#     l = list(map(int, input().split()))
#     l.insert(0,0)
#     for j in range(1,C+1):
#         rowSum[i][j] = l[j] + rowSum[i][j-1]
# K = int(input())
# maxSum = 0

# for i in range(R-K+1):
#     for j in range(C-K+1):
#         sum = 0
#         for srow in range(i, i+K):
#             sum += rowSum[srow][j+K-1]
#         if sum>maxSum:
#             maxSum = sum
# print(maxSum)

# S, K = input().split()
# K = int(K)
# start = end = max = 0
# unique = 1
# length = len(S)
# arr = [0 for i in range(128)]
# arr[ord(S[end])] = 1
# maxStart = 0
# maxEnd = 0
# while end<length:
#     if K==unique:
#         current = end - start + 1
#         if current > max:
#             max = current
#             maxStart = start
#             maxEnd = end
#     if unique<=K:
#         end += 1
#         if end==len(S):
#             break
#         arr[ord(S[end])] += 1
#         if arr[ord(S[end])]==1:
#             unique += 1
#     else:
#         arr[ord(S[start])] -= 1
#         if arr[ord(S[end])]==0:
#             unique -= 1
#         start += 1
# print(maxStart, maxEnd, sep="  ")
# print(S[maxStart:maxEnd+1])



# n = int(input())
# l = list(map(int, input().split()))
# diff = 0
# x = 0
# y = 0
# for start in range(n):
#     for end in range(start,n-1): 
#         #print(start, end, sep=" - ")
#         temp = l[start:end+1].count(0) - l[start:end+1].count(1)
#         # print(temp)
#         if temp>diff:
#             diff = temp
#             x = start
#             y = end

#         else:
#             continue
# #print(x, y, sep=" - ")
# for i in range(x, y+1):
#     l[i] = 0 if l[i]==1 else 1
# print(l.count(1))




# S = input().strip()
# uppercase = []
# lowercase = []
# for i in S:
#     if i.isupper():
#         uppercase.append(i)
#     else:
#         lowercase.append(i)
# uppercase.sort()
# lowercase.sort()

# ctr = 0
# while(ctr!=len(uppercase) and ctr!=len(lowercase)):
#     print(uppercase[ctr]+lowercase[ctr], end="")
#     ctr += 1
    
# if len(uppercase)!=0:
#     print(*uppercase[ctr:])
# if len(lowercase)!=0:
#     print(*lowercase[ctr:])




# N = int(input())
# stocks = list(map(int, input().split()))
# minPrice = stocks[0]
# for i in range(1, N):
#     if stocks[i]<minPrice:
#         minPrice = stocks[i]
#     else:
#         maxProfit = minPrice - stocks[i]
# print(maxProfit)

# N = int(input())
# profit = 0
# stocks = list(map(int, input().split()))
# for i in range(1,N):
#     if stocks[i-1]<stocks[i]:
#         profit += stocks[i]-stocks[i-1]
#     else:
#         continue
# print(profit)

# n = int(input())
# l = []
# for i in range(n):
#     l.append(input().strip())
# d = {}
# for i in l[0]:
#     d[i]=1
# for string in range(1, len(l)):
#     for i in l[string]:
#         if i in d.keys():
#             if d[i]==string:
#                 d[i]+=1
#             else:
#                 continue
#         else:
#             continue
# temp = []
# for i in d.keys():
#     if d[i]==len(l):
#         temp.append(i)
# temp = temp.sort()
# print("".join(temp))
# print()


# n = int(input())
# l = []
# for i in range(n):
#     l.append(input().strip())
# d = {}
# for string in range(len(l)):
#     visted = []
#     for i in l[string]:
#         if i not in visted:
#             visted.append(i)
#             if i in d.keys():
#                 d[i]+=1
#             else:
#                 d[i] = 1
#         else:
#             continue
#     visted=[]

# temp = []
# for i in d.keys():
#     if d[i]==len(l) or d[i]==len(l)-1:
#         temp.append(i)
# temp.sort()
# print("".join(temp))

# Largest possible odd integer

# n = int(input())
# digits = [0 for i in range(10)]

# while n>0:
#     digits[n%10] += 1
#     n = n//10
    
# unitdigit = -1

# for i in range(1, 10, 2):
#     if digits[i]>0:
#         unitdigit = i
#         digits[i] -= 1
#         break
    
# if unitdigit==-1:
#     print("no")
# else:
#     start = 1
#     for i in range(1,10):
#         if digits[i]>0:
#             start = 0
#             break
        
#     for i in range(9, start-1, -1):
#         while digits[i]>0:
#             print(i,end="")
#             digits[i] -= 1

#     print(unitdigit, end="")




# Smallest Odd integer
# n = int(input())
# digit = [0 for i in range(10)]

# while n>0:
#     digit[n%10] += 1
#     n = n//10

# unitdigit = -1

# for i in range(9,0,-2):
#     if digit[i]>0:
#         unitdigit = i
#         digit[i] -= 1
#         break

# if unitdigit==-1:
#     print("no")
# else:
#     start = 1
#     for i in range(1,10):
#         if digit[i]>0:
#             print(i, end="")
#             digit[i] -= 1
#             start = 0
#             break
#     for i in range(start, 10):
#         if digit[i]>0:
#             print(str(i)*digit[i], end="")
#     print(unitdigit, end="")

#Your code below
# n=int(input())
# d={}
# for i in range(10):
#     d[i]=0 
# while(n>0):
#     rem=n%10
#     n=n//10
#     d[rem]+=1 
# ud=-1
# for i in range(9,0,-2):
#     if d[i]>0:
#         ud=i 
#         d[i]-=1
#         break
# if ud==-1:
#     print("no")
# else:
#     start=1
#     for i in range(1,10):
#         if d[i]>0:
#             print(str(i),end="")
#             d[i]-=1 
#             start=0
#             break
#     for i in range(start,10):
#         if d[i]>0:
#             print(str(i)*d[i],end="")
#     print(ud)
# print(d)

#Matrix Zig Zag

# R, C = map(int, input().split())
# matrix = []
# for i in range(R):
#     l = list(map(int, input().split()))
#     matrix.append(l)
# row = 0
# col = 0
# dir = 1
# for iter in range(1, R+C):
#     if dir==1:
#         while row>=0 and col<C:
#             print(matrix[row][col], end=" ")
#             row -= 1
#             col += 1
#         dir = -1
#         if row<0 and col<C:
#             row = 0
#         if col>=C:
#             col = C-1
#             row += 2
#     else:
#         while row<R and col>=0:
#             print(matrix[row][col], end=" ")
#             row += 1
#             col -= 1
#         dir = 1
#         if col<0 and row<R:
#             col = 0
#         if row>=R:
#             row = R-1
#             col += 2



#Matrix Zig Zag Bottomleft

# R, C = map(int, input().split())
# matrix = []
# for i in range(R):
#     l = list(map(int, input().split()))
#     matrix.append(l)
# row = R-1
# col = C-1
# dir = 1
# for iter in range(1, R+C):
#     if dir==1:
#         while row>=0 and col<C:
#             print(matrix[row][col], end=" ")
#             row -= 1
#             col += 1
#         dir = -1
#         if row<0:
#             row = 0
#             col -= 2
            
#         if col>=C and row>=0:
#             col = C-1
            
#     else:
#         while row<R and col>=0:
#             print(matrix[row][col], end=" ")
#             row += 1
#             col -= 1
#         dir = 1
#         if col<0:
#             col = 0
#             row -= 2
            
#         if row>=R:
#             row = R-1






# N, K = map(int, input().split())

# ordered_dict = []

# for i in range(K):
#     temp = list(map(int, input().split()))
#     ordered_dict.append(temp)
    
# ordered_dict = sorted(ordered_dict)

# table = [[0 for i in range(N+1)] for j in range(K+1)]

# cost = [l[0] for l in ordered_dict]
# profit = [l[1] for l in ordered_dict]
# cost.insert(0,0)
# profit.insert(0,0)
# flag = 0
# for item in range(1, K+1):
#     if cost[item]>N:
#         print(table[item-1][N])
#         flag = 1
#         break
    
#     for amount in range(1, N+1):
#         if amount<cost[item]:
#             table[item][amount] = table[item-1][amount]
#         else:
#             incProfit = profit[item] + table[item-1][amount-cost[item]]
#             excProfit = table[item-1][amount]
#             table[item][amount] = max(incProfit, excProfit)

# if flag==0:
#     print(table[K][N])



#Largest square matrix with 1s

# R, C = map(int, input().split())

# matrix = []

# for i in range(R):
#     l = list(map(int, input().split()))
#     matrix.append(l)

# maxval = 0

# for i in range(1, R):
#     for j in range(1,C):
#         if matrix[i][j] != 0:
#             matrix[i][j] = matrix[i][j] + min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1])
#             if matrix[i][j]>maxval:
#                 maxval = matrix[i][j]
#         else:
#             continue
# print(maxval)


# import sys
# sys.setrecursionlimit(10**8)

# def  breakWord(words, s, output, start):
#     if start == len(s):
#         print(output.strip())
#         return
#     for i in range(start, len(s)):
#         word = s[start:i+1]
#         if word in words:
#             breakWord(words, s, output+word+" ", i+1)

# words = list(input().split())

# s = input()

# breakWord(words, s,"", 0)



#define pronic function
# def pronic(n):
#     if n==0:
#         return True
#     for i in range(1, (n//2)+1):
#         if i*(i+1)==n:
#             return True
#     return False

# x = input()

# array = [x[i:j+1] for i in range(len(x)) for j in range(i, len(x))]

# final = []

# for i in array:
#     if int(i) not in final:
#         if pronic(int(i)):
#             final.append(int(i))


# def ComputeMax(N, D, K, toll_distance, toll_fares):
#     revenue = [0 for i in range(N+1)]
#     revenue[0] = 0
#     index = 0
#     for i in range(1, N+1):
#         if toll_distance[index]==i:
#             if i<=D:
#                 revenue[i] = max(revenue[i-1], toll_fares[index])
#             else:
#                 revenue[i] = max(revenue[i-1], toll_fares[index]+revenue[i-D-1])
#             index += 1
#             if index==K:
#                 return revenue[i]
#         else:
#             revenue[i] = revenue[i-1]

# N, D = map(int, input().split())
# K = int(input())
# toll_distance = list(map(int, input().split()))
# toll_fares = list(map(int, input().split()))
# print(ComputeMax(N, D, K, toll_distance, toll_fares))

# text = input().strip()
# wildcard = input().strip()

# matrix = [[0 for i in range(len(wildcard)+1)] for j in range(len(text)+1)]

# matrix[0][0] = 1

# if wildcard[0] == "*":
#     matrix[0][1] = 1



# for i in range(1,len(text)+1):
    
#     for j in range(1,len(wildcard)+1):
        
#         if wildcard[j-1]=="?" or wildcard[j-1]==text[i-1]:
#             matrix[i][j] = matrix[i-1][j-1]
            
#         elif wildcard[j-1]=="*":
#             if matrix[i-1][j]==1 or matrix[i][j-1]==1:
#                 matrix[i][j] = 1
                
            
# if matrix[-1][-1]==1:
#     print("Matching")
# else:
#     print("Not matching")


# N = int(input())
# arr = []
# for i in range(N):
#     R, C = map(int, input().split())
#     matrix = []
#     for i in range(R):
#         l = list(map(int, input().split()))
#         matrix.append(l)
    
#     for row in range(1,R):
        
#         temp = sorted(matrix[row-1])
#         firstmax = temp[-1]
#         secondmax = temp[-2]
        
#         for col in range(C):
             
#             if matrix[row-1][col] != firstmax:
#                 matrix[row][col] += firstmax
#             else:
#                 matrix[row][col] += secondmax
                
        
#     arr.append(max(matrix[-1]))

# for i in arr:
#     print(i)

# import math
# def isPronic(n):
#     global l
#     n = int(n)
#     if n==0:
#         return True
#     if n in l:
#         return True
#     for i in range(1, int(math.sqrt(n))+1):
#         if(i*(i+1)==n):
#             return True
#     return False

# l = []
# for i in range(1000):
#     l.append(i*(i+1))

# N = input().strip()
# right = 0
# left = 0
# size = len(N)
# while(left<size):
#     right = left
#     while(right<size):
#         if isPronic(N[left:right+1]):
#             print(int(N[left:right+1]), end=" ")
#             if(N[left]=="0"):
#                 break
#             right+=1
#         else:
#             right+=1
#     left += 1

# from collections import deque
    
# N, K = map(int, input().strip().split(','))

# alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# students = [alphabets[i] for i in range(N)]
    
# photographs = []
# for i in range(K):
#     l = input().strip().split(',')
#     photographs.append(l)

# missing = False

# for name in students:
#     rel_count = 0
#     queue = deque()
#     visited = []
#     queue.append(name)
#     visited.append(name)
#     while len(queue) != 0:
#         student = queue.popleft()
#         for seq in photographs:
#             if student in seq:
#                 successor = seq[seq.index(student):]
#                 for succstd in successor:
#                     if not succstd in visited:
#                         queue.append(succstd)
#                         visited.append(succstd)
#                         rel_count += 1
#     queue.append(name)
    
#     while len(queue) != 0:
#         student = queue.popleft()
#         for seq in photographs:
#             if student in seq:
#                 predecessor = seq[0:seq.index(student)+1]
#                 for prestd in predecessor:
#                     if not prestd in visited:
#                         queue.append(prestd)
#                         visited.append(prestd)
#                         rel_count += 1
    
#     if rel_count!=N-1:
#         missing = True
#         print(name, end=" ")

# if not missing:
#     print("N/A")


N = int(input())
start = []
end = []
for i in range(N):
    l = input().split()
    start.append(int("".join(l[0].split(':'))))
    end.append(int("".join(l[1].split(':'))))

computers = 0

start.sort()
end.sort()

start_index = 0
end_index = 0

while start_index < len(start) and end_index < len(end):
    temp = abs(start_index - end_index) + 1
    if temp>computers:
        computers = temp
        
    if start[start_index] < end[end_index]:
        start_index += 1
    else:
        end_index += 1
        
    while end_index < len(end) and start_index < len(start) and end[end_index] <= start[start_index]:
        end_index += 1

print(computers)
