def insertion_sort(arr):
    for i in range(1, len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1

# Example usage
arr = [12, 11, 13, 5, 6]
print("Original array:", arr)
insertion_sort(arr)
print("Sorted array:", arr)