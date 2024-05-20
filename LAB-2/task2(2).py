inpt=open("input2.txt","r"	)
otpt=open("output2(2).txt","w")
rng1=int(inpt.readline())
lst1=[int(i) for i in inpt.readline().split()] #list1
rng2=int(inpt.readline())
lst2=[int(i) for i in inpt.readline().split()] #list2
#print(rng1,lst1,rng2,lst2)
rng_final=rng1+rng2

sorted_lst=[]
i1=0
i2=0

while i1!=rng1 or i2!=rng2:
    if i1<rng1 and i2<rng2:
        if lst1[i1]<lst2[i2]:
            sorted_lst.append(lst1[i1])
            i1+=1
        else:
            sorted_lst.append(lst2[i2])
            i2+=1
    elif i1<rng1 and i2==rng2:
        for a in range(i1,rng1):
            sorted_lst.append(lst1[a])
            i1+=1
        break
    elif i1==rng1 and i2<rng2:
        for b in range(i2,rng2):
            sorted_lst.append(lst2[b])
            i2+=1
        break
    
#print(sorted_lst)
for c in range(rng_final):
    otpt.write(f"{sorted_lst[c]} ")
    
inpt.close()
otpt.close()

#============================Code-Explanation============================
"""
First took the values from the input file as range1, list1, range2, list2. Then added range(1+2) and got the final range of the list.
took a empty list named sorted_lst that will store my final sorted list. took two pointers i1, i2. 
i1 and i2 starts iterating the two lists from the front in the while loop. 

__________________________________________________
-----> case1: (The lists are in same lenght)

it will compare the pointer indexes and the lowest value will be added to the final list. Code line (15-21)

-----> case2:(If one of the lists is bigger or smaller)

if i1 or i2 is same as the range of the given list that means that the list is empty now. So the oter pointer can append all the 
values of the remaining list to the final list code line(22-31) and the loop can stop as there are no more values left.
__________________________________________________

Finally wrote the output in the output file. 

"""