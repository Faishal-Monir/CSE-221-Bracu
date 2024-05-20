inpt=open("input4.txt","r"	)
otpt=open("output4.txt","w")
line1=[int(i) for i in inpt.readline().split()]
rng=line1[0]
node=line1[1]


#=======================Formating====================================

time_slot=[]

for i in range(rng):
    temp=[int(j) for j in inpt.readline().split()]
    time_slot.append((temp[0],temp[1]))
# print(time_slot)                                 
#[(5, 7), (2, 4), (6, 8), (8, 10), (1, 3), (7, 9), (3, 5), (2, 6)] --> For input 4


#==================Sorting function==========================

# Start time / End time sorting selection ----> 0 for start time sort ||  1 for end time based sorting 
def sort_koro(arr,val): 
    n = len(time_slot)   
    m=time_slot
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if m[j][val] < m[min_idx][val]:        
                min_idx = j
        m[i], m[min_idx] = m[min_idx], m[i]
    return arr


#==================Sorting selection and corner case check===================
#Corner Case check for input (3)
max_end=time_slot[0][1]
max=time_slot[0][1]
status=False

for b in range(len(time_slot)):
    if time_slot[b][1]>max_end:
        max=time_slot[b][1]
        
if max_end==max:
    time_slot.reverse( )
    status=True
    
#Sending node_time to sorting function
if status==True:
    pass
else:
    sort_koro(time_slot,0)

    
# print(time_slot,"<==========================")

#============================Data assign and logic building=====================================

endtime=[]          #To store (N) numbers of end time in a list
node_time=[]         #To store (N) numbers of time schedules in a list

for i in range(0,node):
    s,e=time_slot.pop(0)    
    endtime.append(e)
    node_time.append([(s,e)])

#print("====Node time====",node_time,"\n====End time of the Nodes====",endtime,sep="\n") 

#print("\nRemaining slots-->",time_slot)

gap=[]                                              # (3, 5), (5, 7), (6, 8), (7, 9), (8, 10)
for i in time_slot:
    for j in range(len(endtime)):
        gap.append(endtime[j]-i[0])
    # print(gap)
    min=gap[0]
    min_idx=0
    for k in range(len(gap)):
        if gap[k]<0:
            min=gap[k]
            min_idx=k
        elif gap[k]==0:
            min=gap[k]
            min_idx=k
        elif gap[k]<min:
            min=gap[k]
            min_idx=k  
              
    if i[0]>=endtime[min_idx]:  
        node_time[min_idx].append(i)
        endtime[min_idx]=i[1]
        
    min_idx=None
    gap=[]

#print(node_time)

#=============Finally counting and printing all the times of each nodes ================================
counter=0
for i in node_time:
    for j in i:
        counter+=1
otpt.write(str(counter))



inpt.close()
otpt.close()

#============================Code-Explanation============================
"""
Took the range and the person info from line 1 of the input file. Made a list of all the time slots as before tasks. Now for the 
twist wrote a function sort_koro that sorts the time slots either regarding start time if val==0 otherwise val===1 for end time
based sorting to make the code dynamic.Now to check the corner case if a maximum end tiem has come or not, for that we already took
the first end time to be the max end time and if there is a max end time after the first slot then it will be stored in the max
variable if not then the first end time is the maximum working time.But for the algo to work we cannot take the max time first 
so we reversed the time slots and check for each condition to avoid the corner case. Now in the code we sort (N) numbers of end
time and node times in the fnal lists. Then Initially we store N number of times and their end times in the lists . Now lastly from 
line 70 to 92  we cxheck for each person and update the minimum gap person with that work so that n people can do maximum number of 
tasks in that given time. lastly we took a nested loop and counted the all time slots and printed them in the output file.
 
 For better understanding please check the comments and the sections that I made in the code. 
 Thank You !
 
"""