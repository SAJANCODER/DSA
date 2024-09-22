print("selection sort")


def selection_sort(arr):
    if len(arr) > 1:
        for i in range(1, len(arr)):
            Min = i
            for j in range(i):

                if arr[j] > arr[Min]:
                    Min = j
                    arr[i], arr[Min] = arr[Min], arr[i]

        return arr


arr = [13, 0, 45, 99, 1, 12, 10]
selection_sort(arr)
print("after sort", arr)

print("\n")
print("------------------------------------------------------------------------------------------------")
print("\n")

print("\nbubble sort")


def bubble_sort(arr):
    if len(arr) > 1:
        for i in range(len(arr) - 1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


arr = [12, 4, 2, 1, 8, 0]
print(arr)
bubble_sort(arr)
print(arr)

print("\n")
print("------------------------------------------------------------------------------------------------")
print("\n")

print("merge sort")


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left_array = arr[:mid]
        right_array = arr[mid:]

        merge_sort(left_array)
        merge_sort(right_array)

        i = j = k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1
            k += 1
        while i < len(left_array):
            arr[k] = left_array[i]
            i += 1
            k += 1
        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1


arr = [45, 37, 23, 0, 6, 1, 4, 9, 2]
print(arr)
merge_sort(arr)
print(arr)

print("\n")
print("------------------------------------------------------------------------------------------------")
print("\n")

print("insertation sort")


def insertation_sort(arr):
    if len(arr) > 1:
        for i in range(1, len(arr)):
            j = i
            while arr[j - 1] > arr[j] and j > 0:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1


arr = [45, 66, 37, 24, 56, 2, 23, 12, 1, 9, 0]
print(arr)
insertation_sort(arr)
print(arr)

