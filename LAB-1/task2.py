#task-2
inpt=open("input2.txt","r")
otpt=open("output2.txt","w")

rng=inpt.readline()
elem=inpt.readline().split( )

lst=[]
for i in range (len(elem)):
    lst.append(int(elem[i]))
    
#print(lst,"<-----")

def bubbleSort(arr):
    
    sorted_status=True
    
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:          #if-1
                sorted_status=False
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
        if sorted_status==True:            #if-2
            break

    return arr

final_lst=bubbleSort(lst)

for k in final_lst:
    otpt.write(f"{k} ")
    
inpt.close()
otpt.close()

#_______________________Code-Explanation_____________________________________
""" 
Same as before we opened the input file and took the range (5). Then took the numbers in a list by using  .split( ) and a loop.
For the bubble sort function we passed the list and there used a flag(sorted_status) to check if the list is sorted or not.

If the list is not sorted it will go into (if-1) then the status will become False and the complexity will be θ(n^2)

But if the list is sorted it will enter the second if bracnch (if-2) then the loop will break and there is no second loop Hence we will get 
the complexity θ(n).
"""
