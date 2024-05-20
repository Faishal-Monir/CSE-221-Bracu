import math  #To use math.infinity
#============================Input Output=============================================
inpt=open("input4.txt","r")
otpt=open("output4.txt","w")
rng=int(inpt.readline( ))
lst=[int(i)for i in inpt.readline().split()]

#=========================================Code===========================
def max_idx_calc(arr):
    left=-math.inf                    #for calculation setting the value to the lowest point possible .
    right=-math.inf
    
    max_mid=len(arr)//2
    for i in range(0,max_mid):        #finding the maximum value for i when i<j for the half of the array.
        if arr[i]>left:
            left=arr[i]
    for j in range(max_mid,len(arr)):  #finding the absolute maximum value for j when i<j and j**2 for the half of the array.
        if abs(arr[j])>right:
            right=abs(arr[j])

    
    return left+(right**2)


def value_finder(arr):
    if len(arr)==0:               #For a empty list
        return "====\nERROR!!\nList is empty\nValue cannot be found\n===="
    if len(arr)==1:               #For single item list 
        return -math.inf
    if len(arr)==2:               #For dual item list calculations
        return arr[0]+(arr[1])**2
    
    mid=len(arr)//2               #MId for using divide and conquer 
    left_arr=value_finder(arr[:mid])
    right_arr=value_finder(arr[mid:])
    
    big_value=max_idx_calc(arr)
    
    return max(left_arr,right_arr,big_value)   #returning the maximum value after the final recursive calls. 


max_val=value_finder(lst)

otpt.write(str(max_val))

otpt.close()
inpt.close()
