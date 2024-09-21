##def bubble_sort(arr):
##    for i in range(len(arr)-1,0,-1):
##        for j in range(i):
##            if (arr[j]>arr[j+1]):
##                arr[j],arr[j+1]=arr[j+1],arr[j]
##    return arr
##length=int(input())
##arr=[]
##for i in range(length):
##    num=int(input(f"enter the {i} element"))
##    arr.append(num)
##print("orginal array",arr)
##print("sorted array",bubble_sort(arr))
##    
#buble sort

def buble_sort(arr,n):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
n=int(input("enter lenght of buble sort:"))
arr=[]
for i in range(n):
    num=int(input(f"enter the value of {i}"))
    arr.append(num)
print("orginal array",arr)
print("sorted array",buble_sort(arr,n))
            
