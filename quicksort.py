#Quick sort implementation in python
#Here I considered last element as pivot

#Quick sort uses "Divide and Conquerer" algorithm to sort an array

#function to partition the array
#left side of the pivot should be less than pivot and right side should be greater than or equal to pivot

#start = starting index
#end = ending index

def partition(start, end, arr):
    pivot = arr[end] #selecting last element as pivot
    i = start-1 #initiation the pointer
    for j in range(start, end): #traverse the array start to end-1 (without pivot element)
        if(arr[j]<=pivot):
            i += 1 #increment i by 1
            arr[i], arr[j] = arr[j], arr[i] #swap the element
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i+1 #returning pivot index

def quicksort(start, end, arr):
    if(len(arr)==1):
        return arr
    if(start<end): #checking whether the start index is less than end
        p = partition(start, end, arr)
        #recursive function calls
        quicksort(start, p-1, arr)
        quicksort(p+1, end, arr)
    return arr

arr = list(map(int, input("Enter the element of the array :").split(' ')))
quicksort(0, len(arr)-1, arr)
print("Sorted array: ",arr)

#Time complexity:
#best case: O(nlogn)
#worst case: O(n**2)