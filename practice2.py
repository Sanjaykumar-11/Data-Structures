# # X = int(input())
# # Y = int(input())
# # Z = int(input())
# # flag = 0
# # if (X < Z and Y < Z) or Z%(min(X, Y))==1:
# #     flag = 1
# #     print(-1)
# # if flag==0:
# #     if X==Z or Y==Z:
# #         print(1)
# #     else:
# #         minimum = min(X, Y)
# #         maximum = max(X, Y)
# #         count = 1
# #         while(maximum != Z):
# #             maximum -= minimum
# #             if count==1:
# #                 count += 1
# #             else:
# #                 count+=2
# #         print(count)

# password = input()
# special_character = ['#', '!', '_', '$', '@']
# special_character_count = 0
# number_count = 0
# uppercase_count = 0
# lowercase_count = 0
# length = False

# for i in password:
#     if i.isnumeric():
#         number_count += 1
#     elif i in special_character:
#         special_character_count += 1
#     elif i.isupper():
#         uppercase_count += 1
#     elif i.islower():
#         lowercase_count+=1

# if len(password)>=8 and len(password)<=25:
#     length = True

# if special_character_count>=1 and number_count>=2 and uppercase_count>=1 and lowercase_count>=1 and length:
#     print("VALID")
# else:
#     print("INVALID")

# print(special_character_count, number_count, uppercase_count, lowercase_count, length, sep=" -- ")

# def shift(char, pos):
#     global alphabets
#     current = alphabets.index(char)
#     new = (current + pos)%26
#     return alphabets[new]
    
# M = input()
# X = int(input())
# Y = int(input())
# encrypted = ""
# alphabets = "abcdefghijklmnopqrstuvwxyz"
# for i in M:
#     if i.isnumeric():
#         encrypted += str(int(i)+Y)
#     elif i in [" ", ".", ",", ";"]:
#         encrypted += i
#     else:
#         encrypted += shift(i,X)
# print(encrypted)

# arr = list(map(int, input().split()))
# arr.sort()
# valid = []
# start = 0
# while start<len(arr):
#     end = start+1
#     while end<len(arr):
#         if arr[start] + arr[end] in arr:
#             valid.append([arr[start], arr[end], arr[start]+arr[end]])
#         end += 1
#     start += 1
# if len(valid)==0:
#     print(-1)
#     exit

# for j in range(len(valid)):
#     for i in range(len(valid)-1):
#         # print(valid[i][-2:], valid[i+1][:-1], sep= "  -  - ")
#         if valid[i][-2:]==valid[i+1][:-1]:
#             temp = valid[i+1][-1]
#             print(temp)
#             valid[i].append(temp)

# for i in range(len(valid)):
#     for k in range(len(valid)):
#         # for k in range(len(valid)):
#         if valid[i][-2:]==valid[k][:2]:
#             temp = valid[k][2:]
#             valid[i].extend(temp)


# print(valid)
# print(*max(valid, key=len), end=" ")

# time = list(map(int, input().split(':')))
# print(time)
# if time[0]>23 or time[0]<0:
#     print("INVALIDINPUT")
# else:
#     if time[0]>=12 and time[0]<=23:\
#         print("PM")
#     else:
#         print("AM")

# def HCF(a, b):
#     return a if b==0 else HCF(b, a%b)

# a = int(input())
# b = int(input())

# hcf = HCF(a, b)
# lcm = (a*b)//hcf
# print(lcm-hcf)


# string = input()
# start = input()
# end = input()
# count = 0
# i = 0
# j = 1
# while(j<len(string)):
#     if string[i]==start and string[j]==end:
#         count += 1
#     i += 1
#     j += 1
# print(count)

# def isPalindrome(s):
#     if s==s[::-1]:
#         return True
#     else:
#         return False

# number = str(int(input())+1)

# while not isPalindrome(number):
#     number = str(int(number)+1)

# print(number)

# n = input()
# X, Y = map(int, input().split())
# n = n*(Y)
# if n[X-1]==n[Y-1]:
#     print("YES")
# else:
#     print("NO")

# day = input().strip()
# date = int(input())
# days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
# month = ["0" for i in range(31)]
# index = days.index(day)
# for i in range(31):
#     print(index)
#     month[i] = days[index%7]
#     index += 1
# print(month[date-1])

def isEqual(row_pos, col_pos):
    global sub_matrix, M, matrix
    print(row_pos, col_pos, sep=" ")
    current = []
    row = row_pos
    for i in range(M):
        l = []
        col = col_pos
        for j in range(M):
            l.append(matrix[row][col])
            col += 1
        current.append(l)
        print(current)
        row += 1
    if sub_matrix==current:
        return True
    else:
        return False
        
N = int(input())
M = int(input())

matrix = []
sub_matrix = []

for i in range(N):
    l = list(map(int, input().split()))
    matrix.append(l)

for i in range(M):
    l = list(map(int, input().split()))
    sub_matrix.append(l)

flag = 0

for i in range(N-M+1):
    for j in range(N-M+1):
        if isEqual(i, j):
            flag = 1
            print("TRUE")
            break
if flag==0:
    print("FALSE")