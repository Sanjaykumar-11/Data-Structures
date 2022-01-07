# from math import sqrt
# def isPronic(n):
#     global l
#     n = int(n)
#     if n in l:
#         return True
#     if n==0:
#         return True
#     for i in range(2, int(sqrt(n))+1,2):
#         if (i*(i+1)==n):
#             return True
#     return False

# l = []
# for i in range(10000):
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

from math import sqrt
def isPronic(n):
    global l
    n = int(n)
    if n in l:
        return True
    if n==0:
        return True
    for i in range(2, int(sqrt(n))+1,2):
        if (i*(i+1)==n):
            return True
    return False

l = []
for i in range(10000):
    l.append(i*(i+1))
N = input().strip()
right = 0
left = 0
size = len(N)
while(left<size):
    right = left
    while(right<size):
        temp = N[left:right+1]
        if (int(temp[-1])%2==0): 
            if isPronic(temp):
                print(int(temp), end=" ")
                if N[left]=="0":
                    break
                right += 1
            else:
                right += 1
        else:
            right += 1
    left += 1