#insertion sort 
def insertionsort(arr):
    for i in range(1,len(arr)): 
        temp = arr[i] 
        j = i-1
        while (arr[j]>temp and j>=0):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr

l = list(map(int, input("Enter the elemtents of the array: ").split()))
print(insertionsort(l))

#Complexity analysis
#best case: Acending order -> O(n) comparisions, O(1) swaps
#Worst case: Decending order -> O(n^2)

