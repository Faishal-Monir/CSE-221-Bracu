#============================Input Output=============================================
inpt=open("input1.txt","r")
otpt=open("output1.txt","w")


rng=int(inpt.readline())
lst=[int(i) for i in inpt.readline().split()]

#=========================================Code===========================
# N complexity solution
def merge(a, b):
    sorted_lst=[]
    rng1=len(a)
    rng2=len(b)
    i1=0
    i2=0

    while i1!=rng1 or i2!=rng2:
        if i1<rng1 and i2<rng2:
            if a[i1]<b[i2]:
                sorted_lst.append(a[i1])
                i1+=1
            else:
                sorted_lst.append(b[i2])
                i2+=1
        elif i1<rng1 and i2==rng2:
            for i in range(i1,rng1):
                sorted_lst.append(a[i])
                i1+=1
            break
        elif i1==rng1 and i2<rng2:
            for j in range(i2,rng2):
                sorted_lst.append(b[j])
                i2+=1
            break
    return sorted_lst


#logn solution
def mergeSort(arr):
    if len(arr) <= 1:     #if the list is empty or has one element it returns the array 
        return arr
    else:
        mid = len(arr)//2      #Finding the mid idx of the array
        
        a1 = mergeSort(arr[:mid])  #recursively calling the function so that it can divide the left part of that array .
        a2 = mergeSort(arr[mid:])  #recursively calling the function so that it can divide the right part of that array. 
        return merge(a1, a2)       #passing the lists after the recursive calls to the merge function.
    
fun_call=mergeSort(lst)

for i in fun_call:           #passing the values to the output.
    otpt.write(f"{i} ")
    
otpt.close( )
inpt.close( )