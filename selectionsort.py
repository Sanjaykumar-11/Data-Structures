#Selection sort
def selectionsort(arr):
    for i in range(len(arr)):
        min = i
        print(arr[min])
        for j in range(i+1, len(arr)):
            if(arr[j]<arr[i]):
                min = j
        arr[i], arr[min] = arr[min], arr[i]
        print(arr)
    return arr

l = list(map(int, input("Enter the elements of the array:").split()))
selectionsort(l)

#Time complexity: O(n^2)