
#
# def Selection_sort(array,n):
#     for i in range(n):
#         Min=i
#         for j in range(i+1,n):
#             if (array[j]<array[Min]):
#                 Min=j
#         array[i],array[Min]=array[Min],array[i]
#     return array
# n=int(input("\n Enter the Length of array:\n"))
# array=[]
# i=0
# for i in range(n):
#     array_elements=int(input(f"Enter The Elements Of the Array{i}:"))
#     array.append(array_elements)
# print("\nOrginal_Array\n",array)
# print("\n Sorted_Array\n",Selection_sort(array,n))
#

# selection sort


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
print(arr)
selection_sort(arr)
print("after sort", arr)
