def insertion_sort(arr):
    # Start from the second element (index 1)
    for i in range(1, len(arr)):
        # The current element to be inserted into the sorted part
        current_value = arr[i]
        j=i-1
        while j>=0 and arr[j]> current_value:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=current_value

# Example usage
arr = [12, 11, 13, 5, 6]
print("Original array:", arr)
insertion_sort(arr)
print("Sorted array:", arr)