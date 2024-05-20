#============================Input Output=============================================
inpt=open("input2.txt","r")
otpt=open("output2.txt","w")
rng=int(inpt.readline())
lst=[int(i) for i in inpt.readline().split()]

#=========================================Code===========================
def compare(a,b):
    if a>b:
        return a
    return b


#Same code as merge sort But modified (T.c= logn)  
def biggest_value_finder(arr):
    if len(arr) <= 1:
        return arr[0]     #just passing the value of the list this time.
    else:
        mid = len(arr)//2                     #Finding the mid idx of the array
        
        a1 = biggest_value_finder(arr[:mid])  #recursively calling the function so that it can divide the left part of that array .
        a2 = biggest_value_finder(arr[mid:])  #recursively calling the function so that it can divide the right part of that array. 
        
        return compare(a1, a2)                #passing the lists after the recursive calls to the biggest_value_finder function.  

temp=biggest_value_finder(lst)
otpt.write(str(temp))

otpt.close( )
inpt.close( )