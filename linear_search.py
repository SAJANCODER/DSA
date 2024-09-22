pos=-1

def linear_search(arr,n):
    i=0
    while i<len(arr):
        if arr[i]==n:
            globals() ['pos']=i
            return True
        i=i+1
    return False
arr=[4,6,2,7,9]
n=9
if linear_search(arr,n):
    print("found",pos+1)  #+1 for human numbers ,so 9 is in 5
else:
    print("not found")


