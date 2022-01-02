#Robot stair climbing problem

# N, S = map(int, input().split(' '))
# leaps = list(map(int, input().split(' ')))
# ways = []
# for i in range(N+1):
#     ways.append(0)
# ways[0] = 1
# for i in range(1, N+1):
#     for j in range(0, len(leaps)):
#         if(i>=leaps[j]):
#             ways[i] += ways[i-leaps[j]];
# print(ways[N])






#Robot Stair Climbing with damaged stair 

# N, S, damage_count = map(int, input().split(' '))
# leaps = list(map(int, input().split(' ')))
# T = list(map(int, input().split(' ')))
# ways = []
# for i in range(N+1):
#     ways.append(0)
# ways[0] = 1
# for i in range(1, N+1):
#     if(i in T):
#         ways[i] = 0
#         continue
#     for j in range(len(leaps)):
#             ways[i] += ways[i-leaps[j]]
# print(ways[N])






#Robot Stair Climbing with slipery stair 

# N, S, slipery_count = map(int, input().split(' '))
# leaps = list(map(int, input().split(' ')))
# T = list(map(int, input().split(' ')))
# ways = []
# for i in range(N+1):
#     ways.append(0)
# ways[0] = 1
# for i in range(1, N+1):
#     for j in range(len(leaps)):
#         ways[i] += ways[i-leaps[j]]
#     if(i in T):
#         last_non_slippery = i-1;
#         while(last_non_slippery in T and last_non_slippery>0):
#             last_non_slippery -= 1
#         if last_non_slippery>0:
#             ways[last_non_slippery] += ways[i]
#         ways[i]=0
# print(ways[N])





#program to print nextgreater element using stack

# from collections import deque
# n = int(input())
# l = list(map(int, input().split()))
# stack = deque()
# for i in range(n-1, -1, -1):
#     if(len(stack)==0):
#         stack.append(l[i])
#     else:
#         if(stack[len(stack)-1] > l[i]):
#             nextgreater = stack[len(stack)-1];
#             stack.append(l[i])
#             l[i] = nextgreater
#         else:
#             while(len(stack) != 0 and  stack[len(stack)-1] <= l[i]):
#                 del stack[(len(stack)-1)]
#             if(len(stack)==0):
#                 stack.append(l[i])
#             else:
#                 nextgreater = stack[len(stack)-1];
#                 stack.append(l[i])
#                 l[i] = nextgreater
# for i in l:
#     print(i, end=" ")






#Remove adjacent Equal values

# from collections import deque
# n = int(input())
# l = list(map(int, input().split()))
# stack = deque()
# for i in range(len(l)):
#     if(len(stack)==0):
#         stack.append(l[i])
#     else:
#         if(stack[(len(stack)-1)]==l[i]):
#             del stack[len(stack)-1]
#         else:
#             stack.append(l[i])
# if(len(stack)==0):
#     print(-1)
# else:
#     for i in stack:
#         print(i, end=" ")








#longest common signal

# s1 = input().strip()
# s2 = input().strip()
# matrix = [[0 for i in range(len(s2))] for j in range(len(s1))]
# max = 0
# for i in range(len(s1)):
#     for j in range(len(s2)):
#         if(s1[i]==s2[j]):
#             matrix[i][j] = 1
#         if(i!=0 and j!=0):
#             matrix[i][j] += matrix[i-1][j-1]
#         if(matrix[i][j]>max):
#             max = matrix[i][j]
# print(max)





# longest subarray with equal number of alpha and numbers

# s = input()
# pos = 0
# count = 0
# maxlen = 0;
# d = {}
# d[count] = pos
# for i in s:
#     pos += 1
#     if(i.isalpha()):
#         count += 1
#     else:
#         count -= 1
#     if(count in d.keys()):
#         current = pos - d[count]
#         if(current>maxlen):
#             maxlen=current
#         else:
#             d[count] = pos
# print(maxlen)


#Matrix Spiral printing

# def printLeftToRight(matrix, row, startcol, endcol):
#     for i in range(startcol, endcol+1):
#         print(matrix[row][i], end=" ")
# def printRightToLeft(matrix, row, startcol, endcol):
#     for i in range(startcol, endcol-1, -1):
#         print(matrix[row][i], end=" ")
# def printTopToBottom(matrix, col, startrow, endrow):
#     for i in range(startrow, endrow+1):
#         print(matrix[i][col], end=" ")
# def printBottomToTop(matrix, col, startrow, endrow):
#     for i in range(startrow, endrow-1, -1):
#         print(matrix[i][col], end=" ")

# R, C = map(int, input().split())

# matrix = []
# for i in range(R):
#     l = list(map(int, input().split()))
#     matrix.append(l)

# startrow = 0
# endrow = R-1
# startcol = 0
# endcol = C-1

# while(startrow<=endrow and startcol<=endcol):
#     printTopToBottom(matrix, startcol, startrow, endrow)
#     printLeftToRight(matrix, endrow, startcol+1, endcol)
#     if(startcol != endcol):
#         printBottomToTop(matrix, endcol, endrow-1, startrow)
#     if(endcol != startcol):
#         printRightToLeft(matrix, startrow, endcol-1, startcol+1);
#     startrow += 1
#     startcol += 1
#     endrow -= 1
#     endcol -= 1
 






# Board game

# R, C = map(int, input().split())
# matrix = []
# for i in range(R):
#     l = list(map(int, input().split()))
#     matrix.append(l)

# max = [[0 for i in range(C)] for j in range(R)]

# for i in range(C):
#     if(i==0):
#         max[0][i] = matrix[0][i]
#     else:
#         max[0][i] += matrix[0][i] + max[0][i-1]

# for i in range(R):
#     if(i==0):
#         max[i][0] = matrix[i][0]
#     else:
#         max[i][0] += matrix[i][0] + max[i-1][0]
  
# for i in range(1, R):
#     for j in range(1, C):
#         max[i][j] += (max[i][j-1]+matrix[i][j]) if max[i][j-1]>max[i-1][j] else (max[i-1][j]+matrix[i][j])


# print(max[R-1][C-1])








#

# R, C = map(int, input().split())
# matrix = []
# for i in range(R):
#     l = list(map(int, input().split()))
#     matrix.append(l)

# startrow, startcol = map(int, input().split())

# ans = matrix

# for i in range(startcol+1, C):
#     ans[startrow][i] = matrix[startrow][i] + ans[startrow][i-1]

# for i in range(startrow+1, R):
#     ans[i][startcol] = ans[i][startcol] + ans[i-1][startcol]

# for i in range(startrow+1, R):
#     for j in range(startcol+1, C):
#         ans[i][j] = (ans[i][j-1]+matrix[i][j]) if ans[i][j-1]>ans[i-1][j] else (ans[i-1][j]+matrix[i][j])

# print(ans[R-1][C-1])







# R, C = map(int, input().split())
# matrix = []
# for i in range(R):
#     l = list(map(int, input().split()))
#     matrix.append(l)
# startrow, startcol = map(int, input().split())
# ans = matrix
# for i in range(startcol+1, C):
#     ans[startrow][i] = matrix[startrow][i] + ans[startrow][i-1]
# for i in range(startrow+1, R):
#     ans[i][startcol] = ans[i][startcol] + ans[i-1][startcol]

# for i in range(startrow+1, R):
#     for j in range(startcol+1, C):
#         ans[i][j] = (ans[i][j-1] + matrix[i][j]) if ans[i][j-1]>ans[i-1][j] else (ans[i-1][j]+matrix[i][j])
# print(ans[R-1][C-1])











# n = int(input())
# l = list(map(int, input().split()))
# count = 0
# majority = 0
# for i in range(len(l)):
#     if(i==0):
#         count = 1
#         majority = l[i]
#     else:
#         if(l[i]==majority):
#             count += 1
#         else:
#             count -= 1
#             if(count==0):
#                 majority = l[i]
#                 count = 1
#     print(majority, count, sep="-")
# c = 0
# for i in l:
#     if(i==majority):
#         c+=1
# if(c>n//2):
#     print(majority)
# else:
#     print("No Majority Element")







# N = int(input())
# arr = list(map(int, input().split()))
# sum = int(input())
# currSum = arr[0]
# li = 0
# ri = 0
# flag = -1
# while(li<N and ri<N):
#     if(sum==currSum):
#         print("Yes")
#         flag = 1
#         break
#     elif (currSum<sum):
#         ri += 1
#         if(ri<N):
#             currSum += arr[ri];
#     else:
#         currSum -= arr[li]
#         li += 1
# if(flag==-1):
#     print("No")




# M, N = map(int, input().split())
# l = list(map(int, input().split()))
# arr = list(map(int, input().split()))
# count = 0
# for i in arr:
#     if i in l:
#         count += 1
# print(count)



# n = int(input())
# down = 0
# up = 0
# for i in range(1,n+1):
#     up = ((i-2)*2)
#     #print(down)
#     down = ((n-i)*2)+1
#     #print(up)
#     prev = 0
#     for j in range(i):
#         if(j==0):
#             print(i, end=" ")
#             prev = i
#         elif(j%2==1):
#             prev = prev+down
#             print(prev, end=" ")
#         elif(j%2==0):
#             prev = prev+up
#             print(prev, end=" ")
#     prev = 0
#     print()

# n = int(input())
# down = 0
# up = 0
# for i in range(1, n+1):
#     down = ((n-i)*2)+1
#     prev = 0
#     for j in range(i):
#         if(j==0):
#             print(i, end=" ")
#             prev = i
#         elif(j%2==1):
#             prev = prev + down
#             print(prev, end=" ")
#         elif(j%2==0):
#             up = (i-j)*2
#             prev = prev+up
#             print(prev, end=" ")
#     prev = 0
#     print()





# n = int(input())
# l = list(map(int, input().split()))
# oddnum = 0
# for i in l:
#     oddnum = oddnum^i
# print(oddnum)





# n = int(input())
# s = "{:b}".format(n)
# print(s.count('1'))





# A, B = map(int, input().split())
# s = "{:b}".format(A^B)
# print(s.count('1'))