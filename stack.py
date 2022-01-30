# from collections import deque

# stack = deque()

# while True:
#     print(stack)

#     s = list(input().strip().split())
    
#     if int(s[0])==1:
#         stack.append(" ".join(s[1:]))
#         continue
    
#     elif int(s[0])== -1:
#         print(stack.pop(), " is removed", end=" ")
#         continue
    
#     elif int(s[0])==2:
#         print(stack[len(stack)-1])
#         continue
        
#     elif int(s[0])==0:
#         break


# SHORTER LEFT WIND MILLS - STACK

# from collections import deque

# n = int(input())

# height = list(map(int, input().split()))

# stack = deque()

# stack.append(0)

# count = [0 for i in range(n)]

# print(0, end=" ")

# for i in range(1, n):
#     last = height[stack[len(stack)-1]]
    
#     if last<height[i]:
#         temp = last
#         counter = 0
#         while len(stack) != 0 and temp<height[i]:
#             counter += 1 + count[stack[len(stack)-1]]
#             stack.pop()
#             if len(stack) != 0:
#                 temp = height[stack[len(stack)-1]]
#             else:
#                 break
#         count[i] = counter
#         print(counter, end=" ")
#         stack.append(i)
        
#     else:
        
#         stack.append(i)
#         print(0, end=" ")


# from collections import deque

    
# stack = deque()

# N = int(input())

# l = list(map(int, input().split()))[::-1]

# stack.append(l[0])

# for i in range(1, len(l)):
#     print(stack)
#     print(l)
#     if l[i] < stack[-1]:
#         stack.append(l[i])
#         l[i] = stack[-1]
#     else:
#         while len(stack)!=0 and l[i]>stack[-1]:
#             stack.pop()
#         if len(stack) != 0:
#             stack.append(l[i])
#             l[i] = stack[-1]
#         else:
#             stack.append(l[i])
# for i in l[::-1]:
#     print(i, end=" ")

# from collections import deque

# string = input()

# index = []

# stack = deque()

# for i in range(len(string)):
#     if string[i] == "(":
#         stack.append(i)
#     elif string[i] == ")":
#         if len(stack)>0:
#             stack.pop()
#         else:
#             index.append(i)
# ans = ""
# for i in range(len(string)):
#     if not i in stack and not i in index:
#         ans += string[i]

# print(ans)

# from collections import deque

# from collections import deque

# string = input()

# stack = deque()

# flag = 0

# for i in range(len(string)):
#     if string[i] in ["(", "{", "["]:
#         stack.append(string[i])
#     else:
#         print(stack)
#         if string[i]=="}" and stack[len(stack)-1]=="{" and len(stack) != 0:
#             stack.pop()
#         elif string[i]==")" and stack[len(stack)-1]=="(" and len(stack) != 0:
#             stack.pop()
#         elif string[i]=="]" and stack[len(stack)-1]=="[" and len(stack) != 0:
#             stack.pop()
#         elif string[i] not in ["]", "}", ")"]:
#             flag = 1
#             print("no")
#             break
#         print(string[i])
#         print(stack)
#         print()
    
# if flag==0 and len(stack)==0:
#     print("yes")
# elif flag==0:
#     print("no")


# Python3 code to Check for 
# balanced parentheses in an expression
# open_list = ["[","{","("]
# close_list = ["]","}",")"]
  
# # Function to check parentheses
# def check(myStr):
#     stack = []
#     for i in myStr:
#         if i in open_list:
#             stack.append(i)
#         elif i in close_list:
#             pos = close_list.index(i)
#             if ((len(stack) > 0) and
#                 (open_list[pos] == stack[len(stack)-1])):
#                 stack.pop()
#             else:
#                 return "Unbalanced"
#     if len(stack) == 0:
#         return "Balanced"
#     else:
#         return "Unbalanced"
  
  
# # Driver code
# string = "[{({[[[[(((({{{{({([])})]}}}}))))]]]]})}]"
# print(string,"-", check(string))
  
import sys
N, L = map(int, input().split())
edges = []
for i in range(L):
    l = list(map(int,input().split()))
    edges.append(l)
distance = {}
distance[1] = 0
for i in range(2, N+1):
    distance[i] = sys.maxsize
print(edges)
for k in range(N-1):
    dist = distance.values()
    for i in edges:
        distance[i[1]] = min(distance[i[0]]+i[2], distance[i[1]])
    new = distance.values()
    if dist == new:
        break
keys = distance.keys()-[1]
for i in keys:
    print(distance[i], end=" ")

