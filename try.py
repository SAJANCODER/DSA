def merge_array(arr):
    if len(arr)>1:
        mid = len(arr)//2

        left_array=arr[:mid]
        right_array=arr[mid:]
        merge_array(left_array)
        merge_array(right_array)

        i=j=k=0
        while i<len(left_array) and j< len(right_array):
            if left_array[i]< right_array[j]:
                arr[k]=left_array[i]
                i+=1
            else:
                arr[k]=right_array[j]
                j+=1
            k+=1

        while i<len(left_array):
            arr[k]=left_array[i]
            i+=1
            k+=1
        while j<len(right_array):
            arr[k]=right_array[j]
            j+=1
            k+=1


n=int(input("enter the length os the array:"))
arr=[]
for i in range(n):
    num=int(input(f"enter the {i} element:"))
    arr.append(num)
print("orginal array",arr)
merge_array(arr)
print("merged_array",arr)
