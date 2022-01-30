"""
For Binary Search Value should be in sorted order

"""
import sys
sys.setrecursionlimit(10**9)
def binarysearch(l, start, end, n):
    mid = (start + end)//2
    if start>end:
        print("Not found")
        return
    if l[mid]==n:
        print("Element found at: ", mid)
        return
    else:
        if l[mid]>n:
            binarysearch(l, start, mid-1,n)
        else:
            binarysearch(l, mid+1, end, n)

l = [9,7,3,2,1]
l.sort()
n = 3
binarysearch(l, 0, len(l)-1, n)