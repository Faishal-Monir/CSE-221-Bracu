#============================Input Output=============================================
inpt=open("input6.txt","r")
otpt=open("output6.txt","w")

temp_1=inpt.readline().split()
rng=int(temp_1[0])
lst=[int(i) for i in inpt.readline().split()]
temp_2=inpt.readline().split()
rng_2=int(temp_2[0]) 
query_lst=[int(inpt.readline()) for i in range(rng_2)]   


#=========================================Code===========================

def part(arr,left,right):          #Quicksort partition function
    temp_pvt=arr[right]
    i=left-1
    for elem in range(left,right):
        if arr[elem]<=temp_pvt:
            i+=1
            arr[i],arr[elem]=arr[elem],arr[i]
    arr[i+1],arr[right]=arr[right],arr[i+1] 
    
    return i+1

def small(arr,left,right,pos):
    if left==right:             #for 1 lenght list 
        return arr[pos]
    
    #fixing pivot
    pvt_idx=part(arr,left,right)

    if pos==pvt_idx:
        return arr[pos]                     #Base case the smallest value

    elif pos<pvt_idx:
        return small(arr,left,pvt_idx-1,pos) #if smaller element is on left side of pivot   
        
    elif pos>pvt_idx:
        return small(arr,pvt_idx+1,right,pos) #if smaller element is on right side of pivot 
    
    

for q in query_lst:
    req=small(lst,0,rng-1,q-1)
    otpt.write(str(req)+"\n")
    
otpt.close()
inpt.close()