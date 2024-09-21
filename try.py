#selection sort

def selection_sort(arr,n):
    for i in range(n):
        Min=i
        for j in range(i+1,n):
            if (arr[j]<arr[Min]):
                Min=j
        arr[i],arr[Min]=arr[Min],arr[i]
    return arr
n=int(input("enter the length of selection sort:"))
arr=[]
for i in range(n):
    num=int(input(f"enter the array element{i}:"))
    arr.append(num)
print("orginal array",arr)
print("sorted array",selection_sort(arr,n))
    
            
