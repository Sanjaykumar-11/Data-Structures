#bubble sort

def bubblesort(arr):
    for i in range(len(arr)-2):
        for j in range(len(arr)-i-1): #last i numbers already in sorted order
            if(arr[j+1]<arr[j]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

l = list(map(int, input("Enter the elements: ").split()))
print(bubblesort(l))

#performance analysis
#Worst case: O(n^2)