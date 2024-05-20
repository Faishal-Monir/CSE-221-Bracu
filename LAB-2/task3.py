inpt=open("input3.txt","r"	)
otpt=open("output3.txt","w")
rng=int(inpt.readline())
time_slot=[]

for i in range(rng):
    temp=[int(j) for j in inpt.readline().split()]
    time_slot.append((temp[0],temp[1]))
# print(time_slot)                                 #[(1, 3), (2, 5), (3, 7), (4, 6), (6, 8), (7, 9)] --> For input 1


n = len(time_slot)   #Selection sorting the end times in ascending order(input-1) 
m=time_slot
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if m[j][1] < m[min_idx][1]:
            min_idx = j
    m[i], m[min_idx] = m[min_idx], m[i]

# print(time_slot)  #[(1, 3), (2, 5), (4, 6), (3, 7), (6, 8), (7, 9)] --> Sorted regarding end time for input 1 
    
final_time=[]
counter=0
endtime=0

#print(time_slot)

for i in range (len(time_slot)):
    
    if final_time==[]:
        final_time.append(time_slot[i])
        counter+=1
        endtime=final_time[-1][1]
        
    elif time_slot[i][0]>=endtime:
        final_time.append(time_slot[i])
        counter+=1
        endtime=final_time[-1][1]

#Printing as output format        
otpt.write(f"{counter}\n")

for a in final_time:
    otpt.write(f"{a[0]} {a[1]}\n")
    
inpt.close()
otpt.close()

#============================Code-Explanation============================
"""
Took the range of numbers at line 3. Then created an empty list to store the time slots. Then wrote a loop and appended all the time
slots in that list (line 9).
Then wrote a selection sort to sort the (end times) in ascending order and sorted out time_slot list(Line 21).Then  took a list named final time
as it will store the final time slots. ANd a counter and a end time variable for each slot. 

Then wrote a loop to itterate the slots and if th efinal time is empty it will take the first time slot and update the counter and 
endtime dynamically. And in the elif branch if the start time of a new task is equal or greater than the previous end time then that 
task can be done by the person and it will append that task in the final list and finally wrote the output files as Counter first
and the time slots.

For input (1) both_slots 6--8 and 7--9 are valid but per question any of them are right but from logic time slot[1 to 8] the lesser 
time consuming tasks should be done so thats why took 6-8 and if there were any tasks next as 8-9 it would be done next(as we need to
complete as much as tasks possible)

"""