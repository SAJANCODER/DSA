def insert_sort(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1

arr=[12,4,5,1,0,8,5,4,3]
print(arr)
insert_sort(arr)
print(arr)