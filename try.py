#selection sort


def selection_sort(arr):
    if len(arr)>1:
        for i in range(1,len(arr)):
            Min=i
            for j in range(i):
                if arr[j]>arr[Min]:
                    Min=j
                    arr[i],arr[Min]=arr[Min],arr[i]
        return arr
                       
    
arr=[13,0,45,99,1,12,10]
print(arr)
selection_sort(arr)
print("after sort",arr)
