###sorted array
##
##def SelectionSort(array,n):
##    for i in range(n):
##        Min=i
##        for j in range(i+1,n):
##            if(array[j]<array[Min]):
##                Min=j
##        array[i],array[Min]=array[Min],array[i]
##    return array
##n=int(input("enter the length of array:"))
##array=[]
##i=0
##for i in range(n):
##    print(f"enter the element {i}:")
##    array_elements=int(input())
##    array.append(array_elements)
##print("orginal array",array)
##print("Sorted array",SelectionSort(array,n))

def Selection_sort(array,n):
    for i in range(n):
        Min=i
        for j in range(i+1,n):
            if (array[j]<array[Min]):
                Min=j
        array[i],array[Min]=array[Min],array[i]
    return array
n=int(input("\n Enter the Length of array:\n"))
array=[]
i=0
for i in range(n):
    array_elements=int(input(f"Enter The Elements Of the Array{i}:"))
    array.append(array_elements)
print("\nOrginal_Array\n",array)
print("\n Sorted_Array\n",Selection_sort(array,n))
    
