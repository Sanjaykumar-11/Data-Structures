arr = list(map(int, input().split()))
arr.sort()
valid = []
start = 0
while start<len(arr):
    end = start+1
    while end<len(arr):
        if arr[start] + arr[end] in arr:
            valid.append([arr[start], arr[end], arr[start]+arr[end]])
        end += 1
    start += 1

if len(valid)==0:
    print(-1)
else:
    for i in range(len(valid)):
        for j in range(len(valid)):
            if valid[i][-2:]==valid[j][:2]:
                temp = valid[j][2:]
                valid[i].extend(temp)
    ans = max(valid, key=len)
    print(*ans, end=" ")