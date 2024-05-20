#============================Input Output=============================================
inpt=open("input5.txt","r")
otpt=open("output5.txt","w")


rng=int(inpt.readline())
lst=[int(i) for i in inpt.readline().split()]

#=========================================Code===========================

def partition(arr,left,right):
    pvt=arr[right]
    i=left-1
    for elem in range(left,right):
        if arr[elem]<=pvt:
            i+=1
            arr[i],arr[elem]=arr[elem],arr[i]
    arr[i+1],arr[right]=arr[right],arr[i+1] 
    
    return i+1
def quicksort(arr,left,right):
    if left<right:
        part=partition(arr,left,right)        #fixing pivot index with the help of partition function
        
        quicksort(arr,left,part-1)            #Recursive call by making smaller list with the help of divide and conquer
        quicksort(arr,part+1,right)           #Recursive call by making smaller list with the help of divide and conquer
    return arr
        
final_lst=quicksort(lst,0,rng-1)

for i in final_lst:
    otpt.write(str(i)+" ")
    
otpt.close()
inpt.close()