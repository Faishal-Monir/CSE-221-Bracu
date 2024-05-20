#============================Input Output=============================================
inpt=open("input3.txt","r")
otpt=open("output3.txt","w")
rng=int(inpt.readline( ))
lst=[int(i)for i in inpt.readline().split()]

#=========================================Code===========================

def calc(left,right,t_count):
    temp_arr=[]
    i=0
    j=0

    while i<len(left) and j<len(right):
        if left[i]>=right[j]:        
            # print(left,right)    
            temp_arr.append(left[i])        #Appending i element as it is greater than j element
            i+=1
            t_count=t_count+len(right[j:])  #Counting the numbers permutatively
        else:
            temp_arr.append(right[j])       #Appending j element as it dosent fullfil inverse count condition
            j+=1 
    
    for elem in range(i,len(left)):         #appending remaining elements using the below two loops if tehlists are un even in size
        temp_arr.append(left[elem])
    
    for elem in range(j,len(right)):
        temp_arr.append(right[elem])
        
    return temp_arr,t_count
    





def alien(arr,count):
    if len(arr)<=1:
        temp_count=0
        return arr , temp_count                      #Base case returning one lenght array with a count of 0 .
    else:
        mid=len(arr)//2                              #finding Mid
        
        l_arr,l_count=alien(arr[:mid],count)         #Recursively calling alien/itself     
        r_arr,r_count=alien(arr[mid:],count)         #Recursively calling alien/itself            
        
    return calc(l_arr,r_arr,l_count+r_count)  #calling the calculation function while pasisng the initial counter value as 0           


srt_arr,cnt=alien(lst,0)
otpt.write(str(cnt))

otpt.close()
inpt.close()